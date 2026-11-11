#!/usr/bin/env python3
"""Keep current Cydia artifacts, validate links, and refresh repository checksums."""
import argparse
import bz2
import gzip
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE_STEMS = {
    'com.michirose.weather': 'michirose-weather',
    'com.michirose.airpodsfix': 'michirose-airpods',
    'com.michirose.cellulardata': 'cellular-data-settings',
}


def maintain(prune=False):
    packages = (ROOT / 'Packages').read_bytes()
    entries = [dict(re.findall(r'^([\w-]+): (.*)$', stanza, re.M))
               for stanza in packages.decode().strip().split('\n\n')]
    assert len({e['Package'] for e in entries}) == len(entries)
    keep = set()
    for entry in entries:
        name = entry['Filename'].removeprefix('./')
        assert Path(name).name == name
        data = (ROOT / name).read_bytes()
        assert len(data) == int(entry['Size']), name
        for field, algorithm in [('SHA256', 'sha256'), ('SHA1', 'sha1'), ('MD5sum', 'md5')]:
            assert hashlib.new(algorithm, data).hexdigest() == entry[field], name
        keep.add(name)
        stem = SOURCE_STEMS.get(entry['Package'])
        if stem:
            source = f'{stem}-source-{entry["Version"].replace("~", "-")}.tar.gz'
            assert (ROOT / source).is_file(), source
            keep.add(source)
    build = json.loads((ROOT / 'PACKAGE-CONTENTS.json').read_text())['build']
    ipa = f'Telegraphica-0.1.0-beta1-build{build}-ios6-armv7.ipa'
    assert (ROOT / ipa).is_file()
    keep.add(ipa)
    artifacts = {p.name for p in ROOT.iterdir()
                 if p.is_file() and (p.suffix in ('.deb', '.ipa') or p.name.endswith('.tar.gz'))}
    obsolete = artifacts - keep
    # A stale depiction must be corrected before pruning anything it links to.
    for page in ROOT.rglob('*.html'):
        for target in re.findall(r'(?:href|src)=["\']([^"\']+)', page.read_text()):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            path = (page.parent / unquote(url.path)).resolve()
            assert path.is_relative_to(ROOT) and path.exists(), (page, target)
            assert path.name not in obsolete, (page, target)
    if not prune:
        assert not obsolete, f'Obsolete artifacts: {sorted(obsolete)}; run with --prune'
    for name in sorted(obsolete):
        (ROOT / name).unlink()
    (ROOT / 'Packages.gz').write_bytes(gzip.compress(packages, mtime=0))
    (ROOT / 'Packages.bz2').write_bytes(bz2.compress(packages))
    release = (ROOT / 'Release').read_text().split('MD5Sum:')[0]
    for title, algorithm in [('MD5Sum', 'md5'), ('SHA256', 'sha256')]:
        release += title + ':\n'
        for name in ('Packages', 'Packages.gz', 'Packages.bz2'):
            data = (ROOT / name).read_bytes()
            release += f' {hashlib.new(algorithm, data).hexdigest()} {len(data)} {name}\n'
    (ROOT / 'Release').write_text(release)
    files = sorted(p for p in ROOT.rglob('*') if p.is_file()
                   and '.git' not in p.relative_to(ROOT).parts and p.name != 'SHA256SUMS')
    (ROOT / 'SHA256SUMS').write_text(''.join(
        f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT)}\n' for p in files))
    assert gzip.decompress((ROOT / 'Packages.gz').read_bytes()) == packages
    assert bz2.decompress((ROOT / 'Packages.bz2').read_bytes()) == packages
    print(f'Validated {len(entries)} Cydia packages, source links and current IPA; removed {len(obsolete)} obsolete artifacts.')
    print(f'Retained artifacts: {", ".join(sorted(keep))}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prune', action='store_true', help='Remove superseded build artifacts from the current tree')
    maintain(parser.parse_args().prune)
