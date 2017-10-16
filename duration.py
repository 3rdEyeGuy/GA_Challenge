"""Plots scatterplot of durations vs pledge amounts for failed campaigns"""

#import classes and modules
import csv
import matplotlib.pyplot as plt
from scipy.stats import skew

#assign csv file to a readable object
with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #skip headers 
    next(csv_reader)
    
    #init list
    duration = []
    pledge = [] 

    #append duration for each project into a list
    for line in csv_reader:
        if line[6] == 'failed':
            duration.append(float(line[16]))
            pledge.append(int(line[8]))

    #close file object
    csv_file.close() 

#calculates Pearson's skewness coefficient
###skew = skew(duration)

#init bin size
###incrmt = 5 
#init list of bins
###bins = list(range(0, int(max(duration)+incrmt), incrmt))

#create histogram
plt.scatter(duration,pledge)
plt.ylabel('Pledge Amount ($)')
plt.xlabel('Campaign Duration (days)')
plt.title('Durations vs. Pledge Amounts of Failed Kickstarter Campaigns')

#inserts skewness 1/2 way across x-axis and 3/4 up the y-axis
#transform allows me to create axes at which 1,1 marks the top right corner of plot
###plt.text(0.5,0.75,r'Skew ={}'.format(skew),transform=plt.gca().transAxes) 

#show histogram
plt.show()
