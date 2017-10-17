"""Sifts through Kick-starter project data and prints the total pledge mean"""
import csv
import statistics

#assign csv file to a readable object
with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #skip headers 
    next(csv_reader)

    #init list of pledges
    pledge=[]

    #init list and dict
    dataRaw = []
    data = []


    #append entire data set into a list
    for line in csv_reader:
        dataRaw.append([int(line[0]),str(line[8])])

    #close file object
    csv_file.close()

    #append only unique data into a list
    for dataR in dataRaw:
        if dataR[0] in data:
            continue
        else: data.append([dataR[0],dataR[1]])

    #create list for total pledge of each project
    for line in data:
        if line[1] is not '':
            pledge.append(int(line[1]))

    mean = statistics.mean(pledge)
    #print the average pledge amount
    print('The mean amount pledged was $' + str(mean))

