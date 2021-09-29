import time
from machine import Pin, PWM

pump = PWM(Pin(0))
D0 = Pin(16)

#pump.freq(900)

duration = 2 #seconds
limit = 50 #power limit

#Duty input and limits

while True:
    percent = input("DEVICE POWER (percent%): ")
    try:
        x = int((float(percent)/100)*1023)
        if x >=500: #duty not more than 500
            x = 500
        print("power:",x)
        if int(percent) >= limit: #power reach limits -> light on
            D0.on()
        else:
            D0.off()
        
#-------------- Improve From Slide----------------------------------------------------
        
        time1 = time.ticks_ms()
        while True:
            delta_time1 = time.ticks_diff(time.ticks_ms(), time1)
            print("delta time1 = ",delta_time1,"ms")
            
            if delta_time1 <= (duration*1000*2):
                pump.duty(x)
                print("Pump ON")

            else :
                pump.duty(0) 
                print("Pump OFF")
                Pin(16).off()
                break
    
            print("I'm out")
            
    except:
        continue
'''
while True:
    delta_time1 = time.ticks_diff(time.ticks_ms(), time1)
    print("delta time1 = ",delta_time1,"ms")
    
    if delta_time1<= 2000:
        pump.duty(x) #25%
        print("Pump ON")
        
    else :
        pump.duty(0) 
        print("Pump OFF")
        break
    
print("I'm out")
'''