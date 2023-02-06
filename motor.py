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

        for e in range(0, 1000):
            #self.values.append(self.amplitude * numpy.sin(e* .8 * self.frequency * (numpy.pi / 2) + self.offset) * (numpy.pi/4))
            self.values.append(numpy.sin(e*.1))

    def Set_Value(self, desiredAngle, robot):
        desiredAngle = pyrosim.Set_Motor_For_Joint(
                bodyIndex = robot,
                jointName = self.jointName,
                controlMode = p.POSITION_CONTROL,
                targetPosition = desiredAngle,
                maxForce = 100)
