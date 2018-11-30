################################################################################
#                           title-of-assignment                                #
#                                                                              #
# PROGRAMMER:       Alvaro Espinoza                                            #
# CLASS:            CG120                                                      #
# ASSIGNMENT:       Final Project                                              #
# INSTRUCTOR:       Dean Zeller                                                #
# TA:               Robert Carver                                              #
# SUBMISSION DATE:  Saturday, December 1,2018                                  #
#                                                                              #
# DESCRIPTION:                                                                 #
# Describe-the-program-implemented-in-your-own-words                           #
#                                                                              #
# COPYRIGHT:                                                                   #
# This program is (c) 2018 Alvaro Espinoza and Dean Zeller. This is original   #
# work, without use of outside sources.                                        #
#                                                                              #
# Pictures:                                                                    #
# http://funwithbonus.com/wp-content/uploads/apu-tyca-e1342877856253.jpg       #    
# https://www.makerbot.com/wp-content/uploads/2011/12/sad_cash_register.png    #
# https://fscomps.fotosearch.com/compc/CSP/CSP842/cartoon-police-car-stock-illustration__k8421966.jpg
#                                                                              #
################################################################################
import time 
import sys
from tkinter import *
import random
c = Canvas(width=2000, height=600, bg='white')
c.pack(expand=YES, fill=BOTH)
thankyou = PhotoImage(file="apu.gif")
register = PhotoImage(file="sad_cash_register.gif")
car = PhotoImage(file="car.gif")

