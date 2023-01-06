import pyrosim.pyrosim as pyrosim


def Create_World():
    pyrosim.Start_SDF("world.sdf")

    x = -3
    y = 3
    z = 0.5
        
    length = 1
    width = 1
    height = 1

    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Link0", pos=[0,0,0.5] , size=[1,1,1])
    
    pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0.5,0,1])

    pyrosim.Send_Cube(name="Link1", pos=[0.5,0,0.5] , size=[1,1,1])

    pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [1,0,0])

    pyrosim.Send_Cube(name="Link2", pos=[0.5,0,-0.5] , size=[1,1,1])

    pyrosim.End()

Create_World()
Create_Robot()