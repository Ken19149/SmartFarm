from machine import Pin,PWM
import time

#16 5 4 0 2

pwm_D1 = PWM(Pin(5))

for x in range(0,512):
    time.sleep(0.01)
    pwm_D0.duty(x)

Pin(16).on()
