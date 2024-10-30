from machine import ADC, Pin, PWM
import time

potenciometro = ADC(Pin(16))
potenciometro.atten(ADC.ATTN_11DB)
potenciometro.width(ADC.WIDTH_12BIT)

LED = PWM(Pin(22), 100)
LED.duty(50)

while True:
 leitura = potenciometro.read()
 leitura = leitura * 3.3 / 4095
 duty = int(leitura * 1023 // 3.3)
 LED.duty(duty)
 time.sleep(0.1)
