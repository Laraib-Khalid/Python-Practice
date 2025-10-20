"""
===============================
  Python Time & Datetime Guide
===============================
This script demonstrates the complete use of:
1. time module — for timestamps, struct_time, clocks, and conversions.
2. datetime module — for date/time arithmetic, formatting, and timezone handling.

Everything is fully commented and follows the official Python documentation.

https://docs.python.org/3/library/time.html
"""



# -----------------------------------------
#               IMPORTS
# -----------------------------------------
import time            # low-level time functions
import datetime as date    # datetime module (imported as alias 'date')
import calendar
from datetime import datetime, timedelta, timezone, time as dtime, date as ddate

# -----------------------------------------
#           TIME MODULE BASICS
# -----------------------------------------
print("\n========== TIME MODULE ==========\n")

# time.time() → current time in seconds since epoch (float)
timestamp = time.time()
print("Current timestamp (seconds since epoch):", timestamp)

# time.ctime([secs]) → human-readable string
print("Human-readable local time:", time.ctime())

# time.asctime([struct_time]) → readable string from struct_time
print("asctime():", time.asctime())

# time.localtime([secs]) → convert to struct_time (local timezone)
local_time = time.localtime()
print("Local time struct:", local_time)

# time.gmtime([secs]) → convert to struct_time (UTC)
utc_time = time.gmtime()
print("UTC time struct:", utc_time)

# time.mktime(struct_time) → convert local struct_time to timestamp
print("Converted localtime to timestamp:", time.mktime(local_time))

# calendar.timegm(struct_time) → convert UTC struct_time to timestamp
print("Converted gmtime to timestamp:", calendar.timegm(utc_time))

# time.strftime(format, [t]) → format struct_time to string
formatted = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Formatted local time:", formatted)

# time.strptime(string, format) → parse string to struct_time
parsed_time = time.strptime("2025-10-16 11:30:00", "%Y-%m-%d %H:%M:%S")
print("Parsed struct_time:", parsed_time)

# time.sleep(secs) → pause execution
print("\nSleeping for 0.5 seconds...")
time.sleep(0.5)
print("Woke up!\n")



# -----------------------------------------
#          CLOCKS & MEASUREMENT
# -----------------------------------------
# Use monotonic/perf/process clocks for measuring durations (not wall time)

print("=== Clock Measurements ===")

# time.monotonic() → strictly increasing, unaffected by system clock changes
start = time.monotonic()
time.sleep(0.1)
end = time.monotonic()
print("Elapsed time (monotonic):", end - start)

# time.monotonic_ns() → integer nanoseconds version
start_ns = time.monotonic_ns()
end_ns = time.monotonic_ns()
print("Elapsed time (monotonic_ns):", end_ns - start_ns, "ns")

# time.perf_counter() → highest resolution timer for performance measurement
p_start = time.perf_counter()
time.sleep(0.1)
p_end = time.perf_counter()
print("Elapsed (perf_counter):", p_end - p_start)

# time.process_time() → CPU time consumed (ignores sleep)
pt1 = time.process_time()
for _ in range(1000000):
    pass
pt2 = time.process_time()
print("CPU time consumed:", pt2 - pt1)

# time.get_clock_info(name) → clock properties
print("\nClock info:")
print("monotonic:", time.get_clock_info("monotonic"))
print("perf_counter:", time.get_clock_info("perf_counter"))
print("time:", time.get_clock_info("time"))

# -----------------------------------------
#     TIMEZONE CONSTANTS (platform-dependent)
# -----------------------------------------
print("\n=== Timezone Constants ===")
print("time.timezone (offset in seconds):", time.timezone)
print("time.daylight (DST available?):", time.daylight)
if hasattr(time, "altzone"):
    print("time.altzone (DST offset):", time.altzone)

# -----------------------------------------
#     TIME EXTRACTION EXAMPLES
# -----------------------------------------
print("\n=== Extracting Components ===")

hour = time.strftime("%H")
minutes = time.strftime("%M")
seconds = time.strftime("%S")
day = date.datetime.now().strftime("%A")

print("Hour:", hour)
print("Minutes:", minutes)
print("Seconds:", seconds)
print("Day:", day)

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



# -----------------------------------------
#          DATETIME MODULE
# -----------------------------------------
print("\n========== DATETIME MODULE ==========\n")

# date(year, month, day)
today_date = ddate.today()
print("Today's date:", today_date)

