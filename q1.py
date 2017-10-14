import csv

#assign csv file to a readable object
with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_obj = csv.reader(csv_file)

    next(csv_obj)

    #print pledge for each project
    for line in csv_obj:
        print(line[8])

     
