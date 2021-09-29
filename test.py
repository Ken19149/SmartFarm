import time
from machine import Pin, PWM

pump = PWM(Pin(0))
pump.freq(900)
time1 = time.ticks_ms()

while True:
    delta_time1 = time.ticks_diff(time.ticks_ms(), time1)
    print("delta time1 = ",delta_time1,"ms")
    
    if delta_time1<= 5000:
        pump.duty(255) #25%
        print("Pump ON")
        
    else :
        pump.duty(0) 
        print("Pump OFF")
        break
    
print("I'm out")