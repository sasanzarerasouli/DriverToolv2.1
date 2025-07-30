# DriverTool v2.1

A lightweight GUI utility for backing up and installing Windows drivers. Designed for PAYAMED users, with a focus on clarity, reliability, and user comfort.

## Features

- Export installed drivers using the built-in DISM tool
- Install `.INF` and `.COM` driver files from a selected folder
- Scrollable file selection dialog with multi-check support
- Live log output panel for real-time feedback
- Packaged in onefile mode, using `resource_path` for compatibility

## Requirements

- Python 3.9 or higher
- PyQt6
- Must be run as Administrator on Windows
- 
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

The birth of this application comes with a story—and in the following section, I’ll be sharing that story with you.

# Story
This tool was born out of a real-world challenge faced by my close friend and colleague, Farzad. He was on a tight schedule, tasked with replacing a software on a medical imaging system. To install the new software, he had to reinstall Windows — but that meant all existing drivers would be wiped. We didn’t have backups of those drivers, and downloading them manually from autodriver platforms was out of the question due to time constraints and limited internet access.

To solve this, I built a minimal Tkinter-based utility (v1.0) with just two buttons: Export and Install. It allowed Farzad to back up all installed drivers before wiping Windows. He used it successfully on-site and recorded the process via mobile for reference — especially since the app had to be run with Run as Administrator via right-click.

However, a problem surfaced: after restoring the ELO touchscreen drivers, the calibration software couldn’t be installed. Windows Installer threw errors, saying an older version was already present. I remotely accessed the system to clean the registry and driver directories, but this made me rethink the workflow.

Enter Version 2.1 — Redesigned and Enhanced
I rebuilt the entire utility in PyQt6, creating a more intuitive and visually polished interface. Major improvements included:

- Scrollable driver selection before install — choose exactly which drivers to restore
- Automatic elevation — no need for right-clicking “Run as Admin”
- Modern UI/UX — sleek layout, branding elements, emoji touch, and version display
- One-click simplicity — just hit the green button, and the app takes care of the rest

As Farzad puts it: "You just click the green button and you're done!" 😁

This wasn’t just a tool — it became a reliable solution for quick, offline driver backup and restore in time-sensitive environments. Whether you're upgrading Windows, reimaging a system, or working in medical or industrial setups, it saves time, hassle, and potential downtime.


