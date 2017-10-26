"""Bar graph of types of projects vs med. pledges (of successful campaigns)"""

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
    else: data.append([dataR[0],dataR[1],dataR[2]])

#creates a list of unique types
for typF in data:
    if typF[1] in types:
        continue
    else: types.append(typF[1])

#create a dict with campaign categories and funding percentages
for typ in types:
    pledge = []
    for pl_typ in data:
        if typ == pl_typ[1]:
            pledge.append(int(pl_typ[2]))
    medpledge = statistics.median(pledge)
    typeDict[typ] = medpledge 

#sort dict
typeDict = collections.OrderedDict(sorted(typeDict.items()))
print(typeDict) 

#create bar graph from dict
plt.bar(range(len(typeDict)), typeDict.values(), align = 'center')
plt.xticks(range(len(typeDict)), typeDict.keys())

#set bar graph title and labels
plt.ylabel('Median Pledge Amounts ($)') 
plt.xlabel('Categories')
plt.title('The Median Pledge Amounts for Successful Kickstarter Campaigns by Categories')

#show bar graph
plt.show()
