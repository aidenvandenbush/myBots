import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")


p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

frontLegSensorValues = numpy.zeros(1000)
backLegSensorValues = numpy.zeros(1000)

frontValues = []
amplitudeFront = numpy.pi/4
frequencyFront = 10
phaseOffsetFront = 0

backValues = []
amplitudeBack = numpy.pi/4
frequencyBack = 10
phaseOffsetBack = numpy.pi/4

for e in range(0, 1000):
    frontValues.append(amplitudeFront * numpy.sin(e* .36 * frequencyFront * (numpy.pi / 180) + phaseOffsetFront) * (numpy.pi/4))

for e in range(0, 1000):
    backValues.append(amplitudeBack * numpy.sin(e* .36 * frequencyBack * (numpy.pi / 180) + phaseOffsetBack) * (numpy.pi/4))

for i in range(1000):
    p.stepSimulation()

    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = backValues[i],
        maxForce = 25)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = frontValues[i],
        maxForce = 25)


    time.sleep(1/100)

numpy.save("frontLegSensorValues.npy", frontLegSensorValues)
numpy.save("backLegSensorValues.npy", backLegSensorValues)
numpy.save("frontValues", frontValues)
numpy.save("backValues", backValues)

p.disconnect()

#print(frontLegSensorValues)
#print(backLegSensorValues)
