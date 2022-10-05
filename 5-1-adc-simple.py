import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def decimalToBinary(number):
    return [int(i) for i in bin(number)[2:].zfill(8)]

def adc():
    for i in range(256):
        sleep(0.01)
        binary = decimalToBinary(i)
        GPIO.output(dac, binary)
        if GPIO.input(comp) == 0:
            GPIO.output(dac, 0)
            return i
    return 255

try:
    while True:
        num = adc()
        print(num, "Target voltage: {:.4f} volts".format(3.3 / 256.0 * num))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()