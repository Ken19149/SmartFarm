from machine import Pin
import time
import dht

#16 5 4 0 2

D0 = dht.DHT11(Pin(16)) #SENSOR
D1 = Pin(5,Pin.OUT)     #LED
D2 = Pin(4,Pin.OUT)     #LED
D3 = Pin(0,Pin.OUT)     #FAN
D4 = Pin(2,Pin.OUT)     #PUMP

D0.on()
D1.on()

'''
delay = 0.5

D0.on()
D1.off()

time.sleep(delay)

while True:
    D0.off()
    D1.on()
    time.sleep(delay)
    D0.on()
    D1.off()
    time.sleep(delay)
'''
