#function for filtering and sorting stalls based of Canteen or Cuisine
import csv

def findstall(option, choice):

    if (option == "Canteen"):
        #Canteen input of each rating is stored in the 1st column(index 0)
        select = 0
        #Cuisince tyoe of each rating is stored in the 2nd column(index 1)
        sel = 1
    elif (option == "Cuisine"):
        #Cuisince tyoe of each rating is stored in the 2nd column(index 1)
        select = 1
        #Canteen input of each rating is stored in the 1st column(index 0)
        sel = 0
              
    with open('reviews.csv') as f:
        reader = csv.reader(f)
        data_as_list = list(reader)

    counter = 0
    plist = []

    for i in range(0, len(data_as_list)):
        #find reviews of stalls matching selected canteen/cuisine
        if (data_as_list[i][select] == choice):
            plist.append([])
            plist[counter]=(data_as_list[i])
            counter = counter + 1
        i = i + 1

    counter = 0
    mlist = []

    with open('stalls.csv') as f:
        reader = csv.reader(f)
        data_as = list(reader)

    for i in range(0, len(data_as)):
        #find stalls matching selected canteen/cuisine
        if (data_as[i][select] == choice):
            mlist.append([])
            mlist[counter]=(data_as[i])
            counter = counter + 1
        i = i + 1


    #compute average ratings of particular store
    for i in range (0,len(mlist)):
        mlist[i][4] = float(mlist[i][4])
        mlist[i][5] = float(mlist[i][5])
        for k in range (0,len(plist)):
            #match each review to stall by checking both location and store name matches
            if ((mlist[i][sel] == plist[k][sel])&(mlist[i][2] == plist[k][2])):
                #add particular rating to overall rating of stall
                mlist[i][4] = (mlist[i][4]) + float(plist[k][3])
                #increase number of people that rated for the particular stall
                mlist[i][5] = (mlist[i][5]) + 1
        #for stalls that people have rated on, we divide overall rating by number of people to obtain average ratings
        if(mlist[i][5] != 0):
            mlist[i][4] = mlist[i][4] / mlist[i][5]
    #sort the list of stalls by average rating in descending order
    sorted_mlist = sorted(mlist,key=lambda x: x[4],reverse=True)

    #output of function is a string containing list of stalls with info such as stall name, canteen, opening hours, cuisine and average ratings
    outmsg = "List of filtered Stalls (Highest rating to Lowest rating) \n \n" 

    for i in range (0,len(sorted_mlist)):
        outmsg = outmsg + "Stall Name: " + str(sorted_mlist[i][2]) +"\n" + "Location: " + str(sorted_mlist[i][0]) + "\n" + "Opening Hours: " + str(sorted_mlist[i][3])+ "\n" + "Cuisine: " + str(sorted_mlist[i][1]) + "\n" + "Avg Rating: " + str(sorted_mlist[i][4]) + "\n \n"

    return(outmsg)
