#Name: Zane Huey
#Purpose: To parse through a CSV and extract various statistics

#Imports the math library to make rounding down simpler
import math

#Open the CSV file for reading
file = open("titanic.csv")

#Skip the row with all the headers
next(file)

#Declare your variables here before the loop
#Variable to track the number of total survivors
NumSurvivors = 0
#Variable to track the number of total first class survivors
FirstClassSurvivors = 0
#Variable to track the number of male survivors
MaleSurvivors = 0
#Variable to track the number of passengers with the title of miss
NumMiss = 0
#Variable to hold the name of the oldest passenger
OldestPassenger = ""
#Variable to hold the age of the oldest passenger
MaximumAge = 0.0
#Variable to hold the name of the passenger who paid the highest fare and didn't survive
MaxTicketNotSurvivor = ""
#Variable to hold the highest fare paid by someone who didn't survived
MaximumFare = 0.0
#Variable to track the number of passengers who paid 0 pounds for their fare
NumZeroFare = 0
#List to hold the names of all passengers who paid 0 pounds for their fare
ZeroFareList = []
#Variable to hold the combined ages of all passengers
TotalAge = 0.0
#Variable to keep track of how many passengers there are
TotalPassengers = 0
#List to hold the fares of all passengers on board
AllFares = []
#List to hold the sorted and unique fare values
UniqueFares = []
#Dictionary to hold all passengers by using their age as a key
PassengerDict = {}
#Variable to hold the age of the current passenger
CurrentAge = 0

#For each line in the file...
for line in file:
    #...split that line into a row by the commas.
    #We can now get each individual piece of data for the row by indexing
    #   it with row[#]
    row = line.strip().split(",")
    
    #1
    #Parses through the CSV and checks if a passenger survived
    if row[0] == "1":
        #Increases the survivor count by 1
        NumSurvivors += 1

    #2
    #Parses through the CSV and checks if a passenger survived and is first class
    if row[0] == "1" and row[1] == "1":
        #Increases the number of first class survivors by 1
        FirstClassSurvivors += 1
    
    #3
    #Parses through the CSV and checks if a passenger survived and is male
    if row[0] == "1" and row[3] == "male":
        #Increases the number of male survivors by 1
        MaleSurvivors += 1
    
    #4
    #Parses through the CSV and checks if a passenger had the title of miss
    if "Miss" in row[2]:
        #Increases the number of passengers with the title of miss by 1
        NumMiss += 1
    
    #5
    #Parses through the CSV and checks if a passenger is older than the current highest age
    if float(row[4]) > MaximumAge:
        #Sets the current passenger's age as the highest current age
        MaximumAge = float(row[4])
        #Sets the current passenger's name as the name of the oldest person aboard the ship
        OldestPassenger = row[2]
    
    #6
    #Parses through the CSV and checks if a passenger didn't survive and paid more than the current highest fare
    if row[0] ==  "0" and float(row[7]) > MaximumFare:
        #Sets the current passenger's fare as the highest fare paid
        MaximumFare = float(row[7])
        #Sets the current passenger's name as the name of the person that paid the highest fare
        MaxTicketNotSurvivor = row[2]

    #7
    #Parses through the CSV and checks if a passenger paid 0 pounds for their fare
    if row[7] == "0":
        #Increases the number of people who paid nothing for their fare by 1
        NumZeroFare += 1
        #Appends the name of the current passenger to a list of all passengers that paid nothing for their fare
        ZeroFareList.append(row[2])

    #8
    #Parses through the CSV and checks if a passenger survived, adds their age to the total, and increases the number of total passengers by 1
    if row[0] == "1":
        #Increases the total age by the current passenger's age
        TotalAge += float(row[4])
        #Increases the total number of passengers by 1
        TotalPassengers += 1
    

    #9
    #Parses through the CSV and appends the passenger's fare to the list
    AllFares.append(float(row[7]))
    

    #10
    #Parses through the CSV, sets age as the current passenger's age,  checks if that age is a key in the dictionary, and appends the name to that key in the dictionary
    #If age isn't a key in the dictionary, a key of the same value is created and then the name is appended to that key in the dictionary
    #Sets age as the current passenger's age
    Age = math.floor(float(row[4]))
    #Checks if the age is already a key in the dictionary
    if Age not in PassengerDict:
        #Creates a list using age as the key
        PassengerDict[Age]  = []
    #Appends the passenger's name to the corresponding key
    PassengerDict[Age].append(row[2])

#### THE LOOP ENDS HERE #####
    
#1. Print the number of survivors
print("The number of survivors is:", NumSurvivors, "\n")

#2. Print the number of first class survivors
print("The number of first class survivors is:", FirstClassSurvivors, "\n")

#3. Prints the number of male survivors
print("The number of male survivors is:", MaleSurvivors, "\n")

#4. Prints the number of passengers who have the title miss
print("The number of passengers with the title of Miss is:", NumMiss, "\n")

#5. Prints the name and age of the oldest passenger
print("The oldest passenger is:", OldestPassenger)
print("Their age is:", MaximumAge, "\n")

#6. Prints the most expensive ticket bought by someone who didn't survive. Also prints their name
print("The most expensive ticket purchased by someone who didn't survive is:", MaximumFare)
print("The ticket holder's name is:",  MaxTicketNotSurvivor, "\n")

#7. Prints the number of passengers who paid 0 pounds for their fare. Also prints their names
print("The number of passengers who paid 0 pounds for their fare:", NumZeroFare)
print("Their names are:", ZeroFareList, "\n")

#8. Prints the average age of all passengers who survived
print("The average age of all survivors is:", round(TotalAge / TotalPassengers, 2), "\n")

#9. Converts the list into a set to remove duplicate values before converting it back into a list
UniqueFares = list(set(list(AllFares)))
#Rounds each list item to the nearest whole number
UniqueFares = [round(x) for x in UniqueFares]
#Prints the list of unique fares
print("The unique fares are:", UniqueFares, "\n")

#10. Prints the list of passengers who were age 10
print(PassengerDict[10])

file.close()
 

