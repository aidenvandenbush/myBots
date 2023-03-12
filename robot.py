from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import random
import constants as c
import os

class ROBOT:
    def __init__(self, solutionID):
        self.sensors = {}
        self.motors = {}
        self.solutionID = solutionID

        self.robotId = p.loadURDF("body" + self.solutionID + ".urdf")

        self.blockId = p.loadURDF("block" + self.solutionID + ".urdf")

        self.nn = NEURAL_NETWORK("brain" + self.solutionID + ".nndf")
        
        os.system("del brain" + self.solutionID + ".nndf")

        os.system("del block" + self.solutionID + ".urdf")

        os.system("del body" + self.solutionID + ".urdf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            
    def Sense(self, t):
        for i in range(len(self.sensors)):
            list(self.sensors.values())[i].Get_Value(t)

    def Prepare_to_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle, self.robotId)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.blockId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]

        basePositionAndOrientationBot = p.getBasePositionAndOrientation(self.robotId)
        basePositionBot = basePositionAndOrientationBot[0]
        xPositionBot = basePositionBot[0]

        
        if xPosition < xPositionBot:
            x = 0
        else:
            x = xPositionBot

        f = open("tmp" + self.solutionID + ".txt", "w")
        f.write(str(x))
        f.close()

        os.rename("tmp" + str(self.solutionID) + ".txt", "fitness" + str(self.solutionID) + ".txt")



            
            