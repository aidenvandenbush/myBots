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

        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[2,.2,.2])

        pyrosim.Send_Joint( name = "Torso_FrontLeft" , parent= "Torso" , child = "FrontLeft" , type = "revolute", position = [-.5,-.1,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLeft", pos=[0,-.1,-.5] , size=[.2,.2,1])

        pyrosim.Send_Joint( name = "Torso_BackLeft" , parent= "Torso" , child = "BackLeft" , type = "revolute", position = [.5,-.1,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeft", pos=[0,-.1,-.5] , size=[.2,.2,1])

        pyrosim.Send_Joint( name = "Torso_FrontRight" , parent= "Torso" , child = "FrontRight" , type = "revolute", position = [-.5,.1,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontRight", pos=[0,.1,-.5] , size=[.2,.2,1])
        
        pyrosim.Send_Joint( name = "Torso_BackRight" , parent= "Torso" , child = "BackRight" , type = "revolute", position = [.5,.1,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackRight", pos=[0,.1,-.5] , size=[.2,.2,1])

        pyrosim.End()
    
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")    
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeft")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeft")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "BackRight")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "FrontRight")

        pyrosim.Send_Motor_Neuron(name = 5 , jointName = "Torso_FrontLeft")
        pyrosim.Send_Motor_Neuron(name = 6 , jointName = "Torso_BackLeft")
        pyrosim.Send_Motor_Neuron(name = 7 , jointName = "Torso_FrontRight")
        pyrosim.Send_Motor_Neuron(name = 8 , jointName = "Torso_BackRight")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + 5 , weight = self.weights[currentRow][currentColumn])
    
        pyrosim.End()