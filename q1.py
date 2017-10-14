"""Sifts through Kick-starter project data and prints the total pledge average"""

import csv

#assign csv file to a readable object
with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_obj = csv.reader(csv_file)
    
    #skip variable title
    next(csv_obj)

    #variable initialization
    Totpledge = 0
    count = 0

    #count total pledge for each project and number of projects
    for line in csv_obj:
        if line[8] is not '':
            Totpledge = int(line[8]) + Totpledge 
            count = count + 1

    #calculate average pledge amount
    avgPledge = Totpledge/count
    
    #print the average pledge amount
    print('The average amount pledged is $' + str(avgPledge))
     
