class Organism:
    def __init__(self,power,initiative,x,y,world):
        self._age = 0
        self._reprdt = 0
        self._x = x
        self._y = y
        self.world = world
        self._power = power
        self._initiative = initiative
        self.world.add_organism(self)
    def action(self):
        raise NotImplementedError()
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def get_initiative(self):
        return self._initiative
    def get_power(self):
        return self._power
    def set_power(self,power):
        self._power = power
    def set_x(self, x):
        self._x = x
    def set_y(self, y):
        self._y = y
    def draw(self):
        return (255,0,0)
    def set_reproduct(self, val):
        self._reprdt = val
    def increase_age(self):
        self._age = self._age + 1
    def is_reproduct(self):
        if(self._reprdt == 1):
            return True
        else:
            return False
    
