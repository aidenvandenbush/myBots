from world import WORLD
from robot import ROBOT

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import random
import constants as c

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        self.solutionID = solutionID
        
        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        
        

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        
        self.world = WORLD()
        self.robot = ROBOT(self.solutionID)

        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_to_Act()


    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def Run(self):

        for i in range(1000):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
 
            if self.directOrGUI == "GUI":
                time.sleep(1/99999999)
            