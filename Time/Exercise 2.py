import time

hour = time.strftime("%H")
print(hour)

# Greeting example
hour_int = int(hour)
if hour_int < 12:
    print("Good Morning")
elif hour_int in range(12, 17):
    print("Good Afternoon")
elif hour_int in range(17, 19):
    print("Good Evening")
else:
    print("Good Night")

