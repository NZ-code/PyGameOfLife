from plant import Plant
import random
class Grass(Plant):
    def __init__(self, x,y,world):
        Plant.__init__(self,0,x,y,world)
    def draw(self):
        return (42, 54, 4)
    def get_name(self):
        return "Grass"
    def get_copy(self,x,y):
        return Grass(x,y,self.world)
    
    
