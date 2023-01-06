import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")


x = 0

for j in range(5):

    y = 0

    for k in range(5):
        
        length = 1
        width = 1
        height = 1

        z = 0.5

        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

            z = z + 1

            length = length * .9
            width = width * .9
            height = height * .9

        y = y + 1
    x = x + 1


pyrosim.End()
