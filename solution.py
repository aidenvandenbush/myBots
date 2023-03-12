import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):

        self.myID = nextAvailableID
        self.numberOfLinks = random.randint(4, 6)

        self.randomNumbers = []
        for i in range(1000):
            self.randomNumbers.append(random.random())

        self.d = []
        for i in range(self.numberOfLinks):
            self.d.append(random.randint(1, 4))
        
        self.numberMotorNeurons = self.numberOfLinks
        
        self.sensorList = [1]
        self.numberSensorNeurons = 1
        for i in range(self.numberOfLinks):
            x = random.randint(0, 1)
            self.sensorList.append(x)
            if x == 1:
                self.numberSensorNeurons += 1 


        self.jointNameList = []
        self.weights = numpy.random.rand(self.numberSensorNeurons, self.numberMotorNeurons) * 2 - 1

    def Start_Simulation(self, mode):
        if self.myID == 0:
            self.Create_World()
        self.Create_Body()
        self.Create_Block()
        self.Create_Brain()
        os.system("start /B python simulate.py " + mode + " " + str(self.myID))
    
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(1)

        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()

        os.system("del fitness" + str(self.myID) + ".txt")


    def Mutate(self):
        if (self.myID >= 6250):
            self.weights[random.randint(0, self.numberSensorNeurons-1)][random.randint(0, self.numberMotorNeurons-1)] = random.random() * 2 - 1
        else:
            linkIndex = random.randint(0, self.numberOfLinks-1)
            multiplier = linkIndex * 25 + 3
            side = random.randint(1, 4)
            self.d[linkIndex] = side

            self.randomNumbers[multiplier + side*5] = random.random()
            self.randomNumbers[multiplier + side*5 + 1] = random.random()
            self.randomNumbers[multiplier + side*5 + 2] = random.random()
            self.randomNumbers[multiplier + side*5 + 3] = random.random()
            self.randomNumbers[multiplier + side*5 + 4] = random.random()

    def Set_ID(self, newID):
        self.myID = newID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.End()

    def Create_Block(self):
        pyrosim.Start_URDF("block" + str(self.myID) + ".urdf")

        colorString = '    <color rgba="1.0 1.0 1.0 1.0"/>'
        pyrosim.Send_Cube(colorString, name="block", pos=[1.25, 0, .25], size=[.5, .5, .5])

        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")

        xDim = self.randomNumbers[0] + .25
        yDim = self.randomNumbers[1] + .25
        zDim = self.randomNumbers[2] + .25

        if self.sensorList[0] == 1:
            colorString = '    <color rgba="0 1.0 0 1.0"/>'
        else:
            colorString = '    <color rgba="0 0 1.0 1.0"/>'

        pyrosim.Send_Cube(colorString,name=str(0), pos=[0,0,zDim/2] , size=[xDim,yDim,zDim])

        randNumCount = 3
        for i in range(self.numberOfLinks):
            # create joint at random point on parent cube
            jointName = str(0) + "_" + str(i+1)
            self.jointNameList.append(jointName)

            if self.sensorList[i+1] == 1:
                colorString = '    <color rgba="0 1.0 0 1.0"/>'
            else:
                colorString = '    <color rgba="0 0 1.0 1.0"/>'
        
            if self.d[i] == 0:
                pos = [xDim/2, self.randomNumbers[randNumCount]*yDim - yDim/2, self.randomNumbers[randNumCount+1]*zDim]
                pyrosim.Send_Joint( name = jointName , parent= str(0) , child = str(i+1) , type = "revolute", position = pos, jointAxis = "0 1 1")

                x = self.randomNumbers[randNumCount+2]
                y = self.randomNumbers[randNumCount+3] * .5
                z = self.randomNumbers[randNumCount+4] * .5

                pyrosim.Send_Cube(colorString,name=str(i+1), pos=[x/2,0,z/2] , size=[x,y,z])

            elif self.d[i] == 1:
                pos = [-xDim/2, self.randomNumbers[randNumCount+5]*yDim - yDim/2, self.randomNumbers[randNumCount+6]*zDim]
                pyrosim.Send_Joint( name = jointName , parent= str(0) , child = str(i+1) , type = "revolute", position = pos, jointAxis = "0 1 1")

                x = self.randomNumbers[randNumCount+7] + 1
                y = self.randomNumbers[randNumCount+8] * .5
                z = self.randomNumbers[randNumCount+9] * .5

                pyrosim.Send_Cube(colorString,name=str(i+1), pos=[-x/2,0,z/2] , size=[x,y,z])
                
            elif self.d[i] == 2:
                pos = [self.randomNumbers[randNumCount+10]*xDim - xDim/2, yDim/2, self.randomNumbers[randNumCount+11]*zDim]
                pyrosim.Send_Joint( name = jointName , parent= str(0) , child = str(i+1) , type = "revolute", position = pos, jointAxis = "1 0 1")

                x = self.randomNumbers[randNumCount+12] * .5
                y = self.randomNumbers[randNumCount+13] + 1
                z = self.randomNumbers[randNumCount+14] * .5

                pyrosim.Send_Cube(colorString,name=str(i+1), pos=[0,y/2,z/2] , size=[x,y,z])
            elif self.d[i] == 3:
                pos = [self.randomNumbers[randNumCount+15]*xDim - xDim/2, -yDim/2, self.randomNumbers[randNumCount+16]*zDim]
                pyrosim.Send_Joint( name = jointName , parent= str(0) , child = str(i+1) , type = "revolute", position = pos, jointAxis = "1 0 1")

                x = self.randomNumbers[randNumCount+17] * .5
                y = self.randomNumbers[randNumCount+18] + 1
                z = self.randomNumbers[randNumCount+19] * .5

                pyrosim.Send_Cube(colorString,name=str(i+1), pos=[0,-y/2,z/2] , size=[x,y,z])
            elif self.d[i] == 4:
                pos = [self.randomNumbers[randNumCount+20]*xDim - xDim/2, self.randomNumbers[randNumCount+21]*yDim - yDim/2, zDim]
                pyrosim.Send_Joint( name = jointName , parent= str(0) , child = str(i+1) , type = "revolute", position = pos, jointAxis = "1 1 0")
                
                x = self.randomNumbers[randNumCount+22] * .5
                y = self.randomNumbers[randNumCount+23] * .5
                z = self.randomNumbers[randNumCount+24]

                pyrosim.Send_Cube(colorString,name=str(i+1), pos=[0,0,z/2] , size=[x,y,z])
            randNumCount += 25

        pyrosim.End()
    


    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        nameNumber = 0
        
        for i in range(self.numberOfLinks+1):
            if self.sensorList[i] == 1:
                pyrosim.Send_Sensor_Neuron(name = nameNumber , linkName = str(i))   
                nameNumber += 1

        for i in range(self.numberOfLinks):
            pyrosim.Send_Motor_Neuron(name = nameNumber , jointName = self.jointNameList[i])
            nameNumber += 1

        for currentRow in range(self.numberSensorNeurons):
            for currentColumn in range(self.numberMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.numberSensorNeurons , weight = self.weights[currentRow][currentColumn])
    
        pyrosim.End()