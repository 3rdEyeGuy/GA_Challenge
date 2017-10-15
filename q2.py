"""Creates a list of number of backers within bins of 100"""
#imports csv class
import csv

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


