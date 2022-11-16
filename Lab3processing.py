import lightFunctions as j
import matplotlib.pyplot as pyplot
import matplotlib.ticker as ticker
lumaR = j.readIntensity("W red.jpg", "Wred_processed.jpg", "Лампа накаливания", "красный лист")
lumaB = j.readIntensity("W blue 3.jpg", "Wblue_processed.jpg", "Лампа накаливания", "синий лист")
lumaG = j.readIntensity("W green.jpg", "Wgreen_processed.jpg", "Лампа накаливания", "зелёный лист")
lumaY = j.readIntensity("W yellow.jpg", "Wyellow_processed.jpg", "Лампа накаливания", "жёлтый лист")
lumaW = j.readIntensity("W white.jpg", "Wwhite_processed.jpg", "Лампа накаливания", "белый лист")

xs = [i for i in range(750, 750-len(lumaG)*2, -2)]
lumaR = [i / 40 for i in lumaR]
lumaG = [i / 40 for i in lumaG]
lumaB = [i / 40 for i in lumaB]
lumaW = [i / 40 for i in lumaW]
lumaY = [i / 40 for i in lumaY]
figure, ax = pyplot.subplots()
ax.plot(xs, lumaG, color='g')
pyplot.plot(xs, lumaR, color="r")
pyplot.plot(xs, lumaB, color="b")
pyplot.plot(xs, lumaW, color="w")
pyplot.plot(xs, lumaY, color="y")
ax.set_title("Альбедо поверхностей", fontsize=22, fontname='serif')
ax.set_xlabel("Длина волны, нм", fontsize=14, fontname='DejaVu Sans')
ax.set_ylabel("Альбедо", fontsize=14, fontname='DejaVu Sans')
ax.set_facecolor("#d6d6d6")
ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))

ax.minorticks_on()
ax.grid(which='major')
ax.grid(which='minor', linestyle=':')
pyplot.show()
