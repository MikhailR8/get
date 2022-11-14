import lightFunctions as j
import matplotlib.pyplot as pyplot 
lumaR = j.readIntensity("W red.jpg", "Wred_processed.jpg", "Лампа накаливания", "красный лист")
lumaB = j.readIntensity("W blue 3.jpg", "Wblue_processed.jpg", "Лампа накаливания", "синий лист")
lumaG = j.readIntensity("W green.jpg", "Wgreen_processed.jpg", "Лампа накаливания", "зелёный лист")
lumaY = j.readIntensity("W yellow.jpg", "Wyellow_processed.jpg", "Лампа накаливания", "жёлтый лист")
lumaW = j.readIntensity("W white.jpg", "Wwhite_processed.jpg", "Лампа накаливания", "белый лист")

xs = [i for i in range(800, 800-len(lumaG)*2, -2)]
figure, ax = pyplot.subplots()
ax.plot(xs, lumaG, color='g')
pyplot.plot(xs, lumaR, color="r")
pyplot.plot(xs, lumaB, color="b")
pyplot.plot(xs, lumaW, color="w")
pyplot.plot(xs, lumaY, color="y")

pyplot.show()
