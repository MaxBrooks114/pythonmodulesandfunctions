# import time
#
# print(time.gmtime(0))
# time_here = time.localtime()
# print("year:", time_here.tm_year)
# print("Month:", time_here.tm_mon)
# print("Day:", time_here.tm_mday)
import time
# from time import process_time as my_timer
# import random
#
# input("press enter to start:")
#
# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# start_time = my_timer()
# input("press enter to stop")
#
# end_time = my_timer()
#
# print("started at " + time.strftime("%X", time.localtime(start_time)))
# print("Ended at " + time.strftime("%X", time.localtime(end_time)))
#
# print("Your reaction time was {} seconds".format(end_time - start_time))


print(time.get_clock_info("time"))
print(time.get_clock_info("perf_counter"))
print(time.get_clock_info("monotonic"))
print(time.get_clock_info("process_time"))


