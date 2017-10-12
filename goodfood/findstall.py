#function for filtering and sorting stalls based of Canteen or Cuisine

import json

def findstall(option, choice):

    if (option == "Canteen"):
        #Canteen input of each rating is stored in the 1st column(index 0)
        select = "Food Location"
        #Cuisince tyoe of each rating is stored in the 2nd column(index 1)
        sel = "Cuisine"
    elif (option == "Cuisine"):
        #Cuisince tyoe of each rating is stored in the 2nd column(index 1)
        select = "Cuisine"
        #Canteen input of each rating is stored in the 1st column(index 0)
        sel = "Food Location"
              
    with open('reviews.json') as rev:
        data_as_list=[]
        try:
            reader = rev.read()
            data_as_list = json.loads(reader)
        except:
            pass
        
    counter = 0
    plist = []

    
    for i in range(0, len(data_as_list)):
        #find reviews of stalls matching selected canteen/cuisine
        if (data_as_list[i][select] == choice):
            plist.append(data_as_list[i])
        i = i + 1

    mlist = []

    with open('stalls.json') as f:
        reader = f.read()
        data_as = json.loads(reader)

    for i in range(0, len(data_as)):
        #find stalls matching selected canteen/cuisine
        if (data_as[i][select] == choice):
            mlist.append(data_as[i])
        i = i + 1


    #compute average ratings of particular store
    for i in range (0,len(mlist)):
        mlist[i]["Total Ratings"] = float(mlist[i]["Total Ratings"])
        mlist[i]["Amt. of reviewers"] = float(mlist[i]["Amt. of reviewers"])
        for k in range (0,len(plist)):
            #match each review to stall by checking both location and store name matches
            if ((mlist[i]["Food Location"] == plist[k]["Food Location"])&(mlist[i]["Food Stalls"] == plist[k]["Food Stalls"])):
                #add particular rating to overall rating of stall
                mlist[i]["Total Ratings"] = (mlist[i]["Total Ratings"]) + float(plist[k]["Ratings"])
                #increase number of people that rated for the particular stall
                mlist[i]["Amt. of reviewers"] = (mlist[i]["Amt. of reviewers"]) + 1
        #for stalls that people have rated on, we divide overall rating by number of people to obtain average ratings
        if(mlist[i]["Amt. of reviewers"] != 0):
            mlist[i]["Total Ratings"] = mlist[i]["Total Ratings"] / mlist[i]["Amt. of reviewers"]
    #sort the list of stalls by average rating in descending order
    sorted_mlist = sorted(mlist,key=lambda x: x["Total Ratings"],reverse=True)

    #output of function is a string containing list of stalls with info such as stall name, canteen, opening hours, cuisine and average ratings
    outmsg = "List of filtered Stalls (Highest rating to Lowest rating) \n \n" 

    for i in range (0,len(sorted_mlist)):
        outmsg = outmsg + "Stall Name: " + str(sorted_mlist[i]["Food Stalls"]) +"\n" + "Location: " + str(sorted_mlist[i]["Food Location"]) + "\n" + "Opening Hours: " + str(sorted_mlist[i]["Operating hours"])+ "\n" + "Cuisine: " + str(sorted_mlist[i]["Cuisine"]) + "\n" + "Avg Rating: " + str(sorted_mlist[i]["Total Ratings"]) + "\n \n"

    return(outmsg)
