"""Bar graph of types of projects vs avg. pledged (of successful campaigns)"""

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
            dataRaw.append([int(line[0]),str(line[3]),float(line[8])])

    #close file object
    csv_file.close()

#correct category typo
#append only unique data into a list
typo = 'Film &amp; Video'
correct = 'Film & Video'
for dataR in dataRaw:
    if dataR[1] == typo:
        dataR[1] = correct

    if dataR[0] in data:
        continue
    else: data.append([dataR[1],dataR[2]])

#creates a list of unique types
for typP in data:
    if typP[0] in types:
        continue
    else: types.append(typP[0])

#create a dict with campaign categories and pledges
for typ in types:
    pledge = []
    for pldg in data:
        if typ == pldg[0]:
            pledge.append(float(pldg[1]))
    avgpledge = statistics.mean(pledge)
    typeDict[typ] = avgpledge 

#sort dict
typeDict = collections.OrderedDict(sorted(typeDict.items()))
print(typeDict) 

#create bar graph from dict
plt.bar(range(len(typeDict)), typeDict.values(), align = 'center')
plt.xticks(range(len(typeDict)), typeDict.keys())

#set bar graph title and labels
plt.ylabel('Average Pledge ($)') 
plt.xlabel('Categories')
plt.title('The Average Pledges of Kickstarter Campaigns by Categories')

#show bar graph
plt.show()
