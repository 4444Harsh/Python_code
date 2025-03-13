import datetime

today = datetime.date.today()

print("EVENT COUNTDOWN")
day = int(input("Event Day: "))
month = int(input("Event Month: "))
year = int(input("Event Year: "))
event = datetime.date(year, month, day)

difference = event - today
difference = difference.days

if difference>0:
  print(f"{difference} days to go")
elif difference<0:
  print(f"😭😭😭😭😭😭😭 You missed it by {difference} days!")
  
else:
  print("🥳🥳🥳🥳🥳🥳🥳 Today!")
