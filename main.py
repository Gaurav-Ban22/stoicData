from enum import Enum

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
                    #checks if subsectione xists with given nmam,e and lervel below
                    return dataHolder(key, self.data, index, self.level + 1)
                    #cehcs iki  subseciton by wanted base
                    #check sis ubs
                    #checks i fbpassed name pf nbase section to chejck if subsection
                    #dcoed ocmpiligj
        raise ValueError("Category " + name + " doesn't exist in " + self.name[0]) 
        #retursn error if jothng ofund

    def getValue(self):
        z = self.name[1]

        try:
            final = int(z)
            
        except:
            try:
                final = tuple(z)
            except:
                final = bool(z)
                try:
                    final = float(z)
                except:
                    final = z
                    try:
                        final = list(final)
                    except:
                        try:
                            final = str(final)
                        except:
                            raise ValueError("Value is not a valid type")
        #inedfficient but works
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

    def insertSubsection(self, name, value, stoicObj):
        self.data.sections.insert(self.index+1, (name, value))
        self.data.levels.insert(self.index+1, self.level+1) #increasing level by 1 because want to make it subsection of level previous given as the base to add into, so +1
        stoicObj.reload(self.data)
        #reloads txt based on self.data, which gets passed to stoiFile and sets it as its self.data
        #in order to check for duplciates would ghave to esdit this
        #coudl use a fopr loop to check for items in the ddataholder 
        #then check if the index is greater than current indx and chek if level is currentleve + 1 
        #this woukd be a good way to check for duplicates and ensure subsections but would need a way to differntiate between differnxt ubsections of different parent sections
        # because this isnt just an isnertion or an addng or a getting, its a checking.
        #could check rfoir all of level + 1 until it isnt, and then check in the names of them, if they equal what oyu ened to add

    def deleteSubsection(self, name, stoicObj):
        hasGot = False
        brokenOut = False
        for index, key in enumerate(self.data.sections):
            if key[0] == self.name[0]:
                hasGot = True
                #has to pass it to get to the subsection of the passed parent section;
            if key[0] == name and hasGot:
                #checks if passed main base secition and checks if susbection
                if self.data.levels[index] == self.level+1:
                    #checks if subsection, sicne 1 lwevel hgher then if subsectionsince 1 more tab
                    
                    passed = False
                    passedIf = False
                    m = 0
                    for inde, key2 in enumerate(self.data.sections):
                        if inde == index and not passedIf:
                            passed = True
                            passedIf = True
                            print("passed")
                        elif passed:
                            if self.data.levels[inde] == self.level+2:
                                m += 1
                            else:
                                break
                                #coudxl otpimzie much mroe witha  boolean and then a breakage func lithe one belpow this toi codde4
                        #coudld oelif but dont need to cin yhis python ciode
                        

                    for i in range(m+1):
                        self.data.sections.pop(index)
                        self.data.levels.pop(index)
                    #it ends up deleting title with this, and then this deltes next
                    brokenOut = True
                    break

            #could use indexes to check if fgreater than index of parent section to see if subsection of parent section (would still need the check to see if its a subsection weioth the index + )

        if not brokenOut:
            raise ValueError("Category " + name + " doesn't exist in " + self.name[0] + " thus, unable to delete it")
        stoicObj.reload(self.data)
        #added delhandling

    def returnSubsections(self, name):
        hasGot = False
        brokenOut = False
        returnable = []
        for index, key in enumerate(self.data.sections):
            if key[0] == self.name[0]:
                hasGot = True
                #has to pass it to get to the subsection of the passed parent section;
            if key[0] == name and hasGot:
                #checks if passed main base secition and checks if susbection
                if self.data.levels[index] == self.level+1:
                    #checks if subsection, sicne 1 lwevel hgher then if subsectionsince 1 more tab
                    
                    passed = False
                    passedIf = False
                    m = 0
                    for inde, key2 in enumerate(self.data.sections):
                        if inde == index and not passedIf:
                            passed = True
                            passedIf = True
                            print("passed")
                        elif passed:
                            if self.data.levels[inde] == self.level+2:
                                returnable.append((key2, inde))
                            else:
                                break
                                #coudxl otpimzie much mroe witha  boolean and then a breakage func lithe one belpow this toi codde4
                        #coudld oelif but dont need to cin yhis python ciode
                        ##checks if different obj or nonchiodl has been reached by checking if the level si differenta lso fireship is copopl
                        

                    
                    #it ends up deleting title with this, and then this deltes next
                    brokenOut = True
                    break

            #could use indexes to check if fgreater than index of parent section to see if subsection of parent section (would still need the check to see if its a subsection weioth the index + )

        if not brokenOut:
            raise ValueError("Category " + name + " doesn't exist in " + self.name[0] + " thus, unable to delete it")

        return returnable

    def swapLocations(self, dest, stoicObj):
        #dest is an object of type dataHolder
        y, x = self.data.sections[self.index], self.data.levels[self.index]
        self.data.sections[self.index], self.data.levels[self.index] = self.data.sections[dest.index], self.data.levels[dest.index]
        self.data.sections[dest.index], self.data.levels[dest.index] = y, x
        #basically just resetting the values and the levels because needs to make the klvels the same
        stoicObj.reload(self.data)

    def moveSubsection(self, dest, stoicObj):
        
        if type(dest) == dataHolder:
            self.data.sections.pop(self.index)
            self.data.sections.insert(dest.index, self.name)
            self.data.levels.insert(dest.index, self.level)
            

        if type(dest) == int:
            self.data.sections.pop(self.index)
          
            self.data.sections.insert(dest, self.name)
           
            self.data.levels.insert(dest, self.level)
            

        else:
            raise ValueError("Destination must be either an integer or a dataHolder object")


        stoicObj.reload(self.data)
    
    def changeLevel(self, level, stoicObj, makeParent = True):

        try:
            self.data.levels[self.index] = level.level
            
        except:
            self.data.levels[self.index] = level
                     

        

        if not makeParent:
            ind = self.index
            name = ""
            lvl = self.level-1
            found = False
            while (not found):
                try:
                    ind -= 1
                    if self.data.levels[ind] == lvl:
                        name = self.data.sections[ind][0]

                        found = True
                except:
                    raise ValueError("No parent section found")
            #cvoudl do the getchidlren over all of the sections in the stoic file, btu cowukl dbe havilty inefficent (coukld check indexes or idneces)
            self.level = level
            self.data.levels[self.index] = lvl
            
            self.moveSubsection(ind, stoicObj)
            # self.data.levels[ind+2] += 1

            

            # for i in self.returnSubsections(name):
            #     self.data.levels[i[1]] = lvl+1
            #wont work if changing formatting iwll come bnack to later
                #changes all of the chikld susbections levels to the base level they were at earlier., thje sel;f.level-1 +1 or self.level before it was changed



            
            
             
                


        
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

    def getSubsection(self, name):
        for index, key in enumerate(self.data.sections):
            if key[0] == name:
                #me when the code works :flumshed:               if self.data[key] == 1:
                #checks if exists
                x = dataHolder(key, self.data, index, 0)
                return x

    def reload(self, newData):

        file = open(self.pathe, "r+")
        lList = []
        for index, key in enumerate(newData.sections):
            lList.append(("    " * newData.levels[index]) + key[0] + ": " + str(key[1]) + "\n")

        with open(self.pathe, "w") as f:
            f.writelines(lList)
            
        file.close()

        self.data = newData



        
