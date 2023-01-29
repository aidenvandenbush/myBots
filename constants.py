import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import random

amplitudeFront = numpy.pi/4
frequencyFront = 15
phaseOffsetFront = 0

amplitudeBack = numpy.pi/4
frequencyBack = 10
phaseOffsetBack = numpy.pi/4

numberOfGenerations = 15
populationSize = 7

numSensorNeurons = 9
numMotorNeurons = 8

motorJointRange = .2