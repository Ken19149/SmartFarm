import csv
import random
import time
'''
header = ["id", "temperature", "humidity", "time"]
file = open("test.csv", mode="w", newline="")
writer = csv.writer(file)
writer.writerow(header)
'''

#append to csv

'''
for x in range(0, 100):
    with open("test.csv", mode="a", newline="") as sensor_file:
        writer = csv.writer(sensor_file)
        now = time.localtime()
        time_format = str(str(now[0]) + "/" + str(now[1]) + "/" + str(now[2]) + " - " + str(now[3]) + ":" + str(now[4]) + ":" + str(now[5]))
        writer.writerow([x,random.randint(-10,10),random.randint(40,85),time_format])
print(now)
'''

# new algo: open -> append -> close