from plant import Plant
import random
class Sonchus(Plant):
    def __init__(self, x,y,world):
        Plant.__init__(self,0,x,y,world)
    def draw(self):
        return (255, 255, 255)
    def get_name(self):
        return "Sonchus"
    def action(self):
        for i in range(0,3):
            Plant.action(self)
    def get_copy(self,x,y):
        return Sonchus(x,y,self.world)
    
    
