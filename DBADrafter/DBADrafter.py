import csv
import random
import os


###UNIVERSALS###


itemTotal = 0 #total items read from file
F = 9 #features per pack
P = 6 #number of packs
chosen = []


###CLASSES###


class Feature:
    def __init__(self, t, user, name, cost, tier, description):
        self.type = str(t)
        self.user = str(user)
        self.name = str(name)
        self.cost = str(cost)
        if tier != "":
            self.tier = int(tier)
        self.description = str(description)

    def featureType(self):
        if self.type == "weapon":
            return 0
        elif self.type == "talent":
            return 1
        elif self.type == "passive":
            return 2
        elif self.type == "ability":
            return 3
        else:
            print("Error: Feature " + self.name + " is not property assigned a feature type")


###FUNCTIONS###


def randomFeature(): #Generate a random number correlating to a feature in the featureList, and will never choose repeats
    val = random.randint(0,itemTotal - 1)
    if val in chosen:
        return randomFeature()
    else:
        chosen.append(val)
        return val

def printFeature(feature): #Returns a string representing a single feature, printable to the screen or to a file
    ftest = "(from " + feature.user + ") " + feature.name
    ftype = feature.featureType()
    if ftype == 3:
        ftest += " (" + feature.cost + ")"
    ftest += " - " + feature.description
    return ftest

def rollPack(features):
    pack = []
    j = 1
    for i in range(F):
        n = randomFeature()
        pick = printFeature(features[n])
        print("(" + str(j) + ") " + pick + "\n")
        pack.append(pick)
        j += 1
    looper = 0
    print("\n")
    while looper != 1 :
        x = int(input())
        if x >= 1 and x <= F :
            os.system('cls')
            return pack[x-1]
        else:
            print("Not a valid choice. Try again.\n")
        
def createOutputFile(outputString, file):
    file.write(outputString)



###MAIN###


featureText = []
featureList = []
outputString = ""

i = 0
while os.path.exists("DraftedKit%s.txt" % i):
    i += 1

outputFile = open("DraftedKit%s.txt" % i,"w+")

with open("DraftData.csv", newline='', encoding="UTF-8") as dataFile: #Gets featureList[]
    dataFile = csv.reader(dataFile)  #Get text into csvreader object
    for i in dataFile: #Read text into a list
        featureText.append(i)
        #itemTotal += 1 #Increment the number of features we have

for i in featureText: #Creates Feature objects and adds them to featureList (the list we'll use for things)
    feature = Feature(i[0],i[1],i[2],i[3],i[4],i[5])
    featureList.append(feature)

itemTotal = len(featureList) + 1 #Sets itemTotal to the length of featureList +1

for i in range(P):
    selectedFeature = rollPack(featureList)
    outputString = outputString + selectedFeature + "\n\n"

print("Here is your character sheet!:\n\n" + outputString + "\n\nPress any key to exit.")
x = input()

createOutputFile(outputString,outputFile)