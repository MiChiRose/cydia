# Telegraphica Cydia repository

Source: **https://michirose.github.io/telegraphica-cydia/**

In Cydia, choose Manage → Sources → Edit → Add and enter the source URL.
A custom domain can be attached later; no home-network address is required.

## Testing status

This is an experimental repository for jailbroken **iOS 6** devices.
**Telegraphica Background is a companion, not the full application.**
It requires an existing Telegraphica installation. Cydia installs and starts the
companion automatically; users do not need a terminal, SSH or a developer Mac.
Closed-app delivery and battery behavior are still undergoing device validation.
Do not treat this as a stable notification release.

The full app is not published here yet. The repository contains distributable
companion binaries, package install/removal scripts, descriptions and checksums.
Application source history, Telegram API configuration, sessions, messages,
database keys, signing private keys and provisioning profiles are not included.

SHA256SUMS allows download integrity checks. These indexes do not yet have an APT
Release signature. Transport compatibility must be checked in actual iOS 6 Cydia.
Do not disable certificate checks or install an untrusted root certificate.

For package removal, use Cydia. Removal unloads only this companion and preserves
the app and account data. Turning off Background Notifications in Telegraphica
releases its background assertion; the helper remains installed until removed.