class Calculator:

    #####################################################################
    # __init__                                                          #
    #                                                                   #
    # purpose:                                                          3
    #     - initialize the attributes to default values                 #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def __init__ (self):
        
        self.hundred = 10000
        self.fifty   = 5000
        self.twenty  = 2000
        self.ten     = 1000
        self.five    = 500
        self.one     = 100
        self.quarter = 25
        self.dime    = 10
        self.nickel  = 5
        self.penny   = 1

        self.cost0  = []
        self.cost   = 0
        self.cost1  = 0
        self.given  = 0
        self.given1 = 0
        self.itemdifference = 0

        self.remainder     = 0
        self.hundredchange = 0
        self.fiftychange   = 0
        self.twentychange  = 0
        self.tenchange     = 0
        self.fivechange    = 0
        self.onechange     = 0
        self.quarterchange = 0
        self.dimechange    = 0
        self.nickelchange  = 0
        self.pennychange   = 0

        self.change = 0.0

        self.pocketchange = 0
        


    #####################################################################
    # introduction                                                      #
    #                                                                   #
    # purpose:                                                          #
    #     - accept user input for user and study name                   #
    #     - display instructions for user                               #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def introduction(self):
        
        print("                         Welcome to Change Calulator!")
        print("")
        print("        This program will recieve two user inputs, one will be the cost")
        print("         of an item and the other will be the amount of money received.")
        print("")
        print("    The program will then calculate the amount of change that will be returned")
        print("   to the customer and tell the user how much of each dollar or coin is needed.")
        print()
        print()



    #####################################################################
    # gatherData                                                        #
    #                                                                   #
    # purpose:                                                          #
    #     - accept user input for the self.data attribute               #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def gatherData(self):


        print("To enter the data correctly, the program needs to know how many items are being purchased.")
        while(True):
            try:
                response=input("    Number of items => ")
                size=int(response)
                break
            except ValueError:
                print("   ",response,"is not an integer value")
                print("    Please enter an integer value.")
        print("    There are",size, "items.")
        print("")


        for i in range(size):
            while(True):
                try:
                    response=(input("What is the cost of item "+str(i)+("?   $")))
                    cost = float(response)
                    break
                except ValueError:
                    print()
                    print("   ",response,"is not a valid cost")
                    print("    Please enter the cost of the item.")
            print("    You entered: $",cost)
            self.cost0.append(cost)
        print()


    #####################################################################
    # calcSum                                                           #
    #                                                                   #
    # purpose:                                                          #
    #     - calculate and print the sum of self.data                    #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def calcSum(self):
        for n in self.cost0:
            self.cost += n
        cost1= str(round(self.cost, 2))
        print("Calculated sum ("+str(cost1)+")")

    
        self.cost1=self.cost*100
        print()


    #####################################################################
    # moredata                                                          #
    #                                                                   #
    # purpose:                                                          #
    #     - calculate and print the sum of self.data                    #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def moreData(self):
        
        while(True):
            try:
                response=input("How much money did the customer give? => $")
                self.given=float(response)
                break
            except ValueError:
                print()
                print("   ",response,"is not a valid dollar amount")
                print("    Please enter the amount of money given.")
        print("    You entered: $",self.given)
            

        self.given1=self.given*100
        print()

        self.itemdifference = self.given1-self.cost1


    #####################################################################
    # performCalculations                                               #
    #                                                                   #
    # purpose:                                                          #
    #     - perform all calculations, with appropriate header           #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def performCalculations(self):

        self.hundredchange=int(self.itemdifference/self.hundred)
        self.remainder=(self.itemdifference%self.hundred)
        self.fiftychange=int(self.remainder/self.fifty)
        self.remainder=(self.remainder%self.fifty)
        self.twentychange=int(self.remainder/self.twenty)
        self.remainder=(self.remainder%self.twenty)
        self.tenchange=int(self.remainder/self.ten)
        self.remainder=(self.remainder%self.ten)
        self.fivechange=int(self.remainder/self.five)
        self.remainder=self.remainder%self.five
        self.onechange=int(self.remainder/self.one)
        self.remainder=(self.remainder%self.one)
        self.quarterchange=int(self.remainder/self.quarter)
        self.remainder=(self.remainder%self.quarter)
        self.dimechange=int(self.remainder/self.dime)
        self.remainder=(self.remainder%self.dime)
        self.nickelchange=int(self.remainder/self.nickel)
        self.remainder=(self.remainder%self.nickel)
        self.pennychange=int(self.remainder/self.penny)
        
        self.change= str(round(self.given-self.cost, 2))


    #####################################################################
    # printReport                                                       #
    #                                                                   #
    # purpose:                                                          #
    #     - print a summary report of the study                         #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def printReport(self):

        if self.given > self.cost:
            print1= ["Calculating change."]
            for p in print1[0]:
                time.sleep(0.045) 
                sys.stdout.write(p)
                sys.stdout.flush()
            time.sleep(2)
            print("")
            print("")
            print("This is the amount of change owed to the customer: $",self.change)
            print("")
            horizline=("+---------------------------------+------------+")
            print(horizline)
            print("| %-13s %10s %10d |" % ("Benjamins(100 dollar):","|",self.hundredchange))
            print(horizline)
            print("| %-13s %14s %10d |" % ("Grants(50 dollar):","|",self.fiftychange))
            print(horizline)
            print("| %-13s %12s %10d |" % ("Jacksons(20 dollar):","|",self.twentychange))
            print(horizline)
            print("| %-13s %11s %10d |" % ("Hamiltons(10 dollar):","|",self.tenchange))
            print(horizline)
            print("| %-13s %13s %10d |" % ("Lincolns(5 dollar):","|",self.fivechange))
            print(horizline)
            print("| %-13s %12s %10d |" % ("Washingtons(Dollar):","|",self.onechange))
            print(horizline)
            print("| %-13s %6s %10d |" % ("Baby Washingtons(Quarter):","|",self.quarterchange))
            print(horizline)
            print("| %-13s %19s %10d |" % ("FDRs(Dime):","|",self.dimechange))
            print(horizline)
            print("| %-13s %13s %10d |" % ("Jeffersons(Nickel):","|",self.nickelchange))
            print(horizline)
            print("| %-13s %11s %10d |" % ("Baby Lincolns(Penny):","|",self.pennychange))
            print(horizline)

            print()
            import math
            change1= float(self.change)
            pocketchange=math.floor(change1)
            pocketchange1= str(round((change1*100)-(pocketchange*100), 2))
            pocketchange2= float(pocketchange1*1)
            if pocketchange2 < 0.01:
                print()
                print("Would you like to donate a dollar to the Pluto is a Planet Foundation?")
                answer = input("Please enter 'Yes' or 'No' => ")
                print()
                print("Sorry, that's the wrong answer. I'll be taking all your change, thanks for your support!")

                time.sleep(3)

                c.create_image(1000,100, image= thankyou, anchor=NW)
                c.create_image(500,100, image= thankyou, anchor=NW)
                c.create_image(0,100, image= thankyou, anchor=NW)

            else:
                
                print("Would you like to round down to the nearest dollar and donate",pocketchange1,"cents")
                print("to the Pluto is a Planet Foundation?")
                answer = input("Please enter 'Yes' or 'No' => ")
                print()
                print("Sorry, that's the wrong answer. I'll be taking all your change, thanks for your support!")

                time.sleep(3)

                c.create_image(1000,100, image= thankyou, anchor=NW)
                c.create_image(500,100, image= thankyou, anchor=NW)
                c.create_image(0,100, image= thankyou, anchor=NW)

                
        elif self.given < self.cost:
            print("Your customer does not have enough money to pay.")
            print1= [" Program will now contact the police!"]
            for p in print1[0]:
                time.sleep(0.045) 
                sys.stdout.write(p)
                sys.stdout.flush()
            time.sleep(2)

            c.create_image(1000,100, image= car, anchor=NW)
            c.create_image(500,100, image= car, anchor=NW)
            c.create_image(0,100, image= car, anchor=NW)


            
                
        else:
            print1= ["No change will be owed! >:( you took my purpose in life!"]
            for p in print1[0]:
                time.sleep(0.045) 
                sys.stdout.write(p)
                sys.stdout.flush()
            time.sleep(2)
            print()

            c.create_image(1000,0, image= register, anchor=NW)
            c.create_image(500,0, image= register, anchor=NW)
            c.create_image(0,0, image= register, anchor=NW)








    






