from plant import Plant
from cyber_sheep import Cyber_Sheep
import random
class Sosnowsky_Hogweed(Plant):
    def __init__(self, x,y,world):
        Plant.__init__(self,10,x,y,world)
    def draw(self):
        return (190, 252, 184)
    def get_name(self):
        return "Sosnowsky_Hogweed"
    def defend(self, org):
        if isinstance(org,Cyber_Sheep)==True:
            return 0
        elif self.get_power() > org.get_power():
            return 1
        else:
            return 0
    def action(self):
        for i in range(max(self._x - 1, 0),min(self._x + 1, self.world.get_width())):
            for j in range(max(self._y - 1, 0),min(self._y + 1, self.world.get_height())):
                if not(i == self._x and j == self._y) and not self.world.is_empty(i,j):
                    org = self.world.get_field(i,j)
                    if isinstance(org,Plant) or isinstance(org,Cyber_Sheep):
                        break
                    else:
                        self.world.remove_organism(org)
        Plant.action(self)
    def get_copy(self,x,y):
        return Sosnowsky_Hogweed(x,y,self.world)            
    
    
