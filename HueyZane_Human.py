#Importing the random library to use random number generation
import random

#Variable asking the user for how many games they with to play
GameNumber = input("How many games do you want to play? ")
#Variable converting the user's input number into an integer for later use
GameNumber = int(GameNumber)
#Variable to keep track of how many games are left before the loop terminates
GamesLeft = GameNumber

#Variable that produces a random integer between 1 and 100
Random = random.randint(1, 100)
#Variable to set the minimum range of numbers
Min = 1
#Variable to set the maximum range of numbers
Max = 100

#While loop that runs for each game the user wants to play
while GamesLeft > 0:
    #Variable keeping track of if the user's guess is right
    RightGuess = False
    #While loop that runs until the user's guess is right
    while RightGuess == False:
        #Variable to receive a guess from the user
        Guess = input("Enter a whole number between 1 and 100: ")
        #Variable converting the user's input number into an integer for later use
        Guess = int(Guess)
        
        #If statement checking if the user's guess is correct or not
        #Activates if the user's guess is correct
        if Guess == Random:
            #Print statement telling the user they guessed correctly
            print("You guessed the number!")
            #Print statement telling the user what the secret number was
            print("The secret number was: " + str(Random))
            #Re-randomizes the variable before the user's next game
            Random = random.randint(1, 100)
            #Subtracts one from the number of remaining games
            GamesLeft = GamesLeft - 1
            #Sets the RightGuess check to true
            RightGuess = True

        #Activates if the user's guess is too high
        elif Guess > Random and Guess <= Max:
            #Print statement telling the user their guess is too high
            #Recommends the user guesses a lower valued number
            print("You guessed too high. Try a lower number")

        #Activates if the user's guess is too low
        elif Guess < Random:
            #Print statement telling the user their guess is too low
            #Recommends the user guesses a higher valued number
            print("You guessed too low. Try a higher number")

        #Activates if the user's guess is higher than the max variable or lower than the min variable
        elif Guess > Max or Guess < Min:
            #Print statement telling the user their guess is outside of the range
            #Recommends the user give another guess
            print("Your guess is outside the range. Guess again")
            
#Print statement telling the user they've played the correct number of games
#Tells the user goodbye
print("You've played the correct number of games now! Bye bye, friend")
