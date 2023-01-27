from simulation import SIMULATION
import sys

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import random
import constants as c

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()