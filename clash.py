from array import *
from pickle import FALSE
from tkinter.tix import ROW
from turtle import st
from click import style
import colorama
from datetime import datetime
import sys
import os
import math
import time
import copy
import time
from colorama import Fore, Back, Style
from buildings import TownHall
from extra import ROWS, COLS, X0, Y0, Xd0, Xl0, Xr0, Yd0, Yl0, Yr0
# custom modules
from game import HEIGHT, Village
from input import get_input
from extra import ROWS, COLS, T
import json
# initialize the layout
inlist =[]
 
xflag = 0        
WIDTH = COLS
HEIGHT = ROWS
layout = [[Fore.GREEN+"_"] * HEIGHT for _ in range(WIDTH)]
townHallDeathCheck =0
frame =0
testing =0
timmytim = 0
Dict = {}   #empty dictionary
f = open('replay.json', 'r+')
blank_board = []
characterChoice =0
for i in range(ROWS):
    row = ['_']*COLS
    row.append('\n')
    blank_board.append(row)
# for r in  layout:
#    for c in r:
#       print(Fore.GREEN +c,end = " " + Style.RESET_ALL)
#    print()
for levelSelect in range(3):
    
     
    while not characterChoice:
        characterChoice = (input("Enter character B: King Q: Queen")).upper()
        if (characterChoice != "B") and (characterChoice != "Q"):
            print("Enter a valid option")
            characterChoice = 0
    inlist.append(characterChoice)
    
    village = Village(levelSelect)
    village.King.char = characterChoice
    if(characterChoice == "Q"):
        village.King.atk = 3
    elif(characterChoice == "B"):
        village.King.atk = 4
    while village.raid:
        

        key = get_input()
        print("\033[H\033[J", end="")
        # village.layout = copy.deepcopy(blank_board)
        village.King.display()
        # village.hut1.display()
        for h in village.hutArr:
            h.display()

        for w in village.wallarr:
            w.display()

        for w in village.canonArr:
            w.display()
        # village.wall.display()
        village.townHall.display()
        for i in village.barbarianTroops:
            i.display()

        for i in village.archerTroops:
            i.display() 
        
        for i in village.balloonTroops:
            i.display() 

        # print(board)
        for row in village.layout:
            for c in row:
                print(c, end='')
            print()

        for i in village.canonArr:
            i.canonfire()
                
        for br in village.totalBuildingsarr:
            if br.destroyed():
                village.layout[br.y][br.x] = Fore.GREEN+"_" + Style.RESET_ALL
                village.totalBuildingsarr.remove(br)

        for br in village.canonArr:
            if br.destroyed():
                village.layout[br.y][br.x] = Fore.GREEN+"_" + Style.RESET_ALL 
                village.canonArr.remove(br)

        if village.King.destroyed():
            village.layout[village.King.y][village.King.x] = Fore.GREEN+"_" + Style.RESET_ALL

        
        for br in village.barbarianTroops:
            if br.destroyed():
                village.layout[br.y][br.x] = Fore.GREEN+"_" + Style.RESET_ALL
                village.barbarianTroops.remove(br)
                village.canonTargetsarr.remove(br)
                village.towerTargetsarr.remove(br)

        for br in village.archerTroops:
            if br.destroyed():
                village.layout[br.y][br.x] = Fore.GREEN+"_" + Style.RESET_ALL
                village.archerTroops.remove(br)
                village.canonTargetsarr.remove(br)
                village.towerTargetsarr.remove(br)

        for br in village.balloonTroops:
            if br.destroyed():
                village.layout[br.y][br.x] = Fore.GREEN+"_" + Style.RESET_ALL
                village.balloonTroops.remove(br)
                #village.canonTargetsarr.remove(br)
                village.towerTargetsarr.remove(br)

    #    village.King.moveY()
    #    village.King.attacking()
        for br in village.wallarr:
            if br.destroyed():
                village.layout[br.y][br.x] = Fore.GREEN+"_" + Style.RESET_ALL
                village.holearr.append((br.x,br.y))
                village.wallMercy = 1
                village.wallarr.remove(br)
                village.holearr.append
                
        for br in village.hutArr:
            if br.destroyed():
                village.layout[br.y][br.x] = Fore.GREEN+"_" + Style.RESET_ALL
                village.hutArr.remove(br)
                #village.totalBuildingsarr.remove(br)

        # while(len(village.balloonTroops)==0):
        #     village.balloonSpawner(Xl0,Yl0)
        #     village.balloonSpawner(Xl0+1,Yl0)
        
        # while(len(village.barbarianTroops)>=2):
            
        #     village.archerSpawner(Xl0,Yl0)

        # while(len(village.barbarianTroops)<=1):
            
        #     village.barbarianSpawner(Xd0,Yd0)
        #     village.barbarianSpawner(Xr0, Yr0)
            
        # village.King.moveY()
        #village.balloonSpawner(Xl0 ,Yl0)
        
        # while  testing==0:
        #     village.barbarianSpawner(Xr0, Yr0)
        #     village.barbarianSpawner(Xl0, Yl0)
        #     testing += 1
        

        if(not village.King.destroyed()):
            if(xflag):
                if((datetime.now()-timmytim).total_seconds() >=1):
                    village.King.xBow()
                    xflag = 0
            if (key == "d"):
                village.King.moveX()
                Dict[frame] = key
            elif (key == "a"):
                village.King.moveX(-1)
                Dict[frame] = key
            elif (key == "w"):
                village.King.moveY(-1)
                Dict[frame] = key
            elif (key == "s"):
                village.King.moveY()
                Dict[frame] = key
            elif (key == " "):
                if(village.King.char == 'B'):
                    village.King.attacking()
                elif(village.King.char == 'Q'):
                    village.King.attackQueen()
                Dict[frame] = key
            elif (key == "l"):
                if(village.King.char == 'B'):
                    village.King.leviathan()
                elif(village.King.char == 'Q'):  
                    timmytim = datetime.now()
                    xflag = 1
                Dict[frame] = key
            elif (key == "2"):
                village.barbarianSpawner(Xd0,Yd0)
                Dict[frame] = key
            elif (key == "3"):
                village.barbarianSpawner(Xr0, Yr0)
                Dict[frame] = key
            elif (key == "4"):
                village.barbarianSpawner(Xl0, Yl0)
                Dict[frame] = key
            
            elif (key == "5"):
                village.archerSpawner(Xl0,Yl0)
                Dict[frame] = key
            elif (key == "6"):
                village.balloonSpawner(Xl0,Yl0)
                #village.balloonSpawner(Xl0+1,Yl0)
                Dict[frame] = key
            elif (key == "7"):
                village.archerSpawner(Xr0,Yr0)
                Dict[frame] = key
            elif (key == "8"):
                village.archerSpawner(Xd0,Yd0)
                Dict[frame] = key
            elif (key == "9"):
                village.balloonSpawner(Xd0,Yd0)
                #village.balloonSpawner(Xl0+1,Yl0)
                Dict[frame] = key
            elif (key == "0"):
                village.balloonSpawner(Xr0,Yr0)
                #village.balloonSpawner(Xl0+1,Yl0)
                Dict[frame] = key
            elif (key == "."):
                village.healthUp()
                Dict[frame] = key
            elif (key == ","):
                village.speedUp()
                Dict[frame] = key

        inlist.append(key)
        for i in village.barbarianTroops:
            i.pathFinder()
            i.attacking()

        for i in village.archerTroops:
            i.pathFinder()
            i.attacking()

        for i in village.balloonTroops:
            i.pathFinder()
            i.attacking()

        print(village.King.x)
        print(village.King.y)
        print("health:" + str(village.King.health))
        for i in range(village.King.health):
            print(Back.GREEN+"|"+ Style.RESET_ALL, end = " ")
        print()
        print("speed:" + str(village.King.turns))
        print("attack:" + str(village.King.atk))
        print(len(village.barbarianTroops))

        time.sleep(T)
        frame+=1
        if not village.totalBuildingsarr:
            print("VICTORY")
            village.raid = False 
            # data = json.load(f)
            # data.append(inlist) 
            # f.seek(0)
            # json.dump(data, f)
            
        elif  (not village.barbarianTroops) & village.King.destroyed():
            print("LOSS")
            village.raid = False
            levelSelect = 4
            break
            # data = json.load(f)
            # data.append(inlist)
            # f.seek(0)
            # json.dump(data, f)

        # os.system('cls' if os.name == 'nt' else 'clear')
    else:
        continue
    break # break happens in inner loop, break outer loop too.


data = json.load(f)
data.append(inlist) 
f.seek(0)
json.dump(data, f)