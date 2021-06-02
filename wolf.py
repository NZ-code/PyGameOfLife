from animal import Animal
import random
class Wolf(Animal):
    def __init__(self, x,y,world):
        Animal.__init__(self,9,5,x,y,1,world)
    def draw(self):
        return (100, 100, 100)
    def get_name(self):
        return "Wolf"
    def get_copy(self,x,y):
        return Wolf(x,y,self.world)
