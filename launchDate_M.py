"""histogram of successful campaigns for each month"""

#import classes and modules
import csv
import matplotlib.pyplot as plt
from scipy.stats import skew
from datetime import datetime

#assign csv file to a readable object
with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #skip headers 
    next(csv_reader)

    #init list
    dataRaw = []
    data = []
    date=[]
    dateReq = []
    months = []

    #append entire data set into a list
    for line in csv_reader:
        dataRaw.append([int(line[0]),str(line[6]),str(line[11])])

    #close file object
    csv_file.close()

#append only unique data into date list
for dataR in dataRaw:
    if dataR[0] in data:
        continue
    else: data.append([dataR[0],dataR[1],dataR[2]])

for dt in data:
    if dt[1] == 'successful': 
        dateSplit =  dt[2].split()
        datePre = [dateSplit[2],dateSplit[1],dateSplit[-2]]
        datePost = datetime.strptime(datePre[0],'%b').month
        dateReq.append([datePost,int(dateSplit[1]),dateSplit[-2]])

for mt in dateReq:
    months.append(mt[0])

#calculates Pearson's skewness coefficient
skew = skew(months)

#init bin size
incrmt = 1
#init list of bins
bins = list(range(1,14))

#create histogram
plt.hist(months,bins, histtype='bar',rwidth=1.0)
plt.ylabel('Number of Campaigns') 
plt.xlabel('Month of Launch')
plt.title('Monthly Launches of Successful Kickstarter Campaigns')
plt.grid()

#inserts skewness 1/2 way across x-axis and 3/4 up the y-axis
#transform allows me to create axes at which 1,1 marks the top right corner of plot
plt.text(0.5,0.75,r'Skew ={}'.format(skew),transform=plt.gca().transAxes) 

#show histogram
plt.show()


