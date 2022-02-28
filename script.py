import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dfDict = pd.read_csv("dictionary.csv")
dfSummer = pd.read_csv("summer.csv")

conDict = {}
index = 0

countries = dfSummer["Country"]
medals = dfSummer["Medal"]

#dictionary with countries and each medal and amount
for country in countries:
    medal = medals[index]
    if country in conDict:
        if medal in conDict[country]:
            conDict[country][medal] += 1
        else:
            conDict[country].update({medal : 1})    
    else:
        conDict.update({country: {medal: 1}})
    index += 1

#country with highest total medal count
medalTotals = {}
for country in countries:
    if country in medalTotals:
        medalTotals[country] += 1
    else:
        medalTotals.update({country: 1})
#print(medalTotals)
highestCountry = max(medalTotals, key=medalTotals.get)
print(highestCountry,":", medalTotals[highestCountry])

        
print(conDict)

#sort dictionary
medalTotals = sorted(medalTotals.items(), key=lambda x:x[1])
sortdict = dict(medalTotals)
keysList = list(sortdict)

#top values
amount = int(input("\nHow many countries would you like to display?\n(Recommended <= 15)\n> "))
topValues = []
i = 1
index = 0
while i <= amount:
    topValues.append(keysList[len(keysList) - i])
    index += 1
    i += 1

print(topValues)


topTotals = []
for country in topValues:  
    topTotals.append(sortdict[country])
print(topTotals)

#seperate medal counts
bronzeCounts = []
silverCounts = []
goldCounts = []

for country in topValues:
    if "Gold" in conDict[country]:
        goldCounts.append(conDict[country]["Gold"])
    else:
        bronzeCounts.append(0)
        
    if "Silver" in conDict[country]:
        silverCounts.append(conDict[country]["Silver"])
    else:
        silverCounts.append(0)
        
    if "Bronze" in conDict[country]:
        bronzeCounts.append(conDict[country]["Bronze"])
    else:
        goldCounts.append(0)
        
#plotting

f = plt.figure()
graphCount = int(input("\nHow many graphs would you like? (Between 1-2):\n> "))

N = len(topValues)
ind = np.arange(N) 
width = .25

if graphCount == 2:
    plt.subplot(1, 2, 1)

plt.bar(ind, goldCounts, width, color = "#ffd700", edgecolor = "black", linewidth = 0.5, label='Gold')
plt.bar(ind + width, silverCounts, width, color = "#c0c0c0", edgecolor = "black", linewidth = 0.5, label='Silver')
plt.bar(ind + 2*width, bronzeCounts, width, color = "#cd7f32", edgecolor = "black", linewidth = 0.5, label='Bronze')
plt.gcf().set_size_inches(16, 9)

plt.ylabel('Medals')
plt.xlabel('Countries')
plt.title("Gold, Silver & Bronze Medals")
plt.xticks(ind + width / 3, (topValues))
plt.legend(loc='best')


if graphCount == 2:
    plt.subplot(1, 2, 2)
    plt.bar(topValues, topTotals, color ='#D972FF',
            edgecolor = "#8447FF", hatch = "x",
            width = 0.6)
    
    plt.title("Totals")
    plt.ylabel('Medals')
    plt.xlabel('Countries')

plt.show()

save = input("Would you like to save this graph to pdf?\n(Y\\N)\n> ")
if save.lower() == "y":
    filename = input("Please enter the name for your file:\n> ")
    f.savefig(filename + ".pdf", bbox_inches='tight')
elif lower(save) == "n":
    print("Shrimp")
else:
    print("Invalid Input - Graph not saved")