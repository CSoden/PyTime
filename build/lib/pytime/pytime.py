import time as t
import os


class Pytime:
    def calcAverageExec(self, func, args, its=0):
        tot = 0
        for i in range(its):
            if (i % (its/100)) == 0:
                self.printProgress(int(i//(its/100)))
            a = t.time()
            func(*args)
            b = t.time()
            tot += (b-a)
        os.system("cls")
        self.getResult(tot, its)
        
    def printProgress(self, i):
        os.system("cls")
        print("-"*102)
        print("|" + "/"*i + " "*(100-i) + "|" + f" {i}%")
        print("-"*102)
        
    def getResult(self, tot, its):
        print("-"*102)
        print(" "*20 + "Total iterations " + "|" + f"{its}" + "|" + " "*10 + "Average time taken " + "|" + f"{round((1000*tot/its), 5)}" + "ms|")
        print("-"*102)