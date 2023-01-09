import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")


p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

frontLegSensorValues = numpy.zeros(1000)
backLegSensorValues = numpy.zeros(1000)

for i in range(1000):
    p.stepSimulation()

    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    time.sleep(1/100)

numpy.save("frontLegSensorValues.npy", frontLegSensorValues)
numpy.save("backLegSensorValues.npy", backLegSensorValues)

p.disconnect()

print(frontLegSensorValues)
print(backLegSensorValues)
