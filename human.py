import pygame
from pygame.locals import *
from animal import Animal
import random
class Human(Animal):
    def __init__(self, x,y,world):
        Animal.__init__(self,4,4,x,y,1,world)
    def draw(self):
        return rgb(236, 188, 180)
    def get_name(self):
        return "Human"
    def get_copy(self,x,y):
        return Human(x,y,self.world)
    def action(self):

