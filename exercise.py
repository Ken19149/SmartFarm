import time
import dht
import machine
from machine import Pin, RTC

#16 5 4 0 2

D0 = dht.DHT11(Pin(16)) #SENSOR
D1 = Pin(5,Pin.OUT)     #RIGHT LED - BLUE
D2 = Pin(4,Pin.OUT)     #LEFT  LED - RED
D3 = Pin(0,Pin.OUT)     #FAN
D4 = Pin(2,Pin.OUT)     #PUMP

delay = 5

def light(delay):
    D2.on()
    time.sleep(delay)
    D2.off()
    D1.on()
    time.sleep(delay)
    D2.on()
    time.sleep(delay)
    D1.off()
    D2.off()
    time.sleep(delay)

rtc = RTC()
print("waiting...")
while True:
    current_time = rtc.datetime()
    hour = current_time[4]
    minute = current_time[5]
    
    if hour == 12 and minute == 2:
        light(5)
    time.sleep(1)