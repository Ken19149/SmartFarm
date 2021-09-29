from machine import Pin,PWM
import time

#16 5 4 0 2

D0 = Pin(16)
pwm_D1 = PWM(Pin(5))

pin = input("select pin: ")
pin = int(pin)
pin = PWM(Pin(pin))

limit = 50 #power limit

while True:
    percent = input("DEVICE POWER (percent%): ")
    try:
        if float(percent) >= limit:
            percent = limit
        x = int((float(percent)/100)*1023)
        pin.duty(x)
        print("power:",x)
        if int(percent) >= limit: #power reach limits -> light on
            D0.on()
        else:
            D0.off()
    except:
        continue