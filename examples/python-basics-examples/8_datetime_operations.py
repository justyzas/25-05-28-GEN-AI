# 📅 Python Date and Time Operations
# This script demonstrates how to work with dates and times in Python using the datetime module.

from datetime import datetime, date, time, timedelta

# ----------------------------------------
# 🕒 Getting Current Date and Time
# ----------------------------------------

# 1️⃣ Get current date and time
now = datetime.now()
print(now)  # e.g., 2025-06-02 14:30:00.123456

# 2️⃣ Get only current date
# today = date.today()
today = datetime.today()
print(today)  # e.g., 2025-06-02

# 3️⃣ Get only current time
current_time = datetime.now().time()
print(current_time)  # e.g., 14:30:00.123456

# ----------------------------------------
# 📆 Creating Specific Dates and Times
# ----------------------------------------

# 4️⃣ Create a specific date
birthday = date(1990, 5, 17)
print(birthday)

# 5️⃣ Create a specific time
lunch_time = time(12, 30)
print(lunch_time)

# 6️⃣ Create a full datetime
meeting = datetime(2025, 6, 15, 9, 0)
print(meeting)

# ----------------------------------------
# 🔄 Date Arithmetic
# ----------------------------------------

# 7️⃣ Add or subtract time
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print(tomorrow)
print(yesterday)

# 8️⃣ Difference between dates
delta = tomorrow - today
print(delta.days)  # 1

# ----------------------------------------
# ⏱ Formatting and Parsing
# ----------------------------------------

# Common format codes:

# %Y - year (e.g., 2025)
# %m - month (01 to 12)
# %d - day (01 to 31)
# %H - hour (00 to 23)
# %M - minute (00 to 59)
# %S - second (00 to 59)


# 9️⃣ Format datetime as string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # e.g., "2025-06-02 14:30:00"

# 🔟 Parse string to datetime
date_str = "2025-06-02 14:30:00"
parsed = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parsed)

# ----------------------------------------
# 🧪 Type Checking and Extraction
# ----------------------------------------

# 🔍 Type checking
print(type(now))        # <class 'datetime.datetime'>
print(type(today))      # <class 'datetime.date'>