#gotta do actual value getting and data type conversion
    def printOut(self):
        for index, key in enumerate(self.data.getSections()):
            print(str(key) + ":" + str(self.data.levels[index]) + "\n")



#sstill need to make schema genioafasdff schema gen to make into an objerct of the class, named thje filename (easy) for sbsection if subsections contains ubs then ignore also comimt an dpush to githui vbhsot webstiecsoed4ftbaoeoicmeilecpdewbesthoscodewbesitehsptiogh
#itgvbommitcoedocmpiel#githiwbsitehstoikcopoieloushccoedcsimchsaoprcommitpushcomtggithuigbodferwebsitehsotgithuibo0cmmutopiyushcodecompielgithubcoommitpushwescodecompilwebstiecodecompilehhowssbewicommiopushhsotwbescommitoegmopilhosartybweicompeicopdecmopielcodeightubcommitpush
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

zx = stoic.getSubsection('among').getSubsection('potato').getSubsection('test').getValue()
print(str(zx))

# zx = stoic.getSubsection('among').getSubsection('pog').getValue()
#this wom't work, tested :D pog
# print(str(zx))

zx = stoic.getSubsection('among').getSubsection('-sheesh').getValue()
#this workls, pgo tbatkna
print(str(zx))


zx = stoic.getSubsection('among').getSubsection('potato').getSubsection('test').getValue()
#i just realized theres an error
print(zx)

