//Main function
fun main() {
    //Boolean variable to check if the user wants to exit
    var userQuit = false
    //While loop that runs until the user types exit
    while(!userQuit) {
        //Print statement asking the user for a number
        print("Enter a number: ")
        //Variable to store the user's input
        val userInput = readln()

        //If statement checking to see if the user wishes to exit
        if(userInput == "exit" || userInput == "Exit") {
            //Sets the boolean variable to true
            userQuit = true
            //Skips the rest of the loop
            continue
        }

        //Converts the user's number into an integer for future use
        val number = userInput.toInt()

        //If statement checking to see if the user's number is even or odd
        if(number.mod(2) == 0) {
            //Print statement informing the user their number is even
            println("This number is even")
        }
        else if(number.mod(2) == 1) {
            //Print statement informing the user their number is odd
            println("This number is odd")
        }
    }
}