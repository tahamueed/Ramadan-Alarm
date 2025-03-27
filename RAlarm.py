import datetime
import time
from pygame import mixer
import threading
import os

# Initialize pygame mixer
mixer.init()

# Default city coordinates (for fallback)
PAKISTAN_CITIES = {
    "Abbottabad": (34.1469, 73.2145),
    "Ahmadpur": (29.3956, 71.6836),
    "Arifwala": (30.2906, 73.0657),
    "Astore": (35.3667, 74.8500),
    "Attock": (33.7660, 72.3598),
    "Badin": (24.6560, 68.8370),
    "Baffa": (34.4378, 73.2234),
    "Bagh": (33.9811, 73.7761),
    "Bahawalnagar": (29.9984, 73.2527),
    "Bahawalpur": (29.3956, 71.6836),
    "Balakot": (34.5488, 73.3536),
    "Bannu": (32.9861, 70.6040),
    "Batgram": (34.6796, 73.0263),
    "Bhakkar": (31.6269, 71.0647),
    "Burewala": (30.1576, 72.6502),
    "Chakwal": (32.9329, 72.8631),
    "Chaman": (30.9177, 66.4520),
    "Charsadda": (34.1482, 71.7406),
    "Chilas": (35.4208, 74.0940),
    "Chiniot": (31.7200, 72.9784),
    "Chishtian": (29.7971, 72.8577),
    "Chitral": (35.8511, 71.7864),
    "Dadu": (26.7303, 67.7769),
    "Dargai": (34.5110, 71.9012),
    "Daska": (32.3243, 74.3497),
    "Dera Ghazi Khan": (30.0561, 70.6348),
    "Dera Ismail Khan": (31.8313, 70.9017),
    "Diamer": (35.4167, 73.7833),
    "Dina": (33.0287, 73.6012),
    "Drosh": (35.5578, 71.7948),
    "Faisalabad": (31.4180, 73.0790),
    "Gilgit": (35.9200, 74.3087),
    "Gojra": (31.1493, 72.6832),
    "Gujranwala": (32.1877, 74.1945),
    "Gujrat": (32.5731, 74.0754),
    "Gwadar": (25.1216, 62.3254),
    "Hafizabad": (32.0709, 73.6880),
    "Hajira": (33.7718, 73.8890),
    "Hangu": (33.5318, 71.0595),
    "Haripur": (33.9946, 72.9341),
    "Hasilpur": (29.6922, 72.5457),
    "Hunza": (36.3167, 74.6500),
    "Hyderabad": (25.3960, 68.3578),
    "Islamabad": (33.6844, 73.0479),
    "Jacobabad": (28.2819, 68.4376),
    "Jamshoro": (25.4283, 68.2806),
    "Jhang": (31.2698, 72.3161),
    "Jhelum": (32.9345, 73.7310),
    "Kalat": (29.0266, 66.5936),
    "Kamoke": (31.9753, 74.2230),
    "Karachi": (24.8607, 67.0011),
    "Kasur": (31.1187, 74.4490),
    "Khairpur": (27.5295, 68.7617),
    "Khanewal": (30.3017, 71.9321),
    "Khushab": (32.2967, 72.3525),
    "Khuzdar": (27.8119, 66.6100),
    "Kohat": (33.5820, 71.4493),
    "Kotli": (33.5184, 73.9022),
    "Lahore": (31.5497, 74.3436),
    "Larkana": (27.5580, 68.2140),
    "Layyah": (30.9613, 70.9390),
    "Lodhran": (29.5399, 71.6324),
    "Loralai": (30.3705, 68.5980),
    "Malakand": (34.5656, 71.9304),
    "Mandi Bahauddin": (32.5870, 73.4973),
    "Mansehra": (34.3302, 73.1968),
    "Mardan": (34.1980, 72.0458),
    "Mastung": (29.7997, 66.8455),
    "Matiari": (25.5961, 68.4467),
    "Mianwali": (32.5777, 71.5285),
    "Mingora": (34.7717, 72.3602),
    "Mirpur": (33.1483, 73.7519),
    "Mirpur Khas": (25.5276, 69.0125),
    "Multan": (30.1575, 71.5249),
    "Muridke": (31.8025, 74.2577),
    "Muzaffarabad": (34.3700, 73.4711),
    "Muzaffargarh": (30.0726, 71.1933),
    "Narowal": (32.1020, 74.8730),
    "Naushahro Feroze": (26.8401, 68.1226),
    "Nawabshah": (26.2483, 68.4038),
    "Nowshera": (34.0158, 71.9750),
    "Nushki": (29.5542, 66.0215),
    "Okara": (30.8090, 73.4458),
    "Pakpattan": (30.3431, 73.3866),
    "Panjgur": (26.9719, 64.0946),
    "Parachinar": (33.8992, 70.1001),
    "Peshawar": (34.0151, 71.5249),
    "Poonch": (33.8500, 73.7500),
    "Quetta": (30.1798, 66.9750),
    "Rahim Yar Khan": (28.4212, 70.2989),
    "Rawalakot": (33.8578, 73.7604),
    "Rawalpindi": (33.5651, 73.0169),
    "Sadiqabad": (28.3062, 70.1307),
    "Sahiwal": (30.6682, 73.1118),
    "Saidu Sharif": (34.7469, 72.3557),
    "Sanghar": (26.0469, 68.9492),
    "Sargodha": (32.0836, 72.6711),
    "Shakargarh": (32.2636, 75.1601),
    "Sheikhupura": (31.7131, 73.9783),
    "Shikarpur": (27.9571, 68.6379),
    "Sialkot": (32.4945, 74.5229),
    "Skardu": (35.2971, 75.6333),
    "Sukkur": (27.7052, 68.8574),
    "Swabi": (34.1202, 72.4698),
    "Talagang": (32.9276, 72.4159),
    "Tando Allahyar": (25.4605, 68.7175),
    "Tando Muhammad Khan": (25.1238, 68.5368),
    "Tank": (32.2171, 70.3832),
    "Taunsa Sharif": (30.7046, 70.6586),
    "Thatta": (24.7475, 67.9235),
    "Timergara": (34.8263, 71.8436),
    "Turbat": (26.0011, 63.0485),
    "Umerkot": (25.3633, 69.7418),
    "Vehari": (30.0452, 72.3489),
    "Wah Cantt": (33.8050, 72.6990),
    "Zhob": (31.3408, 69.4493),
}

