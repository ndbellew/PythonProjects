#!/bin/pyton3
import random
import math
import sys

class StatMaker:

    def __init__(self, _STR, _DEX, _CON, _INT, _WIS, _CHA):
        self.S = _STR
        self.D = _DEX
        self.C = _CON
        self.I = _INT
        self.W = _WIS
        self.CH = _CHA
        self.count = 0
        self.GrandTotalCount = 0

    def RandInt(self,Min):
        Num = 0
        while(Num<Min):
            Num = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
            self.count +=1
        return Num
    def SetStats(self):
        STR=self.RandInt(self.S)
        DEX=self.RandInt(self.D)
        CON=self.RandInt(self.C)
        INT=self.RandInt(self.I)
        WIS=self.RandInt(self.W)
        CHA=self.RandInt(self.CH)
        return STR,DEX,CON,INT,WIS,CHA

    def DetermineStats(self):
        total = 0
        if len(sys.argv) > 1:
            num = int(sys.argv[1])
        else:
            num = 70
        while (total<num):
            STR,DEX,CON,INT,WIS,CHA = self.SetStats()
            total = int(math.fsum([STR,DEX,CON,INT,WIS,CHA]))
        return total, STR, DEX, CON, INT, WIS, CHA

    def PrintStats(self,total, STR,DEX,CON,INT,WIS,CHA):
        print("______________")
        print("STR: ",STR,"\nDEX: ",DEX,"\nCON: ",CON,"\nINT: ",INT,"\nWIS: ",WIS,"\nCHA: ",CHA,"\nTotal: ",total)
        print("Total Rolls to get score: ",self.count)
        print("Grand Total Rolls this session: ", self.GrandTotalCount)
        print("______________")

    def run(self):
        total, STR,DEX,CON,INT,WIS,CHA = self.DetermineStats()
        self.GrandTotalCount += self.count
        self.PrintStats(total, STR,DEX,CON,INT,WIS,CHA)
        self.count = 0

def splitvars(line):
    for x in line.split():
        yield int(x)

def main():
    stats = input("Input your stat minimums in order (STR,DEX,CON,INT,WIS,CHA)\n ex. 3 3 3 3 7 3\n")
    STR,DEX,CON,INT,WIS,CHA = splitvars(stats)
    RollStats = StatMaker(STR,DEX,CON,INT,WIS,CHA)
    RollAgain = True
    while(RollAgain):
        RollStats.run()
        x = input("Would you like to roll again? y/n\n")
        if x == 'n':
            RollAgain = False


if __name__ == "__main__":
    main()
