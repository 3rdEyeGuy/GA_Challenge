"""histogram of goal goals vs for failed campaigns"""

#import classes and modules
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
    goalF=[]
    goalS=[]

    #append entire data set into a list
    for line in csv_reader:
        dataRaw.append([int(line[0]),str(line[6]),float(line[7])])

    #close file object
    csv_file.close()

#append only unique data into goalF list
for dataR in dataRaw:
    if dataR[0] in data:
        continue
    else: data.append([dataR[0],dataR[1],dataR[2]])

#create lists of total,failed and successful goals
for dt in data:
    if dt[1] == 'failed': 
        goalF.append(dt[2])
    elif dt[1] == 'successful':
        goalS.append(dt[2])

#calculates Pearson's skewness coefficient
skewF = round(skew(goalF), 3)
skewS = round(skew(goalS), 3)

#init bin size
incrmt = 2500
#init list of bins
bins = list(range(0, int(max(goalS)+incrmt), incrmt))

#convert to numpy arrays
goalF_ar = np.array(goalF)
goalS_ar = np.array(goalS)

#normalization weights
weightS = np.ones_like(goalS_ar)/float(len(goalS_ar)+len(goalF_ar))
weightF = np.ones_like(goalF_ar)/float(len(goalS_ar)+len(goalF_ar))

#create hists
plt.hist(goalS_ar,bins, histtype = 'bar', alpha = 0.5, weights = weightS, color = 'b', label = 'Successful campaigns')
plt.hist(goalF_ar,bins, histtype = 'bar', alpha = 0.5, weights = weightF, color = 'r', label = 'Failed campaigns')

#label hist
plt.ylabel('Relative Frequency') 
plt.xlabel('Pledge Goals ($)')
plt.title('Pledge Goals of Kickstarter Campaigns')
plt.grid()

#legend
plt.legend(loc='upper right')

#inserts skewness 1/2 way across x-axis and 3/4 up the y-axis
#transform allows me to create axes at which 1,1 marks the top right corner of plot
plt.text(0.4,0.81,r'Skew: {}'.format(skewS),transform=plt.gca().transAxes, color= 'b') 
plt.text(0.4,0.77,r'Skew: {}'.format(skewF),transform=plt.gca().transAxes, color= 'r') 

#show histogram
plt.show()
