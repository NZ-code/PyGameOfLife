import pygame
from organism import Organism
from animal import Animal
from plant import Plant
from human import Human
from antelope import Antelope
from fox import Fox
from sheep import Sheep
from turtle import Turtle
from grass import Grass
from wolf import Wolf
from belladonna import Belladonna
from guarana import Guarana
from sonchus import Sonchus
from sosnowsky_hogweed import Sosnowsky_Hogweed
from cyber_sheep import Cyber_Sheep
class World:
    def __init__(self, width_num,height_num):
        self.__field_width = 25 # size of 
        self.__field_height = 25 # field
        self.__width_num = width_num
        self.__height_num = height_num
        self.__organisms = []
        self.wmap = []
        for r in range(width_num * height_num):
            self.wmap.append(0)
        #print(self.wmap)
    def is_empty(self,x,y):
        index = self.get_index(x,y)
        if self.wmap[index] == 0:
            return 1
        else:
            return 0
    def remove_organism(self,org):
        index = self.get_index(org.get_x(),org.get_y())
        self.__organisms.remove(org)
        self.wmap[index] = 0
    def move_to(self, org ,x, y):
        index = self.get_index(org.get_x(),org.get_y())
        new_index = self.get_index(x,y)
        org.set_x(x)
        org.set_y(y)
        print("Moved to "+str(x) +" "+ str(y))
        self.wmap[new_index] = org
        self.wmap[index] = 0
    def get_index(self,x,y):
        return (y * self.__width_num) + x;
    def get_height(self):
        return self.__height_num
    def get_width(self):
        return self.__width_num
    def add_organism(self,org):
        index = self.get_index(org.get_x(), org.get_y())
        self.wmap[index] = org
        self.__organisms.append(org)
    def set_organism(self):
        #Belladonna(0,0,self)
        #Sosnowsky_Hogweed(9,9,self)
        Wolf(9,0,self)
        Human(4,2,self)
        #Guarana(0,0,self)
    def made_tour(self):
         for o in self.__organisms:
             if o.is_reproduct() == True:
                 continue
             print(o.get_name())
             o.action()
    def sort_key(self,org):
        return org.get_initiative()
    def print_world(self):
        self.made_tour()
        pygame.init()
        win = pygame.display.set_mode(( self.__width_num * self.__field_width,self.__height_num * self.__field_height))
        pygame.display.set_caption("Game of life: MIKITA ZENEVICH 187709 GRUPA 6")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("UP")
                elif event.key == pygame.K_LEFT:
                    print("UP")
                elif event.key == pygame.K_DOWN:
                    print("UP")
                elif event.key == pygame.K_RIGHT:
                    print("UP")
                    
        win.fill((0,0,0))
        self.__organisms.sort(key=self.sort_key)
        for o in self.__organisms:
            pygame.draw.rect(win, o.draw(),(o.get_x()* self.__field_width ,o.get_y() * self.__field_height,self.__field_width,self.__field_height))
        for o in self.__organisms:
            o.set_reproduct(0)
            o.increase_age()
        pygame.display.update()
    def get_field(self,x,y):
        index = self.get_index(x,y)
        return self.wmap[index] 
    def end_game(self):
        pygame.quit()
