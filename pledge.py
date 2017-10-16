"""Plots scatterplot of pledge goals vs funded percent of successful campaigns"""

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
    pledgeGoal = []

    #append pledgeGoal for each project into a list
    for line in csv_reader:
        if line[6] == 'successful':
            pledgeGoal.append(float(line[7]))

    #close file object
    csv_file.close() 

#calculates Pearson's skewness coefficient
skew = skew(pledgeGoal)

#init bin size
incrmt = 1000
#init list of bins
bins = list(range(0, int(max(pledgeGoal)+incrmt), incrmt))

#create histogram
plt.hist(pledgeGoal,bins, histtype='bar',rwidth=1.0)
plt.ylabel('Number of Campaigns') 
plt.xlabel('Pledge Goals ($)')
plt.title('Pledge Goals of Successful Kickstarter Campaigns')

#inserts skewness 1/2 way across x-axis and 3/4 up the y-axis
#transform allows me to create axes at which 1,1 marks the top right corner of plot
plt.text(0.5,0.75,r'Skew ={}'.format(skew),transform=plt.gca().transAxes) 

#show histogram
plt.show()
