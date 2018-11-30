################################################################################
#                   Calculator Tester                                          #
#                                                                              #
# PROGRAMMER:       Alvaro Espinoza                                            #
# CLASS:            CG120                                                      #
# ASSIGNMENT:       Final Project                                              #
# INSTRUCTOR:       Dean Zeller                                                #
# TA:               Robert Carver                                              #
# SUBMISSION DATE:  Saturday, December 1, 2018                                 #
#                                                                              #
# DESCRIPTION:                                                                 #
# This program is the tester for the Change Calculator. It creates a study     #
# and prints the report.                                                       #
#                                                                              #
# COPYRIGHT:                                                                   #
# This program is (c) 2018 Alvaro Espinoza and Dean Zeller. This is original   #
# work, without use of outside sources.                                        #
################################################################################
from ChangeCalculator import Calculator

study1 = Calculator()
study1.introduction()
study1.gatherData()
study1.calcSum()
study1.moreData()
study1.performCalculations()
study1.printReport()
