#!/usr/bin/env python3

# Created by: Ethan Gravelle
# Created on: April 2021
# This calculates the circumference of a circle

import constants

def main ():
    #this function calculates the circumference
    #input
    radius = int(input("Enter radius of circle (mm): "))
    
    #process
    circumference = constants.TAU * radius
    
    #output
    print ("Circumference is {} mm².".format(circumference))
    print ("\nDone.")
    
if __name__ == "__main__":
    main()
