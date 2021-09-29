from machine import RTC, Pin
import time

import ntptime
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

def do_connect(user, password):
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(user, password)
        while not wlan.isconnected():
            pass
        print('network config:', wlan.ifconfig())

#do_connect("wifi_ssid_2.4G", "TCP > UDP") #this is fake username and password
do_connect('kenboy_2.4G', 'kwin1234')

rtc = RTC()
ntptime.settime() # set the RTC's time using ntptime

print(rtc.datetime())
time_offset = 7
gmt = rtc.datetime()
gmt = list(gmt) #Tuple -> list
gmt[4] += time_offset
rtc.datetime(tuple(gmt)) # Set time and convert list -> tuple

print(rtc.datetime())

fan = Pin(0, Pin.OUT)

while True:
    current_time = rtc.datetime()
    hour = current_time[4]
    minute = current_time[5]
    
    if hour == 11 and minute == 19:
        fan.on()
        print("ON")
    elif hour == 11 and minute == 20:
        fan.off()
        print("OFF")
    time.sleep(1)