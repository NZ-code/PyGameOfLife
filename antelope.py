from animal import Animal
import random
class Antelope(Animal):
    def __init__(self, x,y,world):
        Animal.__init__(self,4,4,x,y,2,world)
    def draw(self):
        return (231, 167, 40)
    def get_name(self):
        return "Antelope"
    def defend(self,org):
        if random.randint(0,1) == 0 :
            if self.get_power() >= org.get_power():
                return 1
            else:
                return 0
        else:
            x_k,y_k = self.get_coordinates_neighbour()
            self.world.move_to(self,x_k, y_k)
            return -1
    def get_copy(self,x,y):
        return Antelope(x,y,self.world)
