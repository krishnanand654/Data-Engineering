object ConditionalStatements{
  def main(args: Array[String]): Unit = {
    //If condition
    val x = 10
    if(x > 5){
      println(s"$x is Greater than 5")
    } else{
      println(s"$x is less than 5")
    }

    //if else expression
    val y = 3
    val result = if (y%2 == 0) "Even" else "Odd"

    //ternary and list comprehension python
    println(result)

    //ask user to input the data
    import scala.io.StdIn._
    println("Enter the value: ")
    val input = readInt()
    println(if (input % 2==0 )"Even" else "Odd")
    
  }
}
