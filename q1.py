"""Sifts through Kick-starter project data and prints the total pledge mean"""
import csv
import statistics

#assign csv file to a readable object
with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_obj = csv.reader(csv_file)
    
    #skip variable title
    next(csv_obj)

    #init list of pledges
    pledge=[]

    #create list for total pledge of each project
    for line in csv_obj:
        if line[8] is not '':
            pledge.append(int(line[8]))

    mean = statistics.mean(pledge)
    #print the average pledge amount
    print('The mean amount pledged was $' + str(mean))

    #close file object
    csv_file.close()
