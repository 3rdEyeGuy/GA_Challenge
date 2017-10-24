"""Plots hist of campaign durations for failed campaigns"""

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
    duration=[]

    #init 30-35 duration count
    count = 0
    count30 = 0
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

for dt in data:
    if dt[1] == 'failed': 
        duration.append(dt[3])
        count += 1
        if 30 <= dt[3] < 35:
            count30 += 1

#calculates Pearson's skewness coefficient
skew = round(skew(duration), 3)

#init bin size
incrmt = 5 
#init list of bins
bins = list(range(0, int(max(duration)+incrmt), incrmt))
duration_ar = np.array(duration)
#create histogram
weights = np.ones_like(duration_ar)/float(len(duration_ar))
plt.hist(duration_ar,bins, histtype = 'bar', alpha = 1, weights = weights)

#y-axis scale mod
###plt.gca().set_ylim([0,8500])

#label hist
plt.ylabel('Relative Frequency') 
plt.xlabel('Campaign Duration (days)')
plt.title('Durations of Failed Kickstarter Campaigns')

#inserts skewness 1/2 way across x-axis and 3/4 up the y-axis
#transform allows me to create axes at which 1,1 marks the top right corner of plot
plt.text(0.4,0.75,r'Skew: {}'.format(skew),transform=plt.gca().transAxes) 
plt.text(0.4,0.70,r'Campaigns running 30-34 days: {}'.format(count30),transform=plt.gca().transAxes) 
plt.text(0.4,0.65,r'Total campaigns: {}'.format(count),transform=plt.gca().transAxes) 
#show histogram
plt.show()


