#Using MAP function ----------------------------------
#Step 1 - Create an empty list 
#Step 2 - Append some user input values to it (values must be in meters)
#Step 3 - Use lambda function to convert meter to kilometer
#Step 4 - Map lambda function to the list created
#Step 5 - use for loop to iterate list and print out list of values in Kilometer

meterValues = []
vals_to_add = range(1, 6)
for item in vals_to_add:
    userinput = int(input("Enter value in meters\n"))
    meterValues.append(userinput)

#append user's input to list and iterate using for loop to print

for i in meterValues:
    km = list(map(lambda x:x/1000,meterValues))
print(km," km")
    
