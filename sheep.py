from animal import Animal
import random
class Sheep(Animal):
    def __init__(self, x,y,world):
        Animal.__init__(self,4,4,x,y,1,world)
    def draw(self):
        return (239, 228, 220)
    def get_name(self):
        return "Sheep"
    def get_copy(self,x,y):
        return Sheep(x,y,self.world)
