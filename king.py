import time
import colorama
from colorama import Fore, Back, Style
import math 
# custom modules
from extra import healthCOLOR_king, ROWS, COLS,X0, Y0



class King():

    def __init__(self, village,health, width):
        self.village = village
        self.x = X0  # (x, y) are coordinates of the centre
        self.y = Y0
        self.v = 1
        self.color = Back.BLUE
        #self.char = 'B'
        self.char = 'Q'
        self.attack = False
        self.health = health
        self.color = healthCOLOR_king[health%len(healthCOLOR_king)]
        self.facing = (0,0)
        self.atk = 4
        self.turns =1
        self.atkRange = 0
        self.fallTime = 0
        
    def reset(self):
        self.x = X0
        self.y = Y0

    def moveX(self, dirn=1):
        for i in range(self.turns):
            x = self.x
            self.facing = (dirn,0)
            if (x >= COLS-1  and dirn == 1):
                return
            if (x  <= 1 and dirn == -1):
                return
            if(Fore.GREEN not in (self.village.layout[self.y][self.x + self.v*dirn])):
                return
            self.village.layout[self.y][self.x] = Fore.GREEN +  "_" + Style.RESET_ALL
            self.x += self.v*dirn
    
    def moveY(self, dirn = 1):
        for i in range(self.turns):
            y = self.y
            self.facing = (0,dirn)
            if (y >= ROWS-1  and dirn == 1):
                return
            if (y  < 1 and dirn == -1):
                return
            if(Fore.GREEN not in (self.village.layout[self.y + self.v*dirn][self.x])):
                return


            self.village.layout[self.y][self.x] = Fore.GREEN + "_" + Style.RESET_ALL
            self.y += self.v*dirn


    def display(self):
        y = self.y
        x = self.x
        arr = self.village.layout
        if (x   <= 0):
            x = 0
        elif (x  >= COLS-1):
            x = COLS-1 
        if self.attack:
            self.color = Back.WHITE
        else:
            self.color = healthCOLOR_king[self.health%len(healthCOLOR_king)]
        
        arr[self.y][self.x] = self.color + self.char + Style.RESET_ALL
        self.village.layout = arr
    
    def attacking(self):
        #self.attack = True
        wallobj = self.village.wallarr[0]

        if( "W" in self.village.layout[self.y+ self.facing[1]][self.x+self.facing[0]] and not self.village.wallMercy):
            print("BOOM")
            #self.attack = False
            for x in self.village.wallarr:
                if x.pos == (self.x+self.facing[0],self.y+ self.facing[1]):
                    print("i found it!")
                    wallobj = x
                    break

            wallobj.hit(self.atk)
        elif( "h" in self.village.layout[self.y+ self.facing[1]][self.x+self.facing[0]]):
            print("BOOM")
            #self.attack = False
            for x in self.village.hutArr:
                if x.pos == (self.x+self.facing[0],self.y+ self.facing[1]):
                    print("i found it!")
                    wallobj = x
                    break

            wallobj.hit(self.atk)
        
        elif( "T" in self.village.layout[self.y+ self.facing[1]][self.x+self.facing[0]]):
            print("BOOM")
            #self.attack = False
            self.village.townHall.hit(self.atk)
        
         

        elif( "C" in self.village.layout[self.y+ self.facing[1]][self.x+self.facing[0]]):
            print("BOOM")
            #self.attack = False
            for x in self.village.canonArr:
                if x.pos == (self.x+self.facing[0],self.y+ self.facing[1]):
                    print("i found it!")
                    canonobj = x
                    break

            canonobj.hit(self.atk)

        elif( "t" in self.village.layout[self.y+ self.facing[1]][self.x+self.facing[0]]):
            print("BOOM")
            #self.attack = False
            for x in self.village.canonArr:
                if x.pos == (self.x+self.facing[0],self.y+ self.facing[1]):
                    print("i found it!")
                    canonobj = x
                    break

            canonobj.hit(self.atk)

    def destroyed(self):
        if self.health <= 0:
            self.char = "_"
            return True
        return False

    def hit(self):
        if self.health:
            self.health -=1

        if self.health >= 0:
            self.color = healthCOLOR_king[self.health%len(healthCOLOR_king)]

    def leviathan(self):
        faces = [(1,0), (-1,0), (0,1), (0,-1)]
        storage = self.facing

        for i in range(-2,3):
            for j in range(-2,3):
                
                if(self.x+i>=COLS-1):
                    i = (COLS-1)-self.x
                elif(self.x + i <0):
                    i = -self.x
                
                if(self.y+j>=ROWS-1):
                    j = (ROWS-1)-self.y
                elif(self.y + j <0):
                    j = -self.y
                self.facing = (i,j)

                self.attacking()
        self.facing = storage

    def leviathan2(self):
        faces = [(1,0), (-1,0), (0,1), (0,-1)]
        storage = self.facing

        for i in range(-4,5):
            for j in range(-4,5):
                
                if(self.x+i>=COLS-1):
                    i = (COLS-1)-self.x
                elif(self.x + i <0):
                    i = -self.x
                
                if(self.y+j>=ROWS-1):
                    j = (ROWS-1)-self.y
                elif(self.y + j <0):
                    j = -self.y
                self.facing = (i,j)

                self.attacking()
        self.facing = storage

    def attackQueen(self):
        x = self.x
        y = self.y
        self.x = self.x + 8*self.facing[0]
        self.y = self.y+ 8*self.facing[1]
        if(self.y>=ROWS-1):
            self.y = ROWS-2
        elif(self.y<0):
            self.y = 0
        
        if(self.x>=COLS-1):
            self.x = COLS-2
        elif(self.x<0):
            self.x = 0
        
        self.leviathan()
        self.x = x
        self.y =y

    
    def xBow(self):
        x = self.x
        y = self.y
        self.x = self.x + 16*self.facing[0]
        self.y = self.y+ 16*self.facing[1]
        if(self.y>=ROWS-1):
            self.y = ROWS-2
        elif(self.y<0):
            self.y = 0
        
        if(self.x>=COLS-1):
            self.x = COLS-2
        elif(self.x<0):
            self.x = 0
        
        self.leviathan2()
        self.x = x
        self.y =y


    

    
             
        