zx = stoic.getSubsection('shee').getSubsection('pog').getSubsection('test').getValue()
#i just realized theres an error
print(zx)

stoic.getSubsection('shee').getSubsection('pog').getSubsection('test').setValue(7, stoic)
# stoic.printOut()

zx = stoic.getSubsection('shee').getSubsection('pog').getSubsection('test').getValue()
print(zx)

zx = stoic.getSubsection('among').getSubsection('potato').getSubsection('test').getValue()
print(str(zx))


print("-----------------------------------")

carStoic = stoicFile("cars.stoic")
carStoic.printOut()

zx = stoic.getSubsection('among').getSubsection('potato').getSubsection('test').getValue()
#gets valuje
print(str(zx))

zx = carStoic.getSubsection('cars').getSubsection('volvo').getSubsection('horsepower').getValue() 
#coed comiled
#edcits file, and then prints value the nedcits agiana ndprtitns value, see last editg csharp but thsi is python with parsing szxtoic file
print(zx)


carStoic.getSubsection('cars').getSubsection('volvo').getSubsection('horsepower').setValue(100, carStoic)
#sets value and repirnts, and can also see in file that its edited, can pr5int out file contents to prove during runtime

zx = carStoic.getSubsection('cars').getSubsection('volvo').getSubsection('horsepower').getValue()
print(zx)

carStoic.getSubsection('cars').getSubsection('volvo').getSubsection('horsepower').setValue(30, carStoic)
#sets value and repirnts, and can also see in file that its edited, can pr5int out file contents to prove during runtime

zx = carStoic.getSubsection('cars').getSubsection('volvo').getSubsection('horsepower').getValue() 
#coed comiled
#edcits file, and then prints value the nedcits agiana ndprtitns value, see last editg csharp but thsi is python with parsing szxtoic file
print(zx)

carStoic.getSubsection('cars').getSubsection('volvo').insertSubsection('unitsSold', 300, carStoic)

zx = carStoic.getSubsection('cars').getSubsection('volvo').getSubsection('unitsSold').getValue() 
#coed comiled
#edcits file, and then prints value the nedcits agiana ndprtitns value, see last editg csharp but thsi is python with parsing szxtoic file
print(zx)

carStoic.getSubsection('cars').getSubsection('toyota').insertSubsection('coolnessLvl', 100, carStoic)

carStoic.getSubsection('cars').getSubsection('volvo').insertSubsection('amogus', 200, carStoic)
print(carStoic.getSubsection('cars').getSubsection('volvo').getSubsection('amogus').getValue())

print(carStoic.getSubsection('cars').returnSubsections('volvo'))

#carStoic.getSubsection('cars').getSubsection('volvo').deleteSubsection('bmw', carStoic)

#allows for returnibng of obejct with all tehd ata so can get data and get vluae and then it can get the vlaue and change it and change susbectiosn

#its adding to the end so the entire dictionary iorder system to confirm and ensure accuracy with whether something is a subsection of anmother is babaopoeyed
#it adds it at the end, not before
#Howeer, at least it changes the ocrrect dictionary entry and leaves theo ther one with the same name alone (cuz dif value???)

# zx = stoic.getSubsection('shee').getSubsection('pog').getSubsection('test').getValue()
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

kt = stoicFile("languages.stoic")
try:

    kt.getSubsection('langs').deleteSubsection('kotlin', kt)

except:
    print('this was a test, ensured error')
    #gott amake iot import rthe file and then dynuiamcally load a class as a scgheme - this is unrelated to this try catch but mprotant to overall

kt.getSubsection('langs').getSubsection('rust').getSubsection('type').changeLevel(4, kt, False)
kt.printOut()