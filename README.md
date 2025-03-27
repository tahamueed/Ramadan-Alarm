# Ramadan Sehri & Iftar Alarm System
Overview
A Python-based desktop app to alert users for Sehri and Iftar during Ramadan. Fetches prayer times via Aladhan API, plays custom audio alarms, sends notifications, and features a Ramadan-themed Tkinter GUI.

Features
Real-time Sehri/Iftar times for Pakistani cities (e.g., Karachi, Lahore).
Customizable MP3/WAV alarms for Sehri and Iftar.
Desktop notifications at prayer times.
Modern GUI with countdown, prayer time display, and status indicator.
Confirmation pop-up when alarm is set.
Installation
Clone the repo:
git clone https://github.com/[your-username]/ramadan-alarm-system.git
cd ramadan-alarm-system
Install dependencies:
pip install pygame requests plyer
Ensure Tkinter is installed (Linux: sudo apt-get install python3-tk).
Add sound files (sehri_alarm.mp3, iftar_alarm.mp3) to the directory.
Usage
Run the app:
python ramadan_alarm_system.py
Select a city, set custom sounds, and click "Start Alarm".
View prayer times, countdown, and status. Alarms ring with notifications at Sehri/Iftar.
Requirements
Python 3.8+
Internet connection
Troubleshooting
No Sound: Check sound files or reselect via GUI.
No Notifications: Verify plyer installation.
API Errors: Ensure internet connectivity.
