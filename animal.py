import random
from organism import Organism
class Animal(Organism):
    def __init__(self,power,initiative,x,y,step_k,world):
        Organism.__init__(self,power,initiative,x,y,world)
        self.__step_k = step_k
    def fight(self,x,y):
        org = self.world.get_field(x,y)
        print("Attack")
        self.attack(org)
    def draw(self):
        return (255,0,0)
    def action(self):
        step = self.get_step()
        self.go_by_step(step)
    def go_by_step(self,step):
        if(step == 0):# up
            if self.check_field(self._x,self._y - self.__step_k):
                self.world.move_to(self,self._x,self._y - self.__step_k)
            else:
                print("Collision")
                self.collision(self._x,self._y - self.__step_k)
        elif(step == 1):#down
            if self.check_field(self._x,self._y + self.__step_k):
                self.world.move_to(self,self._x,self._y + self.__step_k)
            else:
                print("Collision")
                self.collision(self._x,self._y + self.__step_k)
        elif(step == 2):#left
            if self.check_field(self._x - self.__step_k,self._y):
                self.world.move_to(self,self._x - self.__step_k,self._y)
            else:
                print("Collision")
                self.collision(self._x - self.__step_k,self._y)
        else:#right
            if self.check_field(self._x + self.__step_k,self._y):
                self.world.move_to(self,self._x + self.__step_k,self._y)
            else:
                print("Collision")
                self.collision(self._x + self.__step_k,self._y)
    def get_step(self):
        step = random.randint(0,3)
        while not self.check_move(self._x, self._y, step, self.__step_k):
            step = random.randint(0,3)
        return step
    def get_organism(self,x,y):
        return self.world.get_field(x,y)
    def collision(self, x, y):
        o = self.get_organism(x,y)
        if(o.draw() == self.draw()):
            print("Reproduct")
            self.reproduct(x, y)
        else:
            print("Attack")
            self.attack(o)
    def reproduct(self,x,y):
        org = self.get_organism(x,y)
        if org.is_reproduct() == 1 or self.is_reproduct() == 1:
            return
        n_x, n_y = self.get_coordinates_neighbour()
        if(self.world.is_empty(n_x,n_y)):
            org.set_reproduct(1)
            self.get_copy(n_x, n_y).set_reproduct(1)
            self.set_reproduct(1)
    def attack(self,org):
        defend = org.defend(self)
        if defend == -1:	
            print("ESCAPE")
        elif defend == 1:
            print("LOSE")
            self.world.remove_organism(self)
        else:
            print("WON")
            self.world.remove_organism(org)
            self.world.move_to(self,org._x,org._y)
    def defend(self,org):
        if(self._power >= org._power):
            return 1
        else:
            return 0
    def check_field(self,x,y):
        return self.world.is_empty(x,y)
    def check_move(self, x,y,step , __step_k):
        if(step == 0):# up
            if y - 1 * __step_k >= 0:
                return 1
            else:
                return 0
        elif(step == 1):#down
            if y + 1 * __step_k < self.world.get_height():
                return 1
            else:
                return 0
        elif(step == 2):#left
            if x - 1 * __step_k >= 0:
                return 1
            else:
                return 0
        else:#right
            if x + 1 * __step_k < self.world.get_width():
                return 1
            else:
                return 0
    def get_coordinates_neighbour(self):
        index = -1
        for i in range(max(self._x - 1, 0),min(self._x + 1, self.world.get_width())):
            for j in range(max(self._y - 1, 0),min(self._y + 1, self.world.get_height())):
                if not(i == self._x and j == self._y) and self.world.is_empty(i,j):
                    return (i,j)
        if index == -1:
            return (max(self._x-1,0),max(self._y-1,0))
    
	
