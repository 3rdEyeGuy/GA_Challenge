"""Bar graph of types of projects vs avg. funded percent (of successful campaigns)"""

#import classes and modules
import csv
import matplotlib.pyplot as plt
from scipy.stats import skew
import statistics
import collections

#assign csv file to a readable object
with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #skip headers 
    next(csv_reader)
    
    #init list and dict
    dataRaw = []
    data = []
    typeDict = {}
    types = []

    #append entire data set into a list
    for line in csv_reader:
        if line[6] == 'successful':
            dataRaw.append([int(line[0]),str(line[3]),float(line[9])])

    #close file object
    csv_file.close()

#Append only unique data into a list
for dataR in dataRaw:
    if dataR[0] in data:
        continue
    else: data.append([dataR[1],dataR[2]])

#creates a list of unique types
for typF in data:
    if typF[0] in types:
        continue
    else: types.append(typF[0])

#create a dict with campaign categories and funding percentages
for typ in types:
    fundPrcnt = []
    for fund in data:
        if typ == fund[0]:
            fundPrcnt.append(float(fund[1]))
    avgfundPrcnt = statistics.mean(fundPrcnt)
    typeDict[typ] = avgfundPrcnt 

#sort dict
typeDict = collections.OrderedDict(sorted(typeDict.items()))
print(typeDict) 

#create bar graph from dict
plt.bar(range(len(typeDict)), typeDict.values(), align = 'center')
plt.xticks(range(len(typeDict)), typeDict.keys())

#set bar graph title and labels
plt.ylabel('Average Funded Percent') 
plt.xlabel('Categories')
plt.title('The Average Funded Percents of Kickstarter Campaign Categories')

#show bar graph
plt.show()
