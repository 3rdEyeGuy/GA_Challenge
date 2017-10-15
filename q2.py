"""Creates a list of number of backers within bins of 100"""
#imports csv class
import csv

#assign csv file to a readable object
with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_obj = csv.reader(csv_file)
    
    #skip headers 
    next(csv_obj)

    #variable initialization
    backers = [] 

    #count total pledge for each project and number of projects
    for line in csv_obj:
        if line[10] is not '':
            backers.append(int(line[10]))

    #close file object
    csv_file.close() 

#opens csv file to write 
with open('backers_hist_data.csv', 'w') as hist_obj:
    hist_data = csv.writer(hist_obj,delimiter=',')
    
    #init variables
    frq = 0
    bin_ct = 100
    hist_list = []

    #init bin range variables
    a = 0
    b = bin_ct

    #Until the bin range encompasses the largest number of backers
    #sift through the data for each bin range and append the "bin,frequency" to
    #a csv file
    while (b-bin_ct) <= max(backers):
        #init bin range
        rng = list(range(a,b+1))

        #sift through every point within each bin and update the frequency
        #for the number of backers within each bin
        for line in backers:
            if rng[0] <= line <= rng[-1]:
                frq = frq + 1

        #append "bin,frequency" to a list 
        hist_list.append([b,frq])

        #resets frequency counter
        frq = 0
        
        #update the bin range for next frequency count
        if a == 0:
            a = a + bin_ct + 1
            b = b + bin_ct
        elif a != 0:
            a = a + bin_ct
            b = b + bin_ct

    #append hist_list values to csv file
    hist_data.writerow(['project_backers', 'frequency'])
    for bin in hist_list:
        hist_data.writerow(bin)

    #close file object
    hist_obj.close() 
