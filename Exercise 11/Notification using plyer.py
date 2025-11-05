# Install dependency
# pip install plyer

from plyer import notification
import time

while True:
    notification.notify(
        title="💧 Water Reminder",
        message="Drink a glass of water to stay fresh & healthy!🌿",
        timeout=10
    )

    # Wait 1 hour (change to 7200 for 2 hours)
    time.sleep(5)



# import winsound
# from plyer import notification
# import time
#
# while True:
#     # Play beep sound (frequency, duration in ms)
#     winsound.Beep(2000, 1000)
#
#     notification.notify(
#         title="💧 Water Time!",
#         message="Drink water now!",
#         timeout=10
#     )
#
#     time.sleep(3500)
