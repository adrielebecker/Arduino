from machine import Pin
from time import sleep
from stepper import Stepper

stepsPerRevolution = 2048  # altere isso para ajustar o número de passos por revolução

# Pinos do Driver do Motor ULN2003
IN1 = 5
IN2 = 4
IN3 = 14
IN4 = 12

# Inicializa o motor de passo
stepper = Stepper(stepsPerRevolution, Pin(IN1), Pin(IN3), Pin(IN2), Pin(IN4))

def setup():
    # Configura a velocidade e aceleração
    stepper.max_speed(500)
    stepper.acceleration(100)
    # Define a posição alvo
    stepper.move_to(stepsPerRevolution)

def loop():
    # Verifica a posição atual do motor de passo para inverter a direção
    if stepper.distance_to_go() == 0:
        stepper.move_to(-stepper.position())
        print("Changing direction")
    # Move o motor de passo (um passo de cada vez)
    stepper.run()

setup()

while True:
    loop()

