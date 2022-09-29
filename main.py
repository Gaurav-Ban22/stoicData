
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
                name = ""
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
                        
                for char in line.strip():   
                    name += char
                self.data[name]  = level

        

    def printOut(self):
        for key in self.data:
            print(key, self.data[key])


stoic = stoicFile("data.stoic")
stoic.printOut()

