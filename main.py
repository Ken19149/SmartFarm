import time
import dht
import machine
from machine import Pin, RTC, PWM

import ntptime
import network

D0 = dht.DHT11(Pin(16))      #SENSOR
D1 = Pin(5,Pin.OUT)          #LED
D2 = Pin(4,Pin.OUT)          #LED
D3 = Pin(0,Pin.OUT)          #FAN
D4 = PWM(Pin(2,Pin.OUT))     #PUMP

pump_power = 50
pump_power = int(float((pump_power)/100)*1023)

D4.freq(900)
standard_humidity = 75

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

def do_connect(user, password):
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(user, password)
        while not wlan.isconnected():
            pass
        print('network config:', wlan.ifconfig())

do_connect('kenboy_2.4G', 'kwin1234')

rtc = RTC()
ntptime.settime()

time_offset = 7
gmt = rtc.datetime()
gmt = list(gmt) #Tuple -> list
gmt[4] += time_offset
rtc.datetime(tuple(gmt)) # Set time and convert list -> tuple

#Light always on

D1.on()
D2.on()

while True:
    D0.measure()
    
    temperature = D0.temperature()
    humidity = D0.humidity()
        
    if humidity >= standard_humidity:
        D3.on()
    else:
        D3.off()
    
    current_time = rtc.datetime()
    hour = current_time[4]
    minute = current_time[5]
    second = current_time[6]
    
    if hour == 12 and minute == 0 and (0 <= second <= 30):
        D4.duty(pump_power)
    else:
        D4.duty(0)
    
    #-----------Record Sensor data----------------#
    
    time.sleep(1)
    
    