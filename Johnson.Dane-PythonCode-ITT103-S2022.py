#Author: Dane Johnson
#Date Created: Apr 16, 2022
#Course: ITT103 - Programming Techniques
#Purpose: This program collects sales data from a user, then calculates and #outputs commission for a sales person

#import necessary python packages
import os

#initialize and set variabes
sales_class = 0
sales_id = 0
crate = 0.0
rate = [0.04, 0.045, 0.06, 0.07, 0.10]

#define goodbye menu
def farewell():
    os.system("cls")
    print("=================JamEx Commission================")
    print("=================================================")
    print("=====================Farewell====================")
    print("=================================================\n")
    os.system("pause")
    quit()

#main menu/banner 
def mainMenu():
    os.system("cls")
    print("=================JamEx Commission================")
    print("This program exists to calculate sales commission")
    print("=================================================")
    print("==========Enter sales ID 1001 to exit============")
    print("========Sales class must be 1, 2, or 3===========")
    print("=================================================\n")

def outputDisplay(sales_id, commission):
    print("=================================================")
    print(" Sales ID  :  " + str(sales_id))
    print("Commission : $" + str(commission))    
    print("=================================================\n")

          

while sales_id != 1001:#pretest condition
    
    mainMenu()
    #accept sales data from user
    sales_id = int(input("Enter Sales ID: "))
    
    #check for exit parameter
    if sales_id == 1001:
        #salutation message    
        print("Thank You, Goodbye")
        os.system("cls")
        farewell()

        
    #resume data collection   
    sales = float(input("Enter Sales: "))
    sales_class = int(input("Enter Sales Class: "))
    
    #determine sales class entered
    if sales_class == 1:#class 1 commission ranges
        
        if sales <= 1000:
            crate = rate[2]
        elif sales > 1000 and sales <= 2000:
            crate = rate[3]
        elif sales > 2000:
            crate = rate[4]
        else:
            print("Invalid Sales Figure Entered!")
    elif sales_class == 2:#class 2 commission ranges
        
        if sales < 1000:
            crate = rate[0]
        elif sales >= 1000:
            crate = rate[2]
        else:
            print("Invalid Sales Figure Entered!")
    elif sales_class == 3:#class 3 commission
            crate = rate[1]
    else:
        print("Invalid Class Entered!")#invalid class error message
        os.system("pause")
        continue

    #calculate commission based on determined rate
    commission = sales * crate

    #display commission
    outputDisplay(sales_id, commission)
    os.system("pause")
