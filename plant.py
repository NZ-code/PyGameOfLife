import random
from organism import Organism
class Plant(Organism):
    def __init__(self,power,x,y,world):
        Organism.__init__(self,power,0,x,y,world)
    def draw(self):
        return (255,0,0)
    def get_name(self):
        return "Grass"
    def action(self):
        if random.randint(0,100) > 97:
            cnt = 0
            TRY = 100
            min_x = max(self._x - 1, 0)
            max_x = min(self._x + 1, self.world.get_width()-1)
            min_y = max(self._y - 1, 0) 
            max_y = min(self._y + 1, self.world.get_height()-1)
            while cnt < TRY:
                cnt = cnt + 1
                x_n = random.randint(min_x, max_x)
                y_n = random.randint(min_y, max_y)
                if not(x_n == self._x and y_n == self._y) and self.world.is_empty(x_n,y_n):
                    self.get_copy(x_n,y_n)
                    return
    def get_organism(self,x,y):
        return self.world.get_field(x,y)
    def collision(self, x, y):
        pass
    def attack(self,org):
        pass
    def defend(self,org):
        if(self._power >= org._power):
            return 1
        else:
            return 0
    def check_field(self,x,y):
        return self.world.is_empty(x,y)
    def get_coordinates_neighbour(self):
        index = -1
        for i in range(max(self._x - 1, 0),min(self._x + 1, self.world.get_width())):
            for j in range(max(self._y - 1, 0),min(self._y + 1, self.world.get_height())):
                if not(i == self._x and j == self._y) and self.world.is_empty(i,j):
                    return (i,j)
        if index == -1:
            return (max(self._x-1,0),max(self._y-1,0))
