# Ramadan Sehri & Iftar Alarm System
Overview
A Python-based console application to alert users for Sehri and Iftar during Ramadan 2025. Uses a static calendar for Bahawalpur and adjusts prayer times for other Pakistani cities based on longitude differences. Plays audio alarms at the appropriate times.

Features
Supports 100+ Pakistani cities with longitude-based time adjustments.
Static Ramadan 2025 calendar for Bahawalpur (March 2–31).
Audio alarms for Sehri and Iftar (MP3 files).
Real-time countdown display in the console.
Multi-threaded for simultaneous time display and alarm checks.
Installation
Clone the repo:

git clone https://github.com/tahamueed/ramadan-alarm-system.git
cd ramadan-alarm-system
Install dependencies:

pip install pygame
Add sound files (sehri_alarm.mp3, iftar_alarm.mp3) to the project directory.
Usage
Run the app:

python ramadan_alarm_system.py
Enter your city (e.g., "Lahore") and the current Roza number (1–30).
View adjusted Sehri/Iftar times for your city.
The console displays a countdown; alarms play at the specified times.
Requirements
Python 3.8+
Sound files (sehri_alarm.mp3, iftar_alarm.mp3)
Troubleshooting
No Sound: Ensure sound files are in the directory and are valid MP3s.
Invalid Input: Enter a valid city and Roza number (1–30).
Limitations
Uses a static calendar for Bahawalpur; times are approximate for other cities.
No GUI; console-based only.
License
MIT License. See  file.
