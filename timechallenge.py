import pytz
import datetime

menu = []

for i in range(9):
    menu.append(pytz.all_timezones[i])
print("please choose a timezone: ")
for i in menu:
    print("\t{}. {} Timezone".format(menu.index(i) + 1, i))

choice = int(input("please choose a timezone: ")) - 1
print("Times in the {} timezone are as follows: \n local time is {} \n UTC time is {} ".format(menu[choice], datetime.datetime.now(tz = pytz.timezone(menu[choice])), datetime.datetime.utcnow()))
