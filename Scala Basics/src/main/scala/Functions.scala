
object Functions{
  def main(args: Array[String]): Unit = {

//    //Functions: Function is a block of code which must do a certain task
//    import scala.io.StdIn._
//
//    //Method
//    def greetings(name: String): Unit = {
//      println(s"Hello, $name Welcome to UST.")
//    }
//
//    //user input
//    println("Please enter your username: ")
//    val username = readLine()
//
//    //calling function
//    greetings(username)
//
//    //More than one parameter
//    def add(a:Int, b:Int): Int = {
//      a + b
//    }
//
////    println("Enter first number: ")
////    var a: Int = readInt()
////    println("Enter second number: ")
////    var b: Int = readInt()
////
//    //Alternative
//    var a: Int = readLine("Enter first number: ").toInt
//    var b: Int = readLine("Enter second number: ").toInt
//
//    println("Result of addition is:  "+add(a,b))
//
//
//    //Create a scala function calculator
//    def calculator(a:Int, b:Int, op:String): Any = {
//      if (op == "+"){
//        a+b
//      }else if(op == "-"){
//        a-b
//      }else if(op == "/"){
//        a/b
//      }else if(op == "*"){
//        a*b
//      }else{
//        "Invalid Operation"
//      }
//    }
//
//    a = readLine("Enter first number: ").toInt
//    b = readLine("Enter second number: ").toInt
//    val op = readLine("Enter operation: ")
//    println(calculator(a, b, op))


    // Declare a function with default value
    def divide(a: Int, b:Float = 5): Float = {
      a/b
    }

    println(divide(10))
    println(divide(23,12))

    //Anonymous function
    val add = (a:Int, b: Int ) => a+b
    println(add(10,20))



    //High order functions: Function passed as parameter
    def applyFunction(f:(Int,Int) => Int, a:Int,b:Int): Int = {
      f(a,b)
    }
    println(applyFunction(add,10,20))


    //Write a function to remove duplicate entry from list
    val duplicate_list = List(1,1,2,3,4,5,4,4)
    def removeDuplicate(x: List[Int]): List[Int] = {
      val newSet = x.toSet
      newSet.toList
    }
    print(removeDuplicate(duplicate_list).mkString(", "))

    //Alternative
    val removeD = (x: List[Int]) => x.distinct
    println(removeD(duplicate_list).mkString(", "))

    //palindrome
    val isPalindrome = (x:String) => x.toLowerCase().reverse == x.toLowerCase()
    println(if (isPalindrome("Malayalam")) "Palindrome" else "Not Palindrome")


    //Create a scala function which returns factorial of a number
    def factorial(x:Int): Int = {
      if (x == 0)
        1
      else
        x * factorial(x-1)
    }

    println(factorial(5))

    // Example usage
    val number = 5
    val fact = factorial(5)
    println(fact)

//    def isPrime():Boolean = {
//      var x = 10
//      var i = 2
//      var flag = true
//      while(i<x/2) {
//        if (x % i == 0) {
//          flag = false
//        }
//        i += 1
//      }
//      flag
//    }
//    println(isPrime())


  }
}