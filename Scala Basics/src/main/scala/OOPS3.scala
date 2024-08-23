//Parent class
class Animal (val name: String){
  def makeSound():Unit= {
    println(s"$name makes sound")
  }
}

//subclass
class Dog(name:String) extends Animal(name){
  //override parent method
  override def makeSound(): Unit = {
    println(s"$name make sound: Woof!")
  }
}

object OOPS3 extends App{
  val animal = new Animal("Generic name")
  val dog = new Dog("Bucky")
  animal.makeSound()
  dog.makeSound()
}