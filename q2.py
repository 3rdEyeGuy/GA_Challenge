"""Creates a list of number of backers within bins of 100"""
#imports csv class
import csv

#assign csv file to a readable object
with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_obj = csv.reader(csv_file)
    
    #skip headers 
    next(csv_obj)

    #opens csv file to write 
    with open('backers_hist_data.csv', 'w') as hist_obj:
        hist_data = csv.writer(hist_obj)

        #count total pledge for each project and number of projects
        for line in csv_obj:
            if line[10] is not '':
                hist_data.writerow(int(line[10]))

        #close file object
        hist_obj.close()    

    #close file object
    csv_file.close() 
