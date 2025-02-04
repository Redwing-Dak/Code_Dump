#Variable to receive a number between 1 and 100 from the user
NumberToGuess = input("Please enter a number between 1 and 100 for me to guess: ")
#Converting the user's number into an integer for future use
NumberToGuess = int(NumberToGuess)
#While loop to make sure the user enters a number within the range
while NumberToGuess > 100 or NumberToGuess < 1:
    #Variable to receive a number between 1 and 100 from the user
    NumberToGuess = input("Enter a number between 1 and 100: ")
    #Converting the user's number into an integer for future use
    NumberToGuess = int(NumberToGuess)

#Variable to hold the lowest number still within the range
Min = 1
#Variable to hold the highest number still within the range
Max = 100
#Sets the computer's first guess as the average of the minimum and maximum
ComputerGuess = (Min + Max) // 2

#Print statement assuring the user that the computer doesn't know what to guess
print("I promise I didn't peek... now let's see.")

#Variable to hold the total number of guesses the computer makes
GuessCounter = 0
#While loop that runs until the computer guesses the user's number
while ComputerGuess != NumberToGuess:

    #If statement helping the computer to refine its guesses
    #Runs if the computer's guess is higher than the user's number
    if ComputerGuess > NumberToGuess:
        #Print statement telling the user that the computer guessed too high
        print(str(ComputerGuess) + " is too high")
        #Sets the maximum as the computer's current guess
        Max = ComputerGuess
        #Increments the counter by one
        GuessCounter += 1
        #Calculates the computer's next guess with the updated variables
        ComputerGuess = (Min + Max) // 2

    #Runs if the computer's guess is lower than the user's number   
    elif ComputerGuess < NumberToGuess:
        #Print statement telling the user that the computer guessed too low
        print(str(ComputerGuess) + " is too low")
        #Sets the minimum as the computer's current guess
        Min = ComputerGuess
        #Increments the counter by one
        GuessCounter += 1
        #Calculates the computer's next guess with the updated variables
        ComputerGuess = (Min + Max) // 2

#Increments the counter for the final guess
GuessCounter += 1

#Print statement printing out the user's number
print("I got it! Your secret number is: " + str(NumberToGuess) + "!")
#Print statement printing out how many guesses the computer needed
print("And it only took me " + str(GuessCounter) + " guesses. Not bad!")
    

