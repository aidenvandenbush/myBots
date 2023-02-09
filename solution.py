import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = 0
        self.myID = nextAvailableID
        self.numberOfLinks = 0
        self.numberSensorNeurons = 0
        self.numberMotorNeurons = 0
        self.sensorList = []

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
        self.weights[random.randint(0, self.numberSensorNeurons-1)][random.randint(0, self.numberMotorNeurons-1)] = random.random() * 2 - 1

    def Set_ID(self, newID):
        self.myID = newID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        self.numberOfLinks = random.randint(3,10)

        for i in range(self.numberOfLinks+1):
            self.sensorList.append(random.randint(0, 1))

        xDim = random.random()/2 + .5
        yDim = random.random()/2 + .5
        zDim = random.random()/2 + .5

        if self.sensorList[0] == 1:
            colorString = '    <color rgba="0 1.0 0 1.0"/>'
        else:
            colorString = '    <color rgba="0 0 1.0 1.0"/>'

        pyrosim.Send_Cube(colorString,name=str(0), pos=[-1*self.numberOfLinks/2,0,zDim/2] , size=[xDim,yDim,zDim])

        for i in range(self.numberOfLinks):

            jointName = str(i) + "_" + str(i+1)

            if i == 0:
                pyrosim.Send_Joint( name = jointName , parent= str(i) , child = str(i+1) , type = "revolute", position = [-1*self.numberOfLinks/2+xDim/2,0,zDim/2], jointAxis = "0 1 1")
            else:
                pyrosim.Send_Joint( name = jointName , parent= str(i) , child = str(i+1) , type = "revolute", position = [xDim,0,0], jointAxis = "0 1 1")
            
            xDim = random.random()/2 + .5
            yDim = random.random()/2 + .5
            zDim = random.random()/2 + .5

            if self.sensorList[i+1] == 1:
                colorString = '    <color rgba="0 1.0 0 1.0"/>'
            else:
                colorString = '    <color rgba="0 0 1.0 1.0"/>'

            pyrosim.Send_Cube(colorString,name=str(i+1), pos=[xDim/2,0,0] , size=[xDim,yDim,zDim])

        pyrosim.End()
    


    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        nameNumber = 0
        
        for i in range(self.numberOfLinks+1):
            if self.sensorList[i] == 1:
                pyrosim.Send_Sensor_Neuron(name = nameNumber , linkName = str(i))  
                self.numberSensorNeurons += 1  
                nameNumber += 1

        for i in range(self.numberOfLinks):
            jointName = str(i) + "_" + str(i+1)
            pyrosim.Send_Motor_Neuron(name = nameNumber , jointName = jointName)

            self.numberMotorNeurons += 1
            nameNumber += 1

        self.weights = numpy.random.rand(self.numberSensorNeurons, self.numberMotorNeurons) * 2 - 1

        for currentRow in range(self.numberSensorNeurons):
            for currentColumn in range(self.numberMotorNeurons):
                #pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.numberSensorNeurons , weight = self.weights[currentRow][currentColumn])
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.numberSensorNeurons , weight = 1)
    
        pyrosim.End()