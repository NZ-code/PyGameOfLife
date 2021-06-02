from plant import Plant
import random
class Belladonna(Plant):
    def __init__(self, x,y,world):
        Plant.__init__(self,99,x,y,world)
    def draw(self):
        return (255, 0, 168)
    def get_name(self):
        return "Belladonna"
    def get_copy(self,x,y):
        return Belladonna(x,y,self.world)
    
