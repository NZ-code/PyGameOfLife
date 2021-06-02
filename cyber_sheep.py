from animal import Animal
import random
class Cyber_Sheep(Animal):
    def __init__(self, x,y,world):
        Animal.__init__(self,4,4,x,y,1,world)
    def draw(self):
        return (5, 8, 255)
    def get_name(self):
        return "Cyber Sheep"
    def get_copy(self,x,y):
        return Cyber_Sheep(x,y,self.world)
        
