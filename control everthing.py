import time
import dht
import machine
from machine import Pin

#16 5 4 0 2

D0 = dht.DHT11(Pin(16)) #SENSOR
D1 = Pin(5,Pin.OUT)     #LED
D2 = Pin(4,Pin.OUT)     #LED
D3 = Pin(0,Pin.OUT)     #FAN
D4 = Pin(2,Pin.OUT)     #PUMP

standard_humidity = 75

while True:
    D0.measure()
    
    temperature = D0.temperature()
    humidity = D0.humidity()
    
    print(temperature,"°C", str(humidity) + "% RH")
    
    if humidity >= standard_humidity:
        D3.on()
        D1.on()
        D2.on()
    else:
        D3.off()
        D1.off()
        D2.off()
    time.sleep(1)