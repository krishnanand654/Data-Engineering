object Loops {
  def main(args: Array[String]): Unit = {

    //while
    var variable = 1
    while (variable < 10) {
      println(variable)
      variable += 1
    }

    //for loop
    val numbers: List[Int] = List(1, 2, 3, 4, 5)
    for (num <- numbers) {
      println(num)
    }

    for (i <- 1 to 10 by 2) {
      println(i)
    }

    val food_list = List("idli", "vada", "dosa", "uttapam", "biriyani")

    for (food <- food_list) {
      println(food)
    }

    //filtering records in for loop using if

    //write a scala program which creates a collection of even array
    import scala.collection.mutable.ArrayBuffer
    val evenArrayBuffer = ArrayBuffer[Int]()

    for (m <- 1 to 20 if m % 2 == 0) {
      evenArrayBuffer += m
    }
    evenArrayBuffer.toArray.foreach(println)

    //2. Write a scala program to show collection of prime number between 1 to 100.

    //    println("Prime no")
    //    for (i <- 2 to 100) {
    //      var x = 1
    //      for (j <- 2 to i-1) {
    //        if (i % j == 0) {
    //          x = 0
    //        }
    //      }
    //      if (x == 1) {
    //        println(i)
    //      }
    //    }


    //    for (i <- 2 to 100) {
    //      var sum = 0
    //      for (j <- 2 to i)
    //        if (i % j == 0)
    //          sum = sum + j
    //      if (sum == i) {
    //        println(i)
    //      }
    //    }


    val primeNumbers = ArrayBuffer[Int]()
    for (num <- 1 to 100) {
      if (num > 1) {
        var isPrime = true
        for (i <- 2 to num / 2 if isPrime) {
          if (num % i == 0) {
            isPrime = false
          }
        }
        if (isPrime) {
          primeNumbers += num
        }
      }
    }

    println(primeNumbers.mkString(", "))

    //Fibanocci series
    println("Fibinocci series")
    var a = 0
    var b = 1
    var count = 0
    println(a)
    println(b)
    while (count < 10) {
      var sum = a + b
      a = b
      b = sum
      println(sum)
      count += 1
    }

    // 4. Find the first prime number greater than the given number
    import scala.io.StdIn._
    println("Enter number: ")
    val userInput = readInt()

    val primeNewNumbers = ArrayBuffer[Int]()


  // check for prime
    var flag = true
    var x = userInput + 1

    while(flag){
      var flag_2 = 0
      var y = 2
      while(y < x) {
        if (x % y == 0) {
          flag_2 = 1
        }
        y += 1
      }
      if(flag_2 == 0){
        print(x)
        flag = false
      }
      x+=1
    }




  }
}