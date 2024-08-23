
//Primitive data types
object Datatypes {
  def main(args: Array[String]): Unit = {
    val intValue: Int = 25
    var doubleValue: Double = 23.234234324
    var longIntValue: Long = 9495434706L
    var myFloatValue: Float = 123.23F

    var charValue: Char = 'A'
    var message: String = "hello Scala"

    var byteValue: Byte = 127
    val booleanValue: Boolean = true
    val booleanValue1: Boolean = false

    println("Integer Value "+ intValue)
    println("Boolean Value "+booleanValue)
    println("String Value "+ message)
    println("Double Value "+doubleValue)

    //intValue = 120 cannot be reassigned because of val {immutability}

    charValue = 'C'
    println("New Character value "+ charValue)
  }
}
