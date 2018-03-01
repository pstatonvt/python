#A program that takes in a list of numbers until you type "done," and then prints the raw and sorted list of numbers.

#Initialize a list
numlist = list()


while True:
    #Asks the user to enter a value until "done" is typed
    inp = input("Enter a value: ")
    #If 'done' is typed, it prints the raw list and sorted list
    if inp == 'done':
        print("Raw list:",numlist)
        numlist.sort()
        print("Sorted:",numlist)
        break
    #Converts the value from a str to int, and puts it in 'numlist.'
    try:
        value = int(inp)
        numlist.append(value)
    #If any letters or words other than 'done' are typed, outputs the error message and continues the loop
    except:
        print("Invalid input!")
        continue
    value = int(inp)
    numlist.append(value)
