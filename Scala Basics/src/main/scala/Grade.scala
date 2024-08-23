object Grade{
  def main(args: Array[String]): Unit ={
    import scala.io.StdIn._
    println("Enter number: ")
    val userInput = readInt()
    var result = ""
    if (userInput > 90){
      result = "A"
    }else if(userInput >80){
      result = "B"
    }else if(userInput >70){
      result = "C"
    }else if(userInput > 60){
      result = "D"
    }else if(userInput > 50){
      result = "E"
    } else{
      result = "F"
    }

    println(s"Grade is: $result")

    println(if (userInput > 90) "Grade is A" else if(userInput>80) "Grade is B" else if(userInput>70) "Grade is C" else if(userInput>60) "Grade is D" else if(userInput>50) "Grade is E" else "Grade is F")

  }
}
