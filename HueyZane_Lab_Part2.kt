//Main function
fun main() {
    //Print statement asking the user for a number
    print("Enter a number: ")
    //Variable to hold the user's number
    val numberOne = readln().toInt()
    //Print statement asking the user for another number
    print("Enter another number: ")
    //Variable to hold the user's second number
    val numberTwo = readln().toInt()

    //Lambda expression that takes in two integers and multiplies them together
    val multiply = {x:Int, y:Int -> x*y}
    //Print statement calling the lambda expression and passing in the
    //user's two numbers
    println(multiply(numberOne,numberTwo))
}