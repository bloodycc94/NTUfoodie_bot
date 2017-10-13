#function that writes user ratings of stores into a file

import csv

def rate(can, stall, rating, userid):

    with open('reviews.csv') as f:
        reader = csv.reader(f)
        data_as_list = list(reader)

    with open('stalls.csv') as f:
        reader = csv.reader(f)
        data_as = list(reader)
    
    i,counter = 0,0
    plist = []
    check = 1

    #user validation. check that for the selected stall from the selected canteen, the user do not already have a previous rating
    for i in range(0, len(data_as_list)):
        if ((data_as_list[i][0] == can) & (data_as_list[i][2] == stall) & (data_as_list[i][4] == userid)):
            check = 0
    #if user passes validation test, we allow ratings to be stored into file
    if (check):
        #find the cuisine type and operating hours of selected stall from selected canteen
        for i in range(0, len(data_as)):
            if ((data_as[i][0] == can) & (data_as[i][2] == stall)):
                food = data_as[i][1]

        with open('reviews.csv','a', newline='') as f:
            writer = csv.writer(f)
            #add all relevant data(canteen, cuisine, stall name, user rating, user id) into existing file
            row = [[can] + [food] + [stall] + [rating] + [userid]]
            writer.writerows(row)
            #output of function is string informing user that his inputs have been recorded
            return("Thank you, your rating has been recorded!")
    #if user validation fail, as user already had a previous rating for selected stall, output of the function is a string informing the user of his error
    else:
        return("You have already entered rating for this stall. Multiple ratings are not allowed!")
            
