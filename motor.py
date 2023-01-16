import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import random
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        
        self.amplitude = c.amplitudeFront
        self.frequency = c.frequencyFront
        self.offset = c.phaseOffsetFront

        self.values = []

        if jointName == "Torso_BackLeg":
            self.frequency = 5

        for e in range(0, 1000):
            self.values.append(self.amplitude * numpy.sin(e* .36 * self.frequency * (numpy.pi / 180) + self.offset) * (numpy.pi/4))

    def Set_Value(self, i, robot):
        self.values[i] = pyrosim.Set_Motor_For_Joint(
                bodyIndex = robot,
                jointName = self.jointName,
                controlMode = p.POSITION_CONTROL,
                targetPosition = self.values[i],
                maxForce = 50)

    def Save_Values(self):
        numpy.save("MotorValues", self.values)