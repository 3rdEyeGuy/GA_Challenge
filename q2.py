"""Creates a list of backers per project and displays a histogram of that data"""
import csv
import matplotlib.pyplot as plt

#assign csv file to a readable object
with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #skip headers 
    next(csv_reader)
    
    #init list
    backers = []

    #append backers for each project to a list
    for line in csv_reader:
        if line[10] is not '':
            backers.append(int(line[10]))
    
    #close file object
    csv_file.close() 

#init bin size
incrmt = 100
#init list of bins
bins = list(range(0, max(backers)+incrmt, incrmt))

#create histogram
plt.hist(backers,bins, histtype='bar',rwidth=1.0)
plt.ylabel('Frequency')
plt.xlabel('Backers')
plt.title('Histogram of Backers')

#show histogram
plt.show()