# Add the complete Ramadan calendar for Bahawalpur
RAMADAN_CALENDAR = {
    1:  {"date": "02-03-2025", "sehri": "05:17 AM", "iftar": "06:20 PM"},
    2:  {"date": "03-03-2025", "sehri": "05:16 AM", "iftar": "06:20 PM"},
    3:  {"date": "04-03-2025", "sehri": "05:15 AM", "iftar": "06:21 PM"},
    4:  {"date": "05-03-2025", "sehri": "05:14 AM", "iftar": "06:21 PM"},
    5:  {"date": "06-03-2025", "sehri": "05:13 AM", "iftar": "06:22 PM"},
    6:  {"date": "07-03-2025", "sehri": "05:12 AM", "iftar": "06:23 PM"},
    7:  {"date": "08-03-2025", "sehri": "05:11 AM", "iftar": "06:23 PM"},
    8:  {"date": "09-03-2025", "sehri": "05:10 AM", "iftar": "06:24 PM"},
    9:  {"date": "10-03-2025", "sehri": "05:08 AM", "iftar": "06:25 PM"},
    10: {"date": "11-03-2025", "sehri": "05:07 AM", "iftar": "06:26 PM"},
    11: {"date": "12-03-2025", "sehri": "05:06 AM", "iftar": "06:26 PM"},
    12: {"date": "13-03-2025", "sehri": "05:05 AM", "iftar": "06:27 PM"},
    13: {"date": "14-03-2025", "sehri": "05:04 AM", "iftar": "06:28 PM"},
    14: {"date": "15-03-2025", "sehri": "05:02 AM", "iftar": "06:28 PM"},
    15: {"date": "16-03-2025", "sehri": "05:01 AM", "iftar": "06:29 PM"},
    16: {"date": "17-03-2025", "sehri": "05:00 AM", "iftar": "06:29 PM"},
    17: {"date": "18-03-2025", "sehri": "04:58 AM", "iftar": "06:30 PM"},
    18: {"date": "19-03-2025", "sehri": "04:56 AM", "iftar": "06:30 PM"},
    19: {"date": "20-03-2025", "sehri": "04:54 AM", "iftar": "06:31 PM"},
    20: {"date": "21-03-2025", "sehri": "04:53 AM", "iftar": "06:31 PM"},
    21: {"date": "22-03-2025", "sehri": "04:52 AM", "iftar": "06:32 PM"},
    22: {"date": "23-03-2025", "sehri": "04:51 AM", "iftar": "06:33 PM"},
    23: {"date": "24-03-2025", "sehri": "04:50 AM", "iftar": "06:33 PM"},
    24: {"date": "25-03-2025", "sehri": "04:48 AM", "iftar": "06:33 PM"},
    25: {"date": "26-03-2025", "sehri": "04:47 AM", "iftar": "06:34 PM"},
    26: {"date": "27-03-2025", "sehri": "04:46 AM", "iftar": "06:34 PM"},
    27: {"date": "28-03-2025", "sehri": "04:45 AM", "iftar": "06:35 PM"},
    28: {"date": "29-03-2025", "sehri": "04:44 AM", "iftar": "06:35 PM"},
    29: {"date": "30-03-2025", "sehri": "04:43 AM", "iftar": "06:36 PM"},
    30: {"date": "31-03-2025", "sehri": "04:41 AM", "iftar": "06:37 PM"}
}

def calculate_time_adjustment(base_lon, target_lon, base_time):
    """Calculate time adjustment based on longitude difference"""
    time_diff_minutes = int((target_lon - base_lon) * 4)  # 4 minutes per degree
    base_dt = datetime.datetime.strptime(base_time, "%I:%M %p")
    adjusted_dt = base_dt + datetime.timedelta(minutes=time_diff_minutes)
    return adjusted_dt.strftime("%I:%M %p")

