"""Creates a list of duration per project and displays a histogram of that data"""
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
    dataRaw = []
    data=[]
    duration=[]

    #append entire data set into a list
    for line in csv_reader:
        dataRaw.append([int(line[0]),float(line[16])])

    #close file object
    csv_file.close()

#append only unique data into duration list
for dataR in dataRaw:
    if dataR[0] in data:
        continue
    elif dataR[1] is not '': 
        data.append([dataR[0],dataR[1]])

for dt in data:
    duration.append(dt[1])

#calculates Pearson's skewness coefficient
skew = skew(duration)

#init bin size
incrmt = 5
#init list of bins
bins = list(range(0, int(max(duration)+incrmt), incrmt))

#create histogram
plt.hist(duration,bins, histtype='bar',rwidth=1.0)
plt.ylabel('Frequency')
plt.xlabel('Duration')
plt.title('Kickstarter Campaign Durations')

#inserts skewness 1/2 way across x-axis and 3/4 up the y-axis
#transform allows me to create axes at which 1,1 marks the top right corner of plot
plt.text(0.5,0.75,r'Skew ={}'.format(skew),transform=plt.gca().transAxes) 

#show histogram
plt.show()
print('The \'duration\' variable is NOT normally distributed.')
print('The skew is to the right at:',str(round(skew,2)))
