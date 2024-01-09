from win10toast import ToastNotifier
import psutil
import time

def batteryStatus():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    toaster = ToastNotifier()

    # Show notification if battery is fully charged
    if plugged and percent >= 99:
        toaster.show_toast(
            "Battery Fully Charged",
            f"Battery is fully charged at {percent}%. Please unplug the charger!",
            icon_path="icon.ico",
            duration=10,
            threaded=True
        )
        return 3600  # Wait for 1 hour before next check

    # For regular battery status update
    if time.time() - batteryStatus.last_check >= 3600:
        status = "Plugged in" if plugged else "Unplugged"
        toaster.show_toast(
            "Battery Status",
            f"Battery status: {percent}% ({status})",
            icon_path="icon.ico",
            duration=10,
            threaded=True
        )
        batteryStatus.last_check = time.time()

    return 300  # Wait for 5 minutes before next check C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp


batteryStatus.last_check = time.time() - 3600  # Initialize last check time pyinstaller --onefile --windowed BatteryMonitor.py

while True:
    wait_time = batteryStatus()
    time.sleep(wait_time)
