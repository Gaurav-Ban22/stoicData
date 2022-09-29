
import os

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
                name = ("","")
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

                    listo[1] += parts[1].strip()
                    name = tuple(listo)

                            #okay for now, but needs to be changed to be more efficient
                except:
                    pass
                self.data[name]  = level

        
#gotta do actual value getting and data type conversion
    def printOut(self):
        for key in self.data:
            print(key, self.data[key])

    # # def getSubsection(self, name):
    # #     try:
    # #         level = self.data[name]

    # #     except:
    # #         raise Exception("No such subsection of stoic: " + self.pathe)
        
         
            
    


stoic = stoicFile("data.stoic")
stoic.printOut()

