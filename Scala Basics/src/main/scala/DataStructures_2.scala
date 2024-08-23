
object DataStructures_2{
  def main(args: Array[String]):Unit = {
    //Scala collection Map.
    //Map : Collection of key-Value pairs. Map can be either mutable or immutable
    // by default Map is Immutable.
    val fruitBasket = Map("Apricot"->20, "BlueBerry"->250, "Cherry"->100,"Donuts"->24, "Eclairs"->100)

    //mutable
    import scala.collection.mutable
    val mutableMap = mutable.Map("Apricot"->20, "BlueBerry"->250, "Cherry"->100,"Donuts"->24, "Eclairs"->100)

    //Basic operation
    println(fruitBasket("Cherry"))

    println(fruitBasket.contains("Donuts"))

    //size
    println(fruitBasket.size)

    val keys = mutableMap.keys
    val values = mutableMap.values

    //adding or removing in Map
    mutableMap += ("Fig"->30)
    mutableMap -= ("Eclairs")

    //update
    mutableMap("Fig") = 40

    //Apply same on Immutable

    val newFruitBasket = fruitBasket + ("Fig"->30)

    println(newFruitBasket)


    //Set
    val set1 = Set(1,2,3,4,5,6,7,8)

    //map
    println(set1.map(_*2))

    //filter
    println(set1.filter(_%2 == 0))

    //reduce
    println(set1.reduce(_*_))

    import scala.collection.mutable

    val mutableSet = mutable.Set(10, 20, 30, 40, 50, 60)
    mutableSet ++= Set(80, 90, 100)

    println(mutableSet)
    // Clear the set
    mutableSet.clear()
    println(mutableSet)

    //Create a new collection
    val fruitList = List("Apple", "Orange", "Grapes","Banana","Apricot")
    val mapFruits = fruitList.groupBy(_.head)




    //Typecast immutable map to mutable map
    val mutableNewMap: mutable.Map[Char, List[String]] = mutable.Map(mapFruits.toSeq: _*)
    mutableNewMap ++= Map('D'->List("Donut"),'E'->List("Eclairs"))

    println(mutableNewMap)


    //Tuple Datatype

    // Tuple: Collection of Immutable Datatype, fixed size, heterogeneous
    val tuple1 = (1, "Hello Tuple", 3.14, "scala", 123456781)

    val firstValue = tuple1._1
    val secondValue = tuple1._2

    println(firstValue)

    //pattern matching in tuple
    val(var1, var2, var3) = (1, "scala", 3.14)

    println(var2)

      println(tuple1.productArity)

    println(tuple1.getClass)

    val newTuple = tuple1.copy(_4 = "Tuple")

    println(newTuple)

    tuple1.productIterator.foreach{
      (element => println(s"Element: $element"))
    }
    


  }
}