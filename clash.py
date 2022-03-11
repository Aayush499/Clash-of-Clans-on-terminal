from array import *
import colorama
import sys
import os
import math
import time
import copy
import time
from colorama import Fore, Back, Style
from extra import ROWS,COLS, X0, Y0
# custom modules
from game  import Village
from input import get_input
from extra import ROWS, COLS, T

#initialize the layout
WIDTH = HEIGHT =15
layout = [[Back.GREEN+"_"]* HEIGHT for _ in range(WIDTH)]

blank_board = []
for i in range(ROWS):
    row = ['_']*COLS
    row.append('\n')
    blank_board.append(row)
# for r in  layout:
#    for c in r:
#       print(Fore.GREEN +c,end = " " + Style.RESET_ALL)
#    print()

village  = Village()
while village.raid:
   key = get_input()
   #village.layout = copy.deepcopy(blank_board)
   village.King.display()

   # print(board)
   for row in village.layout:
        for c in row:
            print(c, end='')
        print()
        
   
    
  
    
   
   if (key == "d"):
      village.King.moveX()
   elif (key == "a"):
      village.King.moveX(-1)
   elif (key == "w"):
      village.King.moveY()
   elif (key == "s"):
      village.King.moveY(-1)
   print(village.King.x)
   time.sleep(T)
   
   os.system('cls' if os.name == 'nt' else 'clear')
   