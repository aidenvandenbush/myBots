import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import random

amplitudeFront = numpy.pi/4
frequencyFront = 10
phaseOffsetFront = 0

numberOfGenerations = 10
populationSize = 5

numSensorNeurons = 5
numMotorNeurons = 4

motorJointRange = .5