from machine import Pin
from time import sleep

# Atribuir a uma vari谩vel o GPIO2 como pino de sa铆da
led = Pin(2, Pin.OUT)

while True:
  # Atribuir ao led o estado contr谩rio ao seu estado atual (se ligado, desliga, e vice-versa)
  led.value(not led.value())
  # Criar um delay de meio segundo
  sleep(0.5)