def get_adjusted_prayer_times(city, roza):
    """Get adjusted prayer times for a city based on the Ramadan calendar"""
    base_lon = PAKISTAN_CITIES["Bahawalpur"][1]
    target_lon = PAKISTAN_CITIES[city][1]
    
    base_times = RAMADAN_CALENDAR[roza]
    sehri = calculate_time_adjustment(base_lon, target_lon, base_times["sehri"])
    iftar = calculate_time_adjustment(base_lon, target_lon, base_times["iftar"])
    
    return {"sehri": sehri, "iftar": iftar, "date": base_times["date"]}

def display_current_time(city, roza):
    """Display current time and countdown"""
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M:%S %p")
        current_date = now.strftime("%d-%m-%Y")
        times = get_adjusted_prayer_times(city, roza)
        
        sehri_dt = datetime.datetime.strptime(f"{current_date} {times['sehri']}", "%d-%m-%Y %I:%M %p")
        iftar_dt = datetime.datetime.strptime(f"{current_date} {times['iftar']}", "%d-%m-%Y %I:%M %p")
        
        if now < sehri_dt:
            time_diff = sehri_dt - now
            print(f"\r⏰ {current_time} | 📅 {current_date} | 🌅 Sehri in: {str(time_diff).split('.')[0]} | 📍 {city}", end="", flush=True)
        elif now < iftar_dt:
            time_diff = iftar_dt - now
            print(f"\r⏰ {current_time} | 📅 {current_date} | 🌙 Iftar in: {str(time_diff).split('.')[0]} | 📍 {city}", end="", flush=True)
        else:
            print(f"\r⏰ {current_time} | 📅 {current_date} | 📍 {city}", end="", flush=True)
        
        time.sleep(1)

def play_alarm(alarm_type):
    """Play alarm sound"""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sound_file = os.path.join(current_dir, f"{alarm_type}_alarm.mp3")
        
        if os.path.exists(sound_file):
            mixer.music.load(sound_file)
            mixer.music.play()
            time.sleep(30)
            mixer.music.stop()
        else:
            print(f"\n⚠️ Warning: Sound file not found: {sound_file}")
    except Exception as e:
        print(f"\n❌ Error playing {alarm_type} alarm: {e}")

def check_alarm_times(city, roza):
    """Check and trigger alarms"""
    last_triggered = {"sehri": None, "iftar": None}
    
    while True:
        now = datetime.datetime.now()
        current_date = now.strftime("%d-%m-%Y")
        current_minute = now.strftime("%H:%M")
        
        times = get_adjusted_prayer_times(city, roza)
        sehri_time = datetime.datetime.strptime(times['sehri'], "%I:%M %p").strftime("%H:%M")
        iftar_time = datetime.datetime.strptime(times['iftar'], "%I:%M %p").strftime("%H:%M")
        
        # Check alarms with a 1-minute window
        if current_minute == sehri_time and last_triggered["sehri"] != current_date:
            print(f"\n🌅 SEHRI TIME! ({city}) - {now.strftime('%I:%M %p')}")
            play_alarm("sehri")
            last_triggered["sehri"] = current_date
        
        if current_minute == iftar_time and last_triggered["iftar"] != current_date:
            print(f"\n🌙 IFTAR TIME! ({city}) - {now.strftime('%I:%M %p')}")
            play_alarm("iftar")
            last_triggered["iftar"] = current_date
        
        time.sleep(30)

def start_ramadan_system():
    try:
        city = input("Enter city (" + ", ".join(PAKISTAN_CITIES.keys()) + "): ")
        if city not in PAKISTAN_CITIES:
            print("City not found, using Bahawalpur")
            city = "Bahawalpur"
        
        roza_count = int(input("Enter the current Roza number (1-30): "))
        if not 1 <= roza_count <= 30:
            print("Please enter a valid Roza number between 1 and 30")
            return start_ramadan_system()

        print("\n🌙 Ramadan Sehri & Iftar Times:")
        print("-------------------------")
        
        # Get today's times
        today_times = get_adjusted_prayer_times(city, roza_count)
        print(f"Today (Roza {roza_count}): {today_times['date']}")
        print(f"🌅 Sehri: {today_times['sehri']}")
        print(f"🌙 Iftar: {today_times['iftar']}")
        
        # Start time display thread
        time_thread = threading.Thread(target=display_current_time, args=(city, roza_count), daemon=True)
        time_thread.start()
        
        # Start alarm thread
        alarm_thread = threading.Thread(target=check_alarm_times, args=(city, roza_count), daemon=True)
        alarm_thread.start()

        print("\n")  # Space for time display
        
        # Keep main thread running
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n🔔 Alarm system stopped.")
    except ValueError as e:
        print(f"Error: {e}")
        print("Please try again with valid inputs")
        return start_ramadan_system()

if __name__ == "__main__":
    print("🌙 Ramadan Alarm System")
    print("-------------------")
    print("The system will alert you at Sehri and Iftar times.")
    print("Press Ctrl+C to stop the alarm system.\n")
    start_ramadan_system()

