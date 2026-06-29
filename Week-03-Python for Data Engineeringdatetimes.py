# Prctice 1 - Current UTC Time

"""from datetime import datetime, timezone

utc_time = datetime.now(timezone.utc)

print(utc_time)"""

# Practice 2 - Current Local Time

"""from datetime import datetime

local_time = datetime.now()

print(local_time)"""


# Understanding the Difference
# UTC Time
#     ↓
# 2026-06-15 15:30

# India (IST)
#     ↓
# 2026-06-15 21:00

# India is:

# UTC + 5:30

# Practice 3 - Create IST Timezone

"""from datetime import datetime, timezone, timedelta

IST = timezone(timedelta(hours=5, minutes=30))

ist_time = datetime.now(IST)

print(ist_time)"""

#Mini Task - Login Timestamp Generator

"""from  datetime import datetime, timezone

user = input("Enter Username: ")

login_time = datetime.now(timezone.utc)

print("User: ", user)
print("Login Time: ", login_time)"""
