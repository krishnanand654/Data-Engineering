object DataStructures{
  def main(args: Array[String]): Unit = {
    val valList:List[String] = List("Apricot", "BlueBerry", "Cherry","Donuts", "Eclairs")
    val firstElement = valList.head
    val restOfList = valList.tail
    val lastValue = valList.last
    val secondValue = valList(1)
    val length = valList.length

    println("Display First value: "+firstElement)
    println("Display Rest of the value: "+restOfList)
    println("Display Last value: "+lastValue)
    println("Display Second value: "+secondValue)
    println("Display length: "+length)

    //Append to valList is not possible due to immutability
//   valList = valList+"fig"

    //immutable
    val appendList = valList:+"Fig"

    println("Is valList Empty ? "+valList.isEmpty)

    val newValList = List("Fig","Grapes","HazelNut")

    val fruitBasket = valList ++ newValList

    print(fruitBasket)

    //Transform list
    val list_1 = List(1,2,3,4,5,6,7,8,9,10)
    println(list_1.map(_*3))

    val evenNum = list_1.filter(_%2 ==0)
    println("Filtered Values "+evenNum)

    val NestedList = List(List("Delhi","Cochin", "Bengaluru"),
                          List("Pune","Varkala", "Mumbai"),
                          List("Trivandrum","Visakhapatnam", "Kottayam"))

    //identity is a predefined function 'A=>A'
    println(NestedList.flatMap(identity))
    println(NestedList.flatten)

    print(list_1.filter(_%2 ==0).reduce(_+_))

    println(fruitBasket.map(_.length))
    println(fruitBasket.map(_.startsWith("A")))

    //sort the list by word length
    val sortedList = fruitBasket.sortWith(_.length < _.length)
    println(sortedList)

    val sortedCity = NestedList.flatten.sortBy(_.length)
    println(sortedCity)

    //list of city that begins with letter K

    val filteredCity = NestedList.flatten.filter(_.startsWith("K"))
    println(filteredCity)


    //subset and slicing
    val city = NestedList.flatten
    println(city)
    println(city.takeRight(5))

    println(city.drop(4))
    println(city.dropRight(2))
    println(city.slice(1,6))

      //slicing using random index positions
    val indices = List(0,2,4,5,7,9)
    // lift is a method that retrieves
    println(indices.flatMap(index => city.lift(index)))

    val populations: List[Int] = List(20000000, 600000, 12000000, 3500000, 40000, 20000000, 900000, 1700000, 130000)

    val pairedList = city.zip(populations)

    println(pairedList)


    //Array : Mutable Collection, indexed with sequence of elements.
    //Array provides fast access and modification of elements,
    // making it useful for performance critical applications.

    val emptyArray = Array[Int]()
    val array1 = Array(1,2,3,4,5,6)

    val firstArrayElement= array1(0)
    val secondArrayElement = array1(1)

    array1(0) = 10
    array1.foreach(println)

    //length of array
    println("Array Length: "+array1.length)

    //adding or removing value to array
    //arrays are of fixed length
//    array1 += 7
//    array1 -= 3



    import scala.collection.mutable.ArrayBuffer
    val arrayBuffer = ArrayBuffer(1,2,3,4,5,6,7,8,9,10)
    arrayBuffer += 11
    arrayBuffer -= 1
    val newArray = arrayBuffer.toArray
    newArray.foreach(println)

    //convert array to arrayBuffer
    val array2 = ArrayBuffer(array1: _*)
    array2.foreach(println)

    //Array transformation
    //map
    println(array2.map(_*2))

    //filter
    println(array2.filter(_%2 == 0))

    //reduce
    println(array2.filter(_%2 ==0).reduce(_+_))

    val NestedArray = Array(Array("Delhi", "Cochin", "Bengaluru"),
      Array("Pune", "Varkala", "Mumbai"),
      Array("Trivandrum", "Visakhapatnam", "Kottayam"))

    println("--cities--")
    NestedArray.flatten.foreach(println)


    //Apply mkString to Collections to Array, Lists, etc
    println(NestedArray.flatten.mkString(", "))

    //slicing and substring
    println("--slicing")
    val cityArray = NestedArray.flatten
    println(cityArray.take(5).mkString(","))
    println(cityArray.takeRight(5).mkString(","))

    println(cityArray.drop(4).mkString(","))
    println(cityArray.dropRight(2).mkString(","))
    println(cityArray.slice(1, 6).mkString(","))

    //reverse
    println(cityArray.mkString(","))
    println(cityArray.reverse.mkString(","))

    //sorting
    //unsorted
    println(array1.mkString(", "))
    //sorted
    println(array1.sorted.mkString(", "))

    println(list_1.sorted.mkString(", "))



  }
}
