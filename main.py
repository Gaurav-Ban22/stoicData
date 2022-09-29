
import os
from enum import Enum

class whatToGet(Enum):
    VALUE = "Value"
    NAME = "Name"
    #probably doing this wrong

class dataHolder:
    def __init__(self, name, data, level=0, ):
        self.name = name
        self.level = level
        self.data = data

    def getSubsection(self, name):
         for key in self.data:
            if key == name:
                if self.data[key] == self.level + 1:
                    return dataHolder(name, self.level + 1)
            else:
                raise ValueError("Category " + name + " doesn't exist")

    


class stoicFile:
    def __init__(self, pathe):
        self.data = {}
        self.pathe = pathe
        self.load(pathe)


    def load(self, pathe):
        with open(pathe, 'r') as f:
            level = 0

            lines = f.readlines()
            print(lines)
            for line in lines:    
                level = 0
                name = ("","header cannot have value")
                if line.startswith("    "):
                    test = 0
                    for char in line:
                        if char == " ":
                            test += 1
                            if test == 4:
                                level += 1
                                test = 0
                        else:
                            break
                g = -1  
                parts = line.split(":") 
                try:
                    listo = list(name)
                    listo[0] = parts[0].strip()

                    name = tuple(listo)

                    listo[1] = parts[1].strip()
                    name = tuple(listo)

                            #okay for now, but needs to be changed to be more efficient
                except:
                    pass
                self.data[name]  = level


    def getBase(self, name):
        for key in self.data:
            if key[0] == name:
                #me when the code works :flumshed:               if self.data[key] == 1:
                x = dataHolder(name, self.data, 0)
                return x
            
            


        
#gotta do actual value getting and data type conversion
    def printOut(self):
        for key in self.data:
            print(key, self.data[key])





    # def get(self, dat, getWhat):

    #     if not isinstance(getWhat, whatToGet):
    #         raise TypeError("getWhat must be of enum type whatToGet (VALUE or NAME)")
    #     if not isinstance(dat, dataHolder):
    #         raise TypeError("second parameter must be of type dataHolder")

    #     if getWhat.value == "Value":

    #         for key in self.data:
    #             if key[0] == dat.name and self.data[key] == dat.level+1:
    #                 #if name (0th index) of tuple is name and the level is prev level +1, return value which is 1st index of tuple
    #                 return key[1]

            




    #     if getWhat.value == "Name": 

    #         try:
    #             level = self.data[dat.name]
    #             #checking if exists easily by checking if level exists
    #             return dataHolder(dat.name, level)


    #         except:
    #             raise Exception("No such subsection of stoicfile " + self.pathe)
        
        
         
            
    


stoic = stoicFile("data.stoic")

stoic.printOut()

zx = stoic.getBase('among').name

#if this passes n errors and oth of thenm exist and are in realistic form, with sheesh as a subsetion of among, if this works as expected.



