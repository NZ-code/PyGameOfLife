from animal import Animal
import random
class Fox(Animal):
    def __init__(self, x,y,world):
        Animal.__init__(self,3,7,x,y,1,world)
    def draw(self):
        return (231, 85, 40)
    def get_name(self):
        return "Fox"
    def collision(self,x,y):
        org = self.world.get_field(x,y)
        print("istance",isinstance(org,Animal))
        if self.draw() == org.draw():
            print("REPRODUCT")
        else:
            if org.get_power() > self.get_power():
                print("FOX ESCAPE FROM FIGHT")
            else:
                Animal.fight(self,x,y)
    def get_copy(self,x,y):
        return Fox(x,y,self.world)
