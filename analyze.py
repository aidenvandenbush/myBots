import numpy
import matplotlib.pyplot

frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")

matplotlib.pyplot.plot(frontLegSensorValues, label="front leg", linewidth=3)
matplotlib.pyplot.plot(backLegSensorValues, label="back leg", linewidth=1)

matplotlib.pyplot.legend()
matplotlib.pyplot.show()