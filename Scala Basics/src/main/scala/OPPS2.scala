class Circle(val radius: Double){
  def area: Double = Math.PI * radius * radius
  def circumference: Double = 2* Math.PI * radius
}

//Companion objects can be used to provide factory method and utility
//function which are related to class
object Circle{
  def apply(radius:Double): Circle = new Circle(radius)
}

object OOPS2 extends App{
  val circle = Circle(5.0)

  println(f"Area: ${circle.area}%.2f")
  println(f"Circumference: ${circle.circumference}%.2f")
}

