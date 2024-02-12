# https://docs.python.org/3/library/datetime.html

from datetime import datetime, date, timedelta

s1 = "2021-04-01 08:30:00"
dt1 = datetime.fromisoformat(s1)
print(dt1.month, dt1.day, dt1.hour)
print(dt1.date(), dt1.time())
print(datetime.min < dt1) #用datetime.min代替None

print(f"今天{date.today()}, 星期{date.today().isoweekday()}")

# 获取当前日期和时间
current_datetime = datetime.now()
# 计算30天前的日期和时间
thirty_days_ago = current_datetime - timedelta(days=30)
print("当前日期和时间:", current_datetime)
print("30天前的日期和时间:", thirty_days_ago)