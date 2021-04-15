import sys
print(sys.version)

seconds = ((42 * 60) + 42)
miles = (10/1.61)
hour = (seconds/3600)
minutes = (seconds/60)
average_speed = (miles/hour)
time_per_mile_minutes = (int(minutes / miles))
time_pro_mile_seconds = (int(((minutes/miles) - time_per_mile_minutes) * 60))
print("1. How many seconds are there in 42 minutes 42 seconds? Answer:", seconds, "seconds")
print("2. How many miles are there in 10 kilometers? Answer:", "%.2f" % miles, "miles")
print("3. What is your average speed in miles per hour? Answer:", "%.2f" % average_speed, "MPH")
print("4. What is your average pace? Answer:", time_per_mile_minutes, "minutes", time_pro_mile_seconds, "seconds")


