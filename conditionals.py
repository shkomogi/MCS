#Create a Generation Decider app

#Ask user for year of birth. Based on that ~ determine what generation the user falls in

YOB = int(input("What is your year of birth?\n"))
if YOB >= 2013 and YOB <=2025:
    print("You are Gen Alpha")

elif YOB >= 1997 and YOB <=2012:
    print("You are Gen Z")

elif YOB >=1981 and YOB <=1996:
    print("You are Gen Millenial")

elif YOB >=1965 and YOB <=1980:
    print("You are Gen X")

elif YOB >=1946 and YOB <=1964:
    print("You are Baby Boomers")

else:
    print("Invalid option")



