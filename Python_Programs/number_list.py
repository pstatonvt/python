#A program that takes in a list of numbers until you type "done," and then prints the raw and sorted list of numbers.
import sys
#Initialize a list
numlist = list()

#Initialize file
outfile = open("output.txt",'w')

while True:
    #Asks the user to enter a value until "done" is typed
    inp = input("Enter a value: ")
    #If 'done' is typed, it prints the raw list and sorted list
    if inp == 'done':
        #Prints the raw list
        print("Raw list:",numlist)
        print("Raw list:",numlist,file=outfile)
        #Prints sorted list
        numlist.sort()
        print("Sorted:",numlist)
        print("Sorted:",numlist,file=outfile)
        #Prints average of numbers
        average = sum(numlist)/len(numlist)
        print("Average:",average)
        print("Average:",average,file=outfile)
        #Prints sum of the list
        print("Sum:",sum(numlist))
        print("Sum:",sum(numlist),file=outfile)
        #Prints the maximum value
        print("Maximum:",max(numlist))
        print("Maximum:",max(numlist),file=outfile)
        #Prints the minimum value
        print("Minimum:",min(numlist))
        print("Minimum:",min(numlist),file=outfile)
        break
    #Converts the value from a str to int, and puts it in 'numlist.'
    try:
        value = int(inp)
        numlist.append(value)
    #If any letters or words other than 'done' are typed, outputs the error message and continues the loop
    except:
        print("Invalid input!")
        continue
