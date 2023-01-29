import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.myID = nextAvailableID

    def Evaluate(self, mode):
        pass

    def Start_Simulation(self, mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py " + mode + " " + str(self.myID))
    
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.05)

        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()

        os.system("del fitness" + str(self.myID) + ".txt")


    def Mutate(self):
        self.weights[random.randint(0, c.numSensorNeurons-1)][random.randint(0, c.numMotorNeurons-1)] = random.random() * 2 - 1
        """
        self.weights[random.randint(0, c.numSensorNeurons-1)][random.randint(0, c.numMotorNeurons-1)] = random.random() * 2 - 1
        self.weights[random.randint(0, c.numSensorNeurons-1)][random.randint(0, c.numMotorNeurons-1)] = random.random() * 2 - 1
        self.weights[random.randint(0, c.numSensorNeurons-1)][random.randint(0, c.numMotorNeurons-1)] = random.random() * 2 - 1
        self.weights[random.randint(0, c.numSensorNeurons-1)][random.randint(0, c.numMotorNeurons-1)] = random.random() * 2 - 1
        """

    def Set_ID(self, newID):
        self.myID = newID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,1,1])

        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[.2,1,.2])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-.5,0] , size=[.2,1,.2])
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[.5,0,0] , size=[1,.2,.2])
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [-.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[-.5,0,0] , size=[1,.2,.2])

        pyrosim.Send_Joint( name = "FrontLeg_FrontLower" , parent= "FrontLeg" , child = "FrontLower" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLower", pos=[0,0,-.5] , size=[.2,.2,1])

        pyrosim.Send_Joint( name = "BackLeg_BackLower" , parent= "BackLeg" , child = "BackLower" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLower", pos=[0,0,-.5] , size=[.2,.2,1])

        pyrosim.Send_Joint( name = "LeftLeg_LeftLower" , parent= "LeftLeg" , child = "LeftLower" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLower", pos=[0,0,-.5] , size=[.2,.2,1])

        pyrosim.Send_Joint( name = "RightLeg_RightLower" , parent= "RightLeg" , child = "RightLower" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLower", pos=[0,0,-.5] , size=[.2,.2,1])

        pyrosim.End()
    
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")    
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")

        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLower")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLower")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLower")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLower")

        pyrosim.Send_Motor_Neuron(name = 9 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 10 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 11 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name = 12 , jointName = "Torso_RightLeg")

        pyrosim.Send_Motor_Neuron(name = 13 , jointName = "BackLeg_BackLower")
        pyrosim.Send_Motor_Neuron(name = 14 , jointName = "FrontLeg_FrontLower")
        pyrosim.Send_Motor_Neuron(name = 15 , jointName = "LeftLeg_LeftLower")
        pyrosim.Send_Motor_Neuron(name = 16 , jointName = "RightLeg_RightLower")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + 9 , weight = self.weights[currentRow][currentColumn])
    
        pyrosim.End()