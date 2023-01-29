from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")

        self.parent = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parent[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        

    def Evolve(self):
        self.Evaluate(self.parent)
        
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children) 
        self.Print()
        self.Select()
        
    def Show_Best(self):
        self.parent[len(self.parent) - 1].Start_Simulation("GUI")
        
    def Spawn(self):
        self.children = {}

        for i in range(len(self.parent)):
            self.children[i] = copy.deepcopy(self.parent[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1     

    def Mutate(self):
        for i in range(len(self.children)):
            self.children[i].Mutate()

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
        
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()

    def Select(self):
        for i in range(len(self.parent)):
            if self.parent[i].fitness > self.children[i].fitness:
                self.parent[i] = self.children[i]

    def Print(self):
        """
        print("\n")
        
        for i in range(len(self.parent)):
            print(self.parent[i].fitness, self.children[i].fitness)
        
        print("\n")
        """
