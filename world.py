import pygame
import time
import pickle
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
        self.pg = pygame.init()
        self.win = pygame.display.set_mode(( self.__width_num * self.__field_width,self.__height_num * self.__field_height))
        pygame.display.set_caption("Game of life: MIKITA ZENEVICH 187709 GRUPA 6")
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
        Belladonna(0,0,self)
        Sosnowsky_Hogweed(9,9,self)
        Wolf(9,0,self)
        #Human(4,2,self)
    def made_tour(self):
         for o in self.__organisms:
             if o.is_reproduct() == True:
                 continue
             print(o.get_name())
             o.action()
    def sort_key(self,org):
        return org.get_initiative()
    def get_coords_mouse(self,pos_x,pos_y):
        r_x = int(pos_x/self.__field_width)
        r_y = int(pos_y/self.__field_height)
        return (r_x,r_y)
    def print_world(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit(); #sys.exit() if sys is imported
                    return
                if event.type == pygame.MOUSEBUTTONUP:
                  pos_x,pos_y = pygame.mouse.get_pos()
                  self.menu = pygame.display.set_mode(( self.__width_num * self.__field_width, self.__height_num * self.__field_height))
                  self.menu.fill((133,133,133))
                  
                  l_org = [Antelope,  Fox,  Sheep, Turtle, Grass,  Wolf, Belladonna, Guarana,  Sonchus,  Sosnowsky_Hogweed,Cyber_Sheep]
                  l_index = -1
                  for i in range(len(l_org)):
                      pygame.draw.rect(self.menu, l_org[i].draw(l_org[i]),( 0* self.__field_width ,i * self.__field_height,self.__width_num * self.__field_width,self.__field_height))
                  pygame.display.update()
                  is_end = False
                  while not is_end:
                      for event in pygame.event.get():
                          if event.type == pygame.MOUSEBUTTONUP:
                              pos_x_color,pos_y_color = pygame.mouse.get_pos()
                              l_index = int(pos_y_color/ self.__field_height)
                              is_end = True
                  #time.sleep(3)
                  real_x, real_y = self.get_coords_mouse(pos_x,pos_y)
                  org = l_org[l_index](real_x, real_y,self)
                  self.add_organism(org)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.save_game()
                        print("Save game")
                    elif event.key == pygame.K_o:
                        self.open_game()
                        print("OPEN game")
        self.made_tour()
        self.win.fill((0,0,0))
        self.__organisms.sort(key=self.sort_key)
        for o in self.__organisms:
            pygame.draw.rect(self.win, o.draw(),(o.get_x()* self.__field_width ,o.get_y() * self.__field_height,self.__field_width,self.__field_height))
        for o in self.__organisms:
            o.set_reproduct(0)
            o.increase_age()
        pygame.display.update()
    def get_field(self,x,y):
        index = self.get_index(x,y)
        return self.wmap[index] 
    def end_game(self):
        pygame.quit()
    def save_game(self):
        l_o = []
        for o in self.__organisms:
            o_tuple = (o.get_x(),o.get_y(),type(o))
            l_o.append(o_tuple)
        s_tuple = (self.__width_num,self.__height_num,l_o)
        filename = 'saves'
        outfile = open(filename,'wb')
        pickle.dump(s_tuple,outfile)
        outfile.close()
    def open_game(self):
        filename = 'saves'
        s_tuple = pickle.load( open(filename, "rb" ) )
        self.__width_num = s_tuple[0]
        self.__height_num = s_tuple[1]
        l_o  = s_tuple[2]
        self.__organisms = []
        self.wmap = []
        for r in range(self.__width_num * self.__height_num):
            self.wmap.append(0)
        for o in l_o:
            type_org = o[2]
            type_org(o[0],o[1],self)
            
