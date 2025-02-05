//Main function
fun main () {
    //Variable to generate a random number between 1 and 100
    var random = (1..100).random()

    //Print statement asking the user how many games they want to play
    print("How many games do you want to play? ")
    //Converts the user's input into an integer for future use
    val gameNumber = readln().toInt()
    //Variable set to the number of total games
    var gamesLeft = gameNumber

    //Variable to keep track of the lowest number in the range
    val min = 1
    //Variable to keep track of the highest number in the range
    val max = 100

    //While loop that runs until the user has played the necessary number of games
    while (gamesLeft > 0) {
        //Boolean variable to use as a condition to terminate the inner loop
        var rightGuess = false
        //While loop that runs until the user guesses the correct number
        while (!rightGuess) {
            //Print statement asking the user for a number within the range
            print("Enter a whole number between 1 and 100: ")
            //Converts the user's input into an integer for future use
            val guess = readln().toInt()

            //If statement that checks if the user's guess is correct, too high,
            //too low, or out of the range
            if (guess == random) {
                //Print statement informing the user that they guessed correctly
                println("You guessed the number!")
                //Print statement telling the user the randomly generated number
                println("The secret number was: " + random.toString())
                //Re-randomizes the number for future games
                random = (1..10).random()
                //Subtracts 1 from the number of games remaining
                gamesLeft -= 1
                //Sets the while loop condition to true
                rightGuess = true
            } else if (guess > random && guess <= max) {
                //Print statement informing the user that they guessed too low
                println("You guessed too high. Try a lower number")
            } else if (guess < random && guess >= min) {
                //Print statement informing the user that they guessed too high
                println("You guessed too low. Try a lower number")
            } else if (guess > max || guess < min) {
                //Print statement informing the user that their guess wasn't within the range
                //Suggests the user guess again
                println("Your guess is outside the range. Guess again")
            }
        }
    }
    //Print statement informing the user that they've played the necessary number of games
    println("You've played the correct number of games now! Bye bye, friend")
}