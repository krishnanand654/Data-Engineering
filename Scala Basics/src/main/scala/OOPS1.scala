class Car(val make: String, val model: String, var year: Int) {
  def displayInfo(): Unit = {
    println(s"Car Info: $year, $make, $model")
  }
}

//Create an object of class Car

// Singleton object extends App (trait) which doesn't need main function anymore
object OOPS extends App {
  val car = new Car("Hyundai", "Creta", 2023)
  car.displayInfo()

  car.year = 2024
  car.displayInfo()
}
