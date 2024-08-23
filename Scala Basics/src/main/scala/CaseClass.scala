// Case Classes are special classes in scala that are immutable
// and compared by value. They are idea use in pattern matching


case class Person(name:String,age:Int )

object CaseClass extends App{
  val person = Person("Tom", 10)

  def describePerson(person: Any): String = person match {
    case Person(name, age) => s"Person Name: $name, Age: $age"
  }

  println(describePerson(person))
}