class Barbarian(King):

    def __init__(self, village,health, width,x,y):
        super().__init__(village,  health,  width)
        #self._color = healthCOLOR_wall[health]
        self.char = 'b'
        self.x = x  # (x, y) are coordinates of the centre
        self.y = y
        self.atk = 2
        self.entranceSearch = 0
        self.deadendcntr = 0
        self.prevFacingArr = []

    def pathFinder(self):

        if not self.village.totalBuildingsarr:
            return
        
        if self.deadendcntr <3:
            if(self.entranceSearch or len(self.village.holearr)==0):
                min =1000
                target = self.village.totalBuildingsarr[0]
                for i in self.village.totalBuildingsarr:
                    dist = math.sqrt((self.x - i.x)**2 + (self.y - i.y)**2)
                    if min > dist:
                        min = dist
                        target = i
                
                if(self.x < target.x):
                    self.moveX()
                elif(self.x> target.x):
                    self.moveX(-1)

                if(self.y< target.y):
                    self.moveY()
                elif(self.y> target.y):
                    self.moveY(-1)
            else:
                min =1000
                prevx = self.x
                prevy = self.y
                prevfacing = self.facing    
                target = self.village.holearr[0]
                for i in self.village.holearr:
                    dist = math.sqrt((self.x - i[0])**2 + (self.y - i[1])**2)
                    if min > dist:
                        min = dist
                        target = i
                
                if(self.x < target[0]):
                    self.moveX()
                elif(self.x> target[0]):
                    self.moveX(-1)

                if(self.y< target[1]):
                    self.moveY()
                elif(self.y> target[1]):
                    self.moveY(-1)
                if self.x == target[0] and self.y== target[1]:
                    self.entranceSearch = 1
                if self.x == prevx and self.y == prevy :
                    self.moveX(prevfacing[0])
                    self.moveY(prevfacing[1])
                    self.deadendcntr+=1
        elif self.deadendcntr >=3:
            min =1000
            prevx = self.x
            prevy = self.y
            prevfacing = self.facing    
            target = self.village.corners[0]
            for i in self.village.corners:
                dist = math.sqrt((self.x - i[0])**2 + (self.y - i[1])**2)
                if min > dist:
                    min = dist
                    target = i
            
            if(self.x < target[0]):
                self.moveX()
            elif(self.x> target[0]):
                self.moveX(-1)

            if(self.y< target[1]):
                self.moveY()
            elif(self.y> target[1]):
                self.moveY(-1)
            if self.x == target[0] and self.y== target[1]:
                self.entranceSearch = 1
            if self.x == prevx and self.y == prevy :
                if(self.facing[0]==0):
                    if "W" not in self.village.layout[self.y+ self.facing[1]][self.x+1]  :
                        self.moveX(2)
                    elif "W" not in self.village.layout[self.y + self.facing[1]][self.x-1]  :
                        self.moveX(-2)
                elif(self.facing[1] ==0)    :
                    if "W" not in self.village.layout[self.y+ 1][self.x+self.facing[0]]  :
                        self.moveY(2)
                    elif "W" not in self.village.layout[self.y -1][self.x+self.facing[0]]  :
                        self.moveY(-2)
                self.deadendcntr = 0

                
            

            
            

        
   

