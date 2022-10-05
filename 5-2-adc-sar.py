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
    num = [0] * 8
    sleep(0.005)
    for i in range(8):
        num[i] = 1
        sleep(0.005)
        GPIO.output(dac, num)
        sleep(0.01)
        comparatorValue = GPIO.input(comp) 
        if comparatorValue == 0:
            num[i] = 0
    num = [str(i) for i in num]
    return ''.join(num)
        


try:
    while True:
        num = adc()
        num = int(num, 2)
        print(num, "Target voltage: {:.4f} volts".format(3.3 / 256.0 * num))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()