import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import random

amplitudeFront = numpy.pi/4
frequencyFront = 10
phaseOffsetFront = 0

numberOfGenerations = 100
populationSize = 50

motorJointRange = .2