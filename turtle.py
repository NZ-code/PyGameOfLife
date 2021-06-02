from animal import Animal
import random
class Turtle(Animal):
    def __init__(self, x,y,world):
        Animal.__init__(self,2,1,x,y,1,world)
    def draw(self):
        return (90, 227, 147)
    def get_name(self):
        return "Turtle"
    def defend(self, org):
        if org.get_power() < 5:
            return -1
        else:
            return 0
    def action(self):
        if random.randint(0,100) > 75:
            Animal.action(self)
    def get_copy(self,x,y):
        return Turtle(x,y,self.world)
