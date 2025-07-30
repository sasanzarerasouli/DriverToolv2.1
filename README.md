# DriverTool v2.1

A lightweight GUI utility for backing up and installing Windows drivers. Designed for PAYAMED users, with a focus on clarity, reliability, and user comfort.

## Features

- Export installed drivers using the built-in DISM tool
- Install `.INF` and `.COM` driver files from a selected folder
- Scrollable file selection dialog with multi-check support
- Live log output panel for real-time feedback
- Packaged in onefile mode, using `resource_path` for compatibility

## Requirements

- Python 3.3 or higher
- PyQt6
- Must be run as Administrator on Windows
- VScode
  
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

The birth of this application comes with a story—and in the following section, I’ll be sharing that story with you.

# Story
I have a dear friend and close colleague named Farzad, who was tasked with a challenging mission: updating the software on a medical imaging device. To install the new software, Farzad had to reinstall Windows, which meant wiping out all the existing drivers. Unfortunately, we didn’t have the drivers for that system readily available, and there wasn’t enough time to download them using auto-driver tools. Farzad couldn’t afford to stay at the medical center for long, so I decided to create a solution to make his job easier.

The goal was to develop a tool that could back up the existing drivers before the Windows reinstall and restore them afterward. I started with a simple application (let’s call it Version 1.0) built using the tkinter library. It had just two buttons: one for exporting drivers and another for installing them. I copied this version onto Farzad’s USB drive. He recorded a video on his phone showing how to run the program by right-clicking the icon and selecting "Run as Administrator" to export and install the drivers.

The next day, Farzad used the tool, and it worked like a charm—his task was completed successfully! However, we hit a snag. The system used Elo touch monitors, and after restoring the drivers (specifically the .inf files), we couldn’t install the touch screen calibration software. Windows threw an error, claiming a version was already installed. I remotely connected to the system that same day and manually removed the touch drivers from the registry and Windows directories, but the issue stuck with me. I knew we needed a better solution.

This led to the development of Version 2.1. I enhanced the driver installation process to allow selective installation, enabling users to exclude unnecessary drivers from the list before proceeding. For this version, I wanted a more polished, user-friendly, and visually appealing interface, so I switched to PyQt6 for the UI. I poured my creativity and ingenuity into making this version as intuitive as possible. One key improvement? The app now runs as administrator by default—no more right-clicking and selecting "Run as Administrator." Just double-click, and you’re good to go! 

As Farzad puts it, “Just hit the green button, and the job’s done!” 😁😁

This tool was born out of necessity and teamwork, and I’m excited to share it with the community. Contributions and feedback are welcome!

