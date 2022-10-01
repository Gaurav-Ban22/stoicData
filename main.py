
class dataHolder:
    def __init__(self, name, data, level=0, ):
        self.name = name
        self.level = level
        self.data = data

    def getSubsection(self, name):
        hasGotToCurrent = False
        for index, (key, value) in enumerate(self.data.items()):
            if key[0] == self.name:
                hasGotToCurrent = True
            if self.data[key] == self.level and key[0] != self.name and hasGotToCurrent:
                break
            
            if key[0] == name:
                # or value, but dont want to change it
                if self.data[key] == self.level                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     + 1:
                    return dataHolder(name, self.data, self.level + 1)
        raise ValueError("Category " + name + " doesn't exist in " + self.name)

    def getValue(self):
        for key in self.data:
            if key[0] == self.name:
                z = key[1]

        try:
            final = int(z)
        except:
            try:
                final = float(z)
            except:
                final = z
                try:
                    final = bool(final)
                except:
                    try:
                        final = str(final)
                    except:
                        raise ValueError("Value is not a valid type")

        return final


        
            
        

    


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
                #checks if exists
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

zx = stoic.getBase('among').getSubsection('potato').getSubsection('test').getValue()
print(str(zx))

zx = stoic.getBase('among').getSubsection('-sheesh').getValue()
print(str(zx))

#if this passes n errors and oth of thenm exist and are in realistic form, with sheesh as a subsetion of among, if works as expected.
#udsign an objectat lvl = prev + 1
#usinga nobject ot store data and to show information of subsections nd the levle tis at, so yu can retrive the name and you can 
#using bjects to store data and to store the value of each thing as we ll as the level of each thing, and then you can retriveve it kterand call funcitons on them to find the item 

#can get the path and the pattern to each subsecton
#can get the subscetion validated and if it exists can retrieve values ush cas name
#can bet the path to the subse
#can get path to wanted subsec,

