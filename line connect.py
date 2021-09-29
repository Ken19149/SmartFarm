import network
import machine
import time
import urequests
import dht
from machine import Pin

user = "kenboy_2.4G"
password = "kwin1234"

D0 = dht.DHT11(Pin(16)) #SENSOR
D1 = Pin(5,Pin.OUT)     #RIGHT LED - BLUE
D2 = Pin(4,Pin.OUT)     #LEFT  LED - RED
D3 = Pin(0,Pin.OUT)     #FAN
D4 = Pin(2,Pin.OUT)     #PUMP

# Config for line notify
url = 'https://notify-api.line.me/api/notify'
token = 'XlmIAjMKTh165yKO1oaLFgQ7bstxKT6YdUArev2l1f2'
payload = 'message='
headers = {
    'Authorization': 'Bearer {}'.format(token),
    'Content-Type': 'application/x-www-form-urlencoded'
}

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

def do_connect():
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(user, password)
        while not wlan.isconnected():
            pass
        print('network config:', wlan.ifconfig())

while True:
    do_connect()
    D0.measure()
    msg = "Temperature : {},Humidity : {}".format(D0.temperature(),D0.humidity())
    response = urequests.request(
        "POST", url, headers=headers, data=payload+msg)
    D1.off()
    D2.on()
    time.sleep(0.3)
    D1.on()
    D2.off()
    time.sleep(3)