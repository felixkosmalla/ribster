import math
import random

develop = False

if not develop:
    import sys



def init_thermo():
    pass

i = 0.0

random.seed(100)

def read_temperature():
    global i
    i+=0.01
    i%=math.pi

    return (math.sin(i))*20.0 + 100.0 + random.randint(-2, 2)

    pass

