
//Parent class
class Ecom (val name: String, val quantity: Float, val price: Float){
  def displayDetails():Unit= {
    println(s"$name $quantity $price")
  }
}

//subclass
class Electronics(name:String, quantity: Float, price:Float) extends Ecom(name, quantity, price){
  //override parent method
  override def displayDetails(): Unit = {
    println(s"\n--Electronic--\n $name \n $quantity \n $price")
  }

  def totalPrice(): Unit = {
    println(s"Total price is: ${price * quantity}")
  }
}

//subclass
class Books(name:String, quantity: Float, price:Float) extends Ecom(name, quantity, price){
  //override parent method
  override def displayDetails(): Unit = {
    println(s"\n--Books--\n $name \n $quantity \n $price")
  }

  def totalPrice(): Unit = {
    println(s"Total price is: ${price * quantity}")
  }
}

//subclass
class Footwears(name:String, quantity: Float, price:Float) extends Ecom(name, quantity, price){
  //override parent method
  override def displayDetails(): Unit = {
    println(s"\n--FootWear--\n $name \n $quantity \n $price")
  }

  def totalPrice(): Unit = {
    println(s"Total price is: ${price * quantity}")
  }
}

object InheritanceEcom extends App{
  val ecomGeneral = new Ecom("Generic name", 0.00, 0.00)
  val book1 = new Books("Wings of fire", 2, 100.99)
  val ec1 = new Electronics("Laptop", 4, 120000.00)
  val fw = new Footwears("Bata", 6, 199.00)

  ecomGeneral.displayDetails()

  book1.displayDetails()
  book1.totalPrice()

  ec1.displayDetails()
  ec1.totalPrice()

  fw.displayDetails()
  fw.totalPrice()

}