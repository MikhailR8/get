import numpy as np
import matplotlib.pyplot as pyplot
import matplotlib.ticker as ticker

#Чтение из файлов
with open("settings.txt") as settings:
    params = np.array([float(i) for i in settings.read().split('\n')])

with open("data.txt") as data:
    ys = np.array([float(i) for i in data.read().split('\n')])

#Обработка массивов и создание массивов маркеров
xs = np.linspace(0, 1/params[0] * len(ys), len(ys))
ys = ys * params[1]
MarkersX, MarkersY = [], []

#Нахождение максимальной точки и расчёт времени заряда-разряда
dotMax = ys.max()
timestamp = ys.argmax()
timeC = 1/params[0] * timestamp
timeD = 1/params[0] * (len(ys) - timestamp)

#Частота маркеров
for i in range(len(xs)):
    if i % 256 == 0:
        MarkersX.append(xs[i])
        MarkersY.append(ys[i])

fig, ax = pyplot.subplots(figsize=(14,7))

#Настройка осей
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))

#Настройка сетки
ax.minorticks_on()
ax.grid(which='major')
ax.grid(which='minor', linestyle=':')

#Вывод времени
ax.text(48, 2, "Time Charging = {:.4f} secs".format(timeC), fontsize=14)
ax.text(48, 1.5, "Time Discharging = {:.4f} secs".format(timeD), fontsize=14)

#Установка пределов по осям
ax.set_xlim([-5, xs.max() + 5])
ax.set_ylim([-0.5, ys.max() + 0.5])

#Построение осей и маркеров
ax.plot(xs, ys, linewidth=2, color='#4169E1', label='V(t)')
ax.scatter(MarkersX, MarkersY, s=35, color='#4B0082', zorder=10)

#Настройка надписей
ax.set_title("Process of charging-discharging capasitor in RC-circuit", fontsize=22, fontname='serif')
ax.set_xlabel("Time, secs", fontsize=14, fontname='DejaVu Sans')
ax.set_ylabel("Voltage on capacitor, volts", fontsize=14, fontname='DejaVu Sans')

#Настрйока легенды
ax.legend(fontsize=10)

#Сохранение картинки
pyplot.savefig("graph.svg")

pyplot.show()
