"""histogram of pledge goals vs for failed campaigns"""

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
    dataRaw = []
    data = []
    pledgeGoal=[]

    #append entire data set into a list
    for line in csv_reader:
        dataRaw.append([int(line[0]),str(line[6]),float(line[7])])

    #close file object
    csv_file.close()

#append only unique data into pledgeGoal list
for dataR in dataRaw:
    if dataR[0] in data:
        continue
    else: data.append([dataR[0],dataR[1],dataR[2]])

for dt in data:
    if dt[1] == 'failed': 
        pledgeGoal.append(dt[2])
        
#calculates Pearson's skewness coefficient
skew = skew(pledgeGoal)

#init bin size
incrmt = 2500
#init list of bins
bins = list(range(0, int(max(pledgeGoal)+incrmt), incrmt))

#create histogram
plt.hist(pledgeGoal,bins, histtype='bar',rwidth=1.0)
plt.ylabel('Number of Campaigns') 
plt.xlabel('Pledge Goals ($)')
plt.title('Pledge Goals of Failed Kickstarter Campaigns')

#inserts skewness 1/2 way across x-axis and 3/4 up the y-axis
#transform allows me to create axes at which 1,1 marks the top right corner of plot
plt.text(0.5,0.75,r'Skew ={}'.format(skew),transform=plt.gca().transAxes) 

#show histogram
plt.show()


