import pygame
import time
from pygame.locals import *
from animal import Animal
import random
class Human(Animal):
    def __init__(self, x,y,world):
        Animal.__init__(self,4,4,x,y,1,world)
        self.skill_counter = 0
        self.disable_counter = 5
        self.is_activate = False
        self.is_disable = False
    def draw(self):
        return (236, 188, 180)
    def get_name(self):
        return "Human"
    def get_copy(self,x,y):
        return Human(x,y,self.world)
    def action(self):
        if self.is_activate == True:
            print("Activate")
            self.skill()
        if self.is_disable == True:
            print("Disable")
        if self.is_disable:
            if (self.disable_counter > 1):
                self.disable_counter= self.disable_counter-1
            else:
                self.is_disable = 0
                self.disable_counter = 5
        elif self.is_activate:
            if self.skill_counter > 1:
                self.skill_counter= self.skill_counter -1
                self.skill()
            else:
                self.skill_counter = 5
                self.is_activate = 0
                self.is_disable = 1
        is_end = False
        step = -1
        while not is_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); #sys.exit() if sys is imported
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print("UP")
                        if self.check_move(self._x,self._y,0 , 1) == 1:
                            step = 0
                            is_end = True
                            break;
                    elif event.key == pygame.K_DOWN:
                        print("DOWN")
                        if self.check_move(self._x,self._y,1 , 1) == 1:               
                            step = 1
                            is_end = True
                            break;
                    elif event.key == pygame.K_LEFT:
                        print("LEFT")
                        if self.check_move(self._x,self._y,2 , 1) == 1:
                            step = 2
                            is_end = True
                            break;
                    elif event.key == pygame.K_RIGHT:
                        print("RIGHT")
                        if self.check_move(self._x,self._y,3 ,1) == 1:
                            step = 3
                            is_end = True
                            break;
                    elif event.key == pygame.K_q:
                        print("Q")
                        if not self.is_activate and not self.is_disable:
                                print("You activated")
                                self.is_activate = True
                                self.skill_counter = 5
                        break;
                    elif event.key == pygame.K_o:
                        self.world.open_game()
                        print("OPEN game")
                    elif event.key == pygame.K_s:
                        self.world.save_game()
                        print("Save")
                        break;
                    else:
                        print("No key")
        self.go_by_step(step)
    def skill(self):
            for i in range(max(self._x - 1, 0),min(self._x + 1, self.world.get_width())):
                for j in range(max(self._y - 1, 0),min(self._y + 1, self.world.get_height())):
                    if not(i == self._x and j == self._y) and not self.world.is_empty(i,j):
                        org = self.world.get_field(i,j)
                        self.world.remove_organism(org)
