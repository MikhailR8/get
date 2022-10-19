import RPi.GPIO as GPIO
import matplotlib.pyplot as pyplot
import time

#Создание переменный
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
troyka = 17
comp = 4

#Настройка выводов
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

#Функция, которая считывает напряжение на компараторе
def adc():
    num = [0] * 8
    for i in range(8):
        num[i] = 1
        GPIO.output(dac, num)
        time.sleep(0.001)
        comparatorValue = GPIO.input(comp) 
        if comparatorValue == 0:
            num[i] = 0
    return num
        
#Функция, которая выводит число на блок leds
def out_leds(num):
    GPIO.output(leds, num)

try:

    values = []

    start_charge = time.time()
    GPIO.output(troyka, 1)
    #Пока конденсатор заряжается
    while True:
        value = adc()
        out_leds(value)
        value = [str(i) for i in value]
        value = int(''.join(value), 2)
        values.append(value)
        print(value)
        if value > 235:
            break
    #Когда конденсатор разряжается
    GPIO.output(troyka, 0)
    stop_charge = time.time()
    while True:
        value = adc()
        out_leds(value)
        value = [str(i) for i in value]
        value = int(''.join(value), 2)
        values.append(value)
        print(value)
        if value < 8:
            break
    
    #Подсчёт времени
    stop_discgarge = time.time()
    during_charge = stop_charge - start_charge
    during_discharge = stop_discgarge - stop_charge
    full_time = during_charge + during_discharge

    #Построение графика
    pyplot.plot(values)
    pyplot.show()

    #Вывод времени
    print("Time Charging: {:.4f} secs".format(during_charge), "\n", "Time Discharging: {:.4f}".format(during_discharge), 
    "\n", "Full time: {:.4f}".format(full_time))
    
    #Запись в файл
    with open("data.txt", "w") as data:
        data.write("\n".join([str(i) for i in values]))
    with open("settings.txt", "w") as settings:
        settings.write("{:.4f}".format(1 / (full_time / len(values))))
        settings.write("\n")
        settings.write("{:.4f}".format(3.3 / 256))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
