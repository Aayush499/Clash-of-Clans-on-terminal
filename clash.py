from array import *
import colorama
import sys
import os
import math
import time
import copy
import time
from colorama import Fore, Back, Style


class Field:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.layout = [["_"]* height for _ in range(width)]

class Barbarian:
   def __init__(self, posx, posy):
    self.posx = posx
    self.posy = posy
    self.symb = "b"

    def Movement()
     

class Game:
   field1 = Field(10,10)
   barb1 = Barbarian(0,5)
   field1.layout[1][1] = barb1.symb


obj =  Game()


for r in field1.layout:
   for c in r:
      print(Fore.GREEN +c,end = " " + Style.RESET_ALL)
   print()
