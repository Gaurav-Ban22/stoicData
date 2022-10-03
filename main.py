#edit until here
#edit until here v2
class lookerUpper:
    def __init__(self, sections=[], levels=[]):
        self = self
        self.sections = sections
        self.levels = levels
    
    def add(self, item, item2):
        self.sections.append(item)
        self.levels.append(item2)
    
    def replaceAt(self, index, value):
        #works pog tabktan

        self.sections[index] = value

    def getSections(self):
        return self.sections

    def getLevels(self):
        return self.levels

    #for loopings sake


class dataHolder:
    def __init__(self, name, data, index, level=0):
        self.name = name
        self.level = level
        self.data = data
        self.index = index

    def getSubsection(self, name):
        hasGotToCurrent = False
        #because of this it skips the first time if two keys in the same level are the same, gotta do some debugging to make sure that the name that is the mainsection comes first and then fionds the susbection u want sooo
        for index, key in enumerate(self.data.sections):
            #technically don't need enumerate way anymore csharp tanlnta
            if key[0] == self.name[0]:
                hasGotToCurrent = True
            if self.data.levels[index] == self.level and key[0] != self.name[0] and hasGotToCurrent:
                break
            
            if key[0] == name and hasGotToCurrent:

                # or value, but dont want to change it
                if self.data.levels[index] == self.level+1:
                    return dataHolder(key, self.data, index, self.level + 1)
        raise ValueError("Category " + name + " doesn't exist in " + self.name[0]) 

    def getValue(self):
        z = self.name[1]

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

    def setValue(self, value, stoicObj):
        for index, key in enumerate(self.data.sections):
            if index == self.index:
                x = list(key)
                x[1] = value
                x = tuple(x)
                self.data.replaceAt(index, x)
                break

        stoicObj.reload(self.data)

class stoicFile:
    def __init__(self, pathe):
        self.data = lookerUpper()
        self.pathe = pathe
        self.load(pathe)


    def load(self, pathe):
        self.data.sections = []
        self.data.levels = []
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

                    listo[1] = parts[1].strip()
                    name = tuple(listo)

                            #okay for now, but needs to be changed to be more efficient
                except:
                    pass
                self.data.add(name, level)
                #parser stays the same because it is flexible and works for any data storage, just gotta change 1 line to sava data at the end.

    def getBase(self, name):
        for index, key in enumerate(self.data.sections):
            if key[0] == name:
                #me when the code works :flumshed:               if self.data[key] == 1:
                #checks if exists
                x = dataHolder(key, self.data, index, 0)
                return x

    def reload(self, newData):

        file = open(self.pathe, "r+")
        lList = file.readlines()  
        for index, key in enumerate(newData.sections):
                lList[index] = ("    " * newData.levels[index]) + key[0] + ": " + str(key[1]) + "\n"

        with open(self.pathe, "w") as f:
            f.writelines(lList)
            
        file.close()

        self.data = newData


        
            
            


        
#gotta do actual value getting and data type conversion
    def printOut(self):
        for index, key in enumerate(self.data.getSections()):
            print(str(key) + ":" + str(self.data.levels[index]) + "\n")





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

# zx = stoic.getBase('among').getSubsection('pog').getValue()
#this wom't work, tested :D pog
# print(str(zx))

zx = stoic.getBase('among').getSubsection('-sheesh').getValue()
#this workls, pgo tbatkna
print(str(zx))


zx = stoic.getBase('among').getSubsection('potato').getSubsection('test').getValue()
#i just realized theres an error
print(zx)

zx = stoic.getBase('shee').getSubsection('pog').getSubsection('test').getValue()
#i just realized theres an error
print(zx)

stoic.getBase('shee').getSubsection('pog').getSubsection('test').setValue(7, stoic)
# stoic.printOut()

zx = stoic.getBase('shee').getSubsection('pog').getSubsection('test').getValue()
print(zx)

zx = stoic.getBase('among').getSubsection('potato').getSubsection('test').getValue()
print(str(zx))


print("-----------------------------------")

carStoic = stoicFile("cars.stoic")
carStoic.printOut()

zx = stoic.getBase('among').getSubsection('potato').getSubsection('test').getValue()
print(str(zx))



#its adding to the end so the entire dictionary iorder system to confirm and ensure accuracy with whether something is a subsection of anmother is babaopoeyed
#it adds it at the end, not before
#Howeer, at least it changes the ocrrect dictionary entry and leaves theo ther one with the same name alone (cuz dif value???)

# zx = stoic.getBase('shee').getSubsection('pog').getSubsection('test').getValue()
# #i just realized theres an error
# print(zx)
#if this passes n errors and oth of thenm exist and are in realistic form, with sheesh as a subsetion of among, if works as expected.
#udsign an objectat lvl = prev + 1
#usinga nobject ot store data and to show information of subsections nd the levle tis at, so yu can retrive the name and you can 
#using bjects to store data and to store the value of each thing as we ll as the level of each thing, and then you can retriveve it kterand call funcitons on them to find the item 

#can get the path and the pattern to each subsecton
#can get the subscetion validated and if it exists can retrieve values ush cas name
#can bet the path to the subse
#can get path to wanted subsec,

