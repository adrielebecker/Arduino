from machine import Pin
from time import sleep
 
ledG = Pin(16, Pin.OUT)
ledR = Pin(5, Pin.OUT)
 
while True:
    ledG.value(not ledG.value())
    sleep(1.0)
    ledR.value(not ledR.value())
    sleep(1.0)

