#function that writes user ratings of stores into a file

import json

def rate(can, stall, rating, userid):

    with open('reviews.json','r') as f:
        data_as_list = []
        try:
            reader = f.read()
            data_as_list = (json.loads(reader))
        except:
            pass

    with open('stalls.json','r') as f:
        reader = f.read()
        data_as = json.loads(reader)
    
    plist = []
    check = 1

    #user validation. check that for the selected stall from the selected canteen, the user do not already have a previous rating
    for i in range(0, len(data_as_list)):
        if ((data_as_list[i]["Food Location"] == can) & (data_as_list[i]["Food Stalls"] == stall) & (data_as_list[i]["Chat ID"] == userid)):
            check = 0
            
    #if user passes validation test, we allow ratings to be stored into file
    if (check):
        #find the cuisine type and operating hours of selected stall from selected canteen
        for i in range(0, len(data_as)):
            if ((data_as[i]["Food Location"] == can) & (data_as[i]["Food Stalls"] == stall)):
                cuisine = data_as[i]["Cuisine"]
                hours = data_as[i]["Operating hours"]
        #add all relevant data(canteen, cuisine, stall name, user rating, user id) into existing file
        row = {"Food Location":can, "Cuisine":cuisine, "Food Stalls":stall, "Ratings":rating, "Chat ID":userid}
        data_as_list.append(row)
        with open('reviews.json','w') as f:
            json.dump(data_as_list,f)
        return("Thank you, your rating has been recorded!")
    #if user validation fail, as user already had a previous rating for selected stall, output of the function is a string informing the user of his error
    else:
        return("You have already entered rating for this stall. Multiple ratings are not allowed!")
            
