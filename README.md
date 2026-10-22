# Telegraphica for iOS 6 — beta 1

Telegraphica is an unofficial Telegram client for jailbroken iOS 6 devices.
The application and its background companion can be installed through Cydia;
no terminal, SSH or development Mac is needed.

## Install through Cydia

1. A jailbreak and **AppSync Unified compatible with iOS 6** are required.
   AppSync must be available from your trusted package source; this repository
   does not redistribute it. See the [AppSync project](https://github.com/akemin-dayo/AppSync).
2. In Cydia open Manage → Sources → Edit → Add, and enter:
   **https://michirose.github.io/telegraphica-cydia/**
3. Refresh, select **Telegraphica** (the full application), and tap Install.
   Its **Telegraphica Background** dependency installs automatically.
4. Open Telegraphica and log in to **your own** Telegram account.

If this source was already added, refresh it: it now includes the full app.
Do not add a home IP address. Do not remove an existing Telegraphica app before
updating; deleting its Home-screen icon can erase its local data.

## Downloads

[Download beta 1: IPA, DEB and SHA-256 checksums](https://github.com/MiChiRose/telegraphica-cydia/releases/tag/ios6-v0.1.0-beta1)

The IPA is an alternative for a compatible jailbreak IPA installer with AppSync.
Downloading an IPA in Safari alone does not install it. This is **not** a signed
stock-iOS build. iOS 7 and newer are not supported by this beta package.

## What was checked

The app runs on **iPhone 4s / iOS 6.1.3**. The full Cydia update completed on that
combination and preserved the existing login and dialogs. A fresh physical
installation on an empty device and other ARMv7 devices have not yet been checked.
This is a beta; real audio/video calls are not implemented, Music search has known
issues, and in-app proxy settings are not available yet. Closed-app notifications
use the jailbreak companion; long-term battery behavior remains experimental.

Packages contain app binaries/resources, not a pre-authorized account. Sessions,
messages, contacts, media cache, database keys, signing keys and provisioning
profiles are not included. Application configuration is fetched over HTTPS;
each user signs in independently. Application implementation/history stays private.

Removing the **Cydia installer package** preserves the app and account data.
Deleting the **app from the Home screen** is a separate action that may erase data.
Turning off Background Notifications in Telegraphica releases its background assertion.

SHA256SUMS in the release verifies the exact downloadable artifacts. The source's
SHA256SUMS covers the APT files/page and old retained companion downloads. APT
indexes are not separately signed; use the HTTPS source without disabling TLS.
Report beta problems with build, device/iOS, steps and error text, without chat
contents, phone numbers, login codes or passwords.
