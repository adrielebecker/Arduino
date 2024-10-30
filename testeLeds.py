#Piscar os leds intercaladamente
from machine import Pin
import time
# Pela numera鑾借尗o do GPIO:
led1 = Pin(5, Pin.OUT) #d1
led2 = Pin(4, Pin.OUT) #d2

while True:
    # Pisca os LEDs de forma intercalada a cada 1 segundo
    led1.on()
    led2.off();
    time.sleep(1)
    led2.on()
    led1.off()
    time.sleep(1)



