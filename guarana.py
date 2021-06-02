from plant import Plant
import random
class Guarana(Plant):
    def __init__(self, x,y,world):
        Plant.__init__(self,0,x,y,world)
    def draw(self):
        return (240, 9, 81)
    def get_name(self):
        return "Guarana"
    def defend(self,org):
        org.set_power(org.get_power() + 3)
        return 0
    def get_copy(self,x,y):
        Guarana(x,y,self.world)
        
    
    
