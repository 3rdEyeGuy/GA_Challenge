"""Creates a list of backers per project and displays a histogram of that data"""
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
    backers=[]
    data=[]

    #append entire data set into a list
    for line in csv_reader:
        dataRaw.append([int(line[0]),int(line[10])])

    #close file object
    csv_file.close()

#append only unique data into backers list
for dataR in dataRaw:
    if dataR[0] in data:
        continue
    elif dataR[1] is not '': 
        data.append([dataR[0],dataR[1]])

for dt in data:
    backers.append(dt[1])

#calculates Pearson's skewness coefficient
skew = skew(backers)

#init bin size
incrmt = 100
#init list of bins
bins = list(range(0, max(backers)+incrmt, incrmt))

#create histogram
plt.hist(backers,bins, histtype='bar',rwidth=1.0)
plt.ylabel('Frequency')
plt.xlabel('Backers')
plt.title('Kickstarter Campaign Backers')

#inserts skewness 1/2 way across x-axis and 3/4 up the y-axis
#transform allows me to create axes at which 1,1 marks the top right corner of plot
plt.text(0.5,0.75,r'Skew ={}'.format(skew),transform=plt.gca().transAxes) 

#show histogram
plt.show()


