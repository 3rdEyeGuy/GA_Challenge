"""Bar graph of types of projects vs avg. funded percent (of successful campaigns)"""

#import classes and modules
import csv
import matplotlib.pyplot as plt
from scipy.stats import skew
import statistics

#assign csv file to a readable object
with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #skip headers 
    next(csv_reader)
    
    #init list
    types = []

    typeDict = {}

    #append types for each project into a list
    for line in csv_reader:
        if line[6] == 'successful':
            if line[3] in types:
                continue
            else: types.append(str(line[3]))

    csv_file.close()
#assign csv file to a readable object
with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_reader = csv.reader(csv_file)

    for typ in types:
        print('typ loop:', typ)
        fundPrcnt = []
        for line in csv_reader:
            if line[6] == 'successful':
                if typ == str(line[3]):
                    fundPrcnt.append(float(line[9]))
        avgfundPrcnt = statistics.mean(fundPrcnt)
        typeDict[typ] = avgfundPrcnt 
        print(typeDict) 

    #close file object
    csv_file.close() 

#create histogram
plt.bar(range(len(typeDict)), typeDict.values(), align = 'center')
plt.xticks(range(len(typeDict)), typeDict.keys())

plt.ylabel('Average Funded Percent') 
plt.xlabel('Categories')
plt.title('The Average Funded Percents of Kickstarter Campaign Categories')

#show histogram
plt.show()