specific_date = ddate(2025, 10, 16)
print("Specific date:", specific_date)
print("Weekday (0=Mon):", specific_date.weekday())

# time(hour, minute, second)
specific_time = dtime(11, 30, 0)
print("Specific time:", specific_time)

# datetime(year, month, day, hour, minute, second)
dt = datetime(2025, 10, 16, 11, 30, 0)
print("Specific datetime:", dt)

# datetime.now() and datetime.utcnow()
print("Local now():", datetime.now())
# print("UTC now():", datetime.utcnow())

# timezone-aware datetime
print("UTC aware now:", datetime.now(timezone.utc))

# timedelta (date/time arithmetic)
delta = timedelta(days=2, hours=3, minutes=15)
future = datetime.now() + delta
past = datetime.now() - timedelta(weeks=1)
print("Future:", future)
print("Past:", past)

# Formatting and parsing
formatted_dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted_dt)

parsed_dt = datetime.strptime("2025-10-16 11:30:00", "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_dt)

# From timestamp
ts = Time.time()
dt_from_ts = datetime.fromtimestamp(ts)
dt_from_ts_utc = datetime.fromtimestamp(ts, tz=timezone.utc)
print("From timestamp (local):", dt_from_ts)
print("From timestamp (UTC):", dt_from_ts_utc)

# To timestamp
print("Datetime to timestamp:", dt_from_ts.timestamp())

# ISO format
iso = datetime.now().isoformat()
print("ISO format:", iso)

from_iso = datetime.fromisoformat("2025-10-16T11:30:00")
print("Parsed from ISO:", from_iso)

# Timezone conversion
cet = timezone(timedelta(hours=1))  # UTC+1
dt_utc = datetime.now(timezone.utc)
converted = dt_utc.astimezone(cet)
print("UTC to CET:", converted)

# # Using zoneinfo (IANA timezone)
# dt_pk = datetime.now(ZoneInfo("Asia/Karachi"))
# print("Asia/Karachi time:", dt_pk)

# Combine date + time
combined = datetime.combine(today_date, specific_time)
print("Combined date & time:", combined)

# Replace parts of datetime
replaced = dt.replace(hour=0, minute=0, second=0, microsecond=0)
print("Replaced to midnight:", replaced)

# Convert to struct_time
print("Datetime as timetuple:", dt.timetuple())

# Arithmetic difference (elapsed seconds)
start_dt = datetime.now()
time.sleep(0.3)
end_dt = datetime.now()
elapsed = (end_dt - start_dt).total_seconds()
print("Elapsed seconds (datetime):", elapsed)

# Naive vs Aware example
naive = datetime(2025, 10, 16, 11, 30, 0)
aware = datetime(2025, 10, 16, 11, 30, 0, tzinfo=timezone.utc)
print("Naive:", naive)
print("Aware:", aware)
print("Converted aware to local:", aware.astimezone())

# -----------------------------------------
# End of script
# -----------------------------------------
print("\nAll examples executed successfully ✅")

# import time
# import datetime as date
#
# timestamp = time.strftime("%H:%M:%S")
# print(timestamp)
#
# timestamp = time.strftime("%I:%M:%S %p %z %Z %j %U %w %x %X %Y")
# print(timestamp)
#
# # Get current local time as a struct_time
# local_time = time.localtime()
#
# # Convert struct_time to timestamp
# timestamp = time.mktime(local_time)
#
# print(timestamp)
#
# timestamp = time.monotonic()
# print(timestamp)
#
# timestamp = time.monotonic_ns()
# print(timestamp)
#
# timestamp = time.asctime()
# print(timestamp)
#
#
#
#
# timestamp = time.gmtime()
# print(timestamp)
#
# timestamp = time.localtime()
# print(timestamp)
#
# hour = time.strftime("%H")
# print("Hour is: ", hour)
#
# minutes = time.strftime("%M")
# print("Minutes are: ", minutes)
#
# seconds = time.strftime("%S")
# print("Seconds are: ", seconds)
#
# day = date.datetime.now().strftime("%A")
# # day = day.strftime("%A")
# print(day)
#
# hour = int(hour)
#
# if hour < 12:
#     print("Good Morning")
# elif hour in range(12,17):
#     print("Good Afternoon")
# elif hour in range(17,19):
#     print("Good Evening")
# else:
#     print("Good Night")