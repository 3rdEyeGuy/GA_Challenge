"""Plots relative freq hist of campaign durations for failed and successful campaigns"""

#import methods
import csv
import matplotlib.pyplot as plt
from scipy.stats import skew
import numpy as np

#assign csv file to a readable object
with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #skip headers 
    next(csv_reader)

    #init list
    dataRaw = []
    data = []
    durationF=[]
    durationS = []
    durationTot = []
    
    #init 30-35 duration count
    countF = 0
    countF30 = 0
    countS = 0
    countS30 = 0
    #append entire data set into a list
    for line in csv_reader:
        dataRaw.append([int(line[0]),str(line[6]),float(line[9]),float(line[16])])

    #close file object
    csv_file.close()

#append only unique data into duration list
for dataR in dataRaw:
    if dataR[0] in data:
        continue
    else: data.append([dataR[0],dataR[1],dataR[2],dataR[3]])

#create lists of total,failed and successful durations
for dt in data:
    durationTot.append(dt[3])
    if dt[1] == 'failed': 
        durationF.append(dt[3])
        countF += 1
        if 30 <= dt[3] < 35:
            countF30 += 1
    elif dt[1] == 'successful':
        durationS.append(dt[3])
        countS += 1
        if 30 <= dt[3] < 35:
            countS30 += 1

#calculates Pearson's skewness coefficient
skewF = round(skew(durationF), 3)
skewS = round(skew(durationS), 3)

#init bin size
incrmt = 5 
#init list of bins
bins = list(range(0, int(max(durationF)+incrmt), incrmt))
#convert to numpy arrays
durationTot_ar = np.array(durationTot)
durationF_ar = np.array(durationF)
durationS_ar = np.array(durationS)

#normalization weights
weightS = np.ones_like(durationS_ar)/float(len(durationS_ar)+len(durationF_ar))
weightF = np.ones_like(durationF_ar)/float(len(durationS_ar)+len(durationF_ar))

#create hists
plt.hist(durationS_ar,bins, histtype = 'bar', alpha = 0.5, weights = weightS, color = 'b', label = 'Successful campaigns')
plt.hist(durationF_ar,bins, histtype = 'bar', alpha = 0.5, weights = weightF, color = 'r', label = 'Failed campaigns')

#label hist
plt.ylabel('Relative Frequency') 
plt.xlabel('Campaign Duration (days)')
plt.title('Durations of Kickstarter Campaigns')
plt.grid()

#legend
plt.legend(loc='upper right')

#inserts skewness 1/2 way across x-axis and 3/4 up the y-axis
#transform allows me to create axes at which 1,1 marks the top right corner of plot
plt.text(0.4,0.81,r'Skew: {}'.format(skewS),transform=plt.gca().transAxes, color= 'b') 
plt.text(0.4,0.77,r'Skew: {}'.format(skewF),transform=plt.gca().transAxes, color= 'r') 

#show histogram
plt.show()
