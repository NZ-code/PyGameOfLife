from world import World
import time
#width_num = int(input("HOW MANY FIELD IN WIDTH:"))
#height_num = int(input("HOW MANY FIELD IN HEIGHT:"))
w = World(10, 10)
w.set_organism()
while True:
    time.sleep(0.7)
    w.print_world()
