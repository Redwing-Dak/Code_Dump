//Student class
//Takes in a string and a float
data class Student(val name: String, val grade: Float)

//Function to calculate the average grade from a list of objects
fun calculateAverageGrade(students: List<Student>): Float {
    //If statement checking that the list isn't empty
    //Returns the students' average
    return if (students.isNotEmpty()) students.sumOf { it.grade.toDouble() }.toFloat() / students.size
    else 0f
}
//Function to sort the students in the list from highest grade to lowest grade
fun sortStudentsByGrade(students: List<Student>): List<Student> {
    //Returns the sorted list
    return students.sortedByDescending { it.grade }
}

//Main function
fun main() {
    //Print statement asking the user how many students will need their information entered
    print("How many students need their information entered? ")
    //Variable to hold the number of students
    val numberOfStudents = readln().toIntOrNull() ?: return
    //Initialization of an empty list that will be added to later
    val studentList = mutableListOf<Student>()

    //Loop that runs for the necessary number of students
    repeat(numberOfStudents) {
        //Print statement asking the user what the student's name is
        print("Enter student name: ")
        //Variable to store the student's name
        val name = readln()
        //Print statement asking the user what the student's grade is
        print("Enter a number grade: ")
        //Variable to store the student's grade
        val grade = readln().toFloatOrNull() ?: 0f

        //Creates an object from the current student's name and grade
        //Adds the object to the list
        studentList.add(Student(name, grade))
    }

    //Variable to call and store the students' average grade
    val averageGrade = calculateAverageGrade(studentList)
    //Variable to call and store the sorted list of students
    val sortedStudents = sortStudentsByGrade(studentList)

    //Print statement that prints out a header for the list
    println("\nStudent List Sorted by Grade (Highest to Lowest):")
    //Loop to parse through the list and print each student's information
    sortedStudents.forEach { println("${it.name}: ${it.grade}") }

    //Print statement that tells the user what the class' average was
    println("\nAverage Grade: %.2f".format(averageGrade))
}
