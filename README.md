# Windows 10 Battery Monitor

Windows 10 Battery Monitor is a simple and effective tool designed to keep you informed about your laptop's battery status. This script provides notifications on your battery's charge level, alerting you every hour about the battery status and also when the battery is fully charged.

## Features

- **Hourly Battery Status Updates:** Receive a notification every 60 minutes with the current status of your battery.
- **Full Charge Alert:** Get notified as soon as your battery reaches 100% charge to prevent overcharging.
- **Lightweight and Easy to Use:** Runs in the background without any complex setup.

## Installation

To install the Windows 10 Battery Monitor, follow these simple steps:

1. **Download the Executable:**
   - Navigate to the `dist` folder in this repository.
   - Download the `BatteryMonitor.exe` file.

2. **Add to Startup:**
   - Press `Win + R` to open the Run dialog.
   - Type `shell:startup` and press Enter. This opens the Startup folder.
   - Copy the downloaded `BatteryMonitor.exe` file into this Startup folder.

3. **Restart Your System:**
   - Restart your computer to start running Windows 10 Battery Monitor automatically.

## Usage

Once installed, the Windows 10 Battery Monitor will:

- Check your battery status every 5 minutes.
- Display a notification for 10 seconds every 60 minutes, showing the current battery level.
- Immediately display a "Battery Fully Charged" notification for 10 seconds when the battery reaches 100%.

The tool runs in the background, so you can continue with your work without any interruption.

## Contributing

Contributions to Windows 10 Battery Monitor are welcome. Feel free to fork the repository and submit pull requests.

## License

[MIT License](LICENSE)
