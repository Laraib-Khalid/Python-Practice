# Install library first
# pip install win10toast

from win10toast import ToastNotifier
import time

# Create notifier object
notifier = ToastNotifier()

while True:
    # Show notification
    notifier.show_toast(
        "💧 Water Reminder",
        "Time to drink water! Stay hydrated 🌿",
        duration=10  # Notification stays for 10 seconds
    )

    # Wait for 1 hour (3600 sec)
    time.sleep(3600)