class Archer(King):

    def __init__(self, village,health, width,x,y):
        super().__init__(village,  health,  width)
        #self._color = healthCOLOR_wall[health]
        self.char = 'a'
        self.x = x  # (x, y) are coordinates of the centre
        self.y = y
        self.atk = 1
        self.turns = 2
        self.cooldown =0
        self.archRange = 3
        self.entranceSearch = 0
    def pathFinder(self):

        if not self.village.totalBuildingsarr:
            return
        deadendcntr = 0

        min =1000
        
        archRange = self.archRange
        target = self.village.totalBuildingsarr[0]
        for i in self.village.totalBuildingsarr:
            dist = math.sqrt((self.x - i.x)**2 + (self.y - i.y)**2)
            if min > dist:
                min = dist
                target = i
        if min > archRange:
            if(self.x < target.x):
                self.moveX()
            elif(self.x> target.x):
                self.moveX(-1)

            if(self.y< target.y):
                self.moveY()
            elif(self.y> target.y):
                self.moveY(-1)

    def attacking(self):
        min =1000
        minwall = 1000
        targetwall = self.village.wallarr[0]
        if(len(self.village.totalBuildingsarr)>=1):
            target = self.village.totalBuildingsarr[0]
            for i in self.village.totalBuildingsarr  :
                dist = math.sqrt((self.x - i.x)**2 + (self.y - i.y)**2)
                if min > dist:
                    min = dist
                    target = i

            for i in self.village.wallarr  :
                dist = math.sqrt((self.x - i.x)**2 + (self.y - i.y)**2)
                if minwall > dist:
                    minwall = dist
                    targetwall = i
            
            if(min>self.archRange):
                target=targetwall
                min = minwall
            self.cooldown+=1
            
            if self.cooldown >= 2:
                if min <= self.archRange:

                    target.hit(self.atk)
                    self.cooldown =0
            


class Balloons(King):
    def __init__(self, village,health, width,x,y):
        super().__init__(village,  health,  width)
        #self._color = healthCOLOR_wall[health]
        self.char = '*'
        self.x = x  # (x, y) are coordinates of the centre
        self.y = y
        self.atk = 4
        self.turns = 2
        self.archRange =2
        self.cooldown = 5
    def moveX(self, dirn=1):
        for i in range(self.turns):
            x = self.x
            self.facing = (dirn,0)
            if (x >= COLS-1  and dirn == 1):
                return
            if (x  <= 1 and dirn == -1):
                return
            # if("W" not in (self.village.layout[self.y][self.x + self.v*dirn]) or "_" not in (self.village.layout[self.y][self.x + self.v*dirn])):
            #     return
            self.village.layout[self.y][self.x] = Fore.GREEN +  "_" + Style.RESET_ALL
            self.x += self.v*dirn
    
    def moveY(self, dirn = 1):
        for i in range(self.turns):
            y = self.y
            self.facing = (0,dirn)
            if (y >= ROWS-1  and dirn == 1):
                return
            if (y  < 1 and dirn == -1):
                return
            # if("W" not in (self.village.layout[self.y + self.v*dirn][self.x]) or "_" not in (self.village.layout[self.y + self.v*dirn][self.x])):
            #     return


            self.village.layout[self.y][self.x] = Fore.GREEN + "_" + Style.RESET_ALL
            self.y += self.v*dirn


            
    def pathFinder(self):

        if not self.village.totalBuildingsarr:
            return
        min =1000
        
        archRange = self.archRange
        target = self.village.totalBuildingsarr[0]

        if(len(self.village.canonArr)==0):
            for i in self.village.totalBuildingsarr:
                dist = math.sqrt((self.x - i.x)**2 + (self.y - i.y)**2)
                if min > dist:
                    min = dist
                    target = i
        else:
            for i in self.village.canonArr:
                dist = math.sqrt((self.x - i.x)**2 + (self.y - i.y)**2)
                if min > dist:
                    min = dist
                    target = i

        if min > archRange:
            if(self.x < target.x):
                self.moveX()
            elif(self.x> target.x):
                self.moveX(-1)

            if(self.y< target.y):
                self.moveY()
            elif(self.y> target.y):
                self.moveY(-1)

    def attacking(self):
        min =1000
        
        
        if( len(self.village.canonArr)>=1):
            target = self.village.canonArr[0]
            for i in self.village.canonArr :
                dist = math.sqrt((self.x - i.x)**2 + (self.y - i.y)**2)
                if min > dist:
                    min = dist
                    target = i
        elif(len(self.village.totalBuildingsarr)>=1 and len(self.village.canonArr) ==0):
            target = self.village.totalBuildingsarr[0]
            for i in self.village.totalBuildingsarr  :
                dist = math.sqrt((self.x - i.x)**2 + (self.y - i.y)**2)
                if min > dist:
                    min = dist
                    target = i

            
            
            
        self.cooldown+=1
            
        if self.cooldown >= 2:
            if min <= self.archRange:

                target.hit(self.atk)
                self.cooldown =0

     

 
        


        
        
     
    
