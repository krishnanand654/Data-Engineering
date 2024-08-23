import scala.io.Source
object FibinocciSeries{
  def main(args: Array[String]): Unit = {
    val source = Source.fromFile(f"D:/sample.txt.txt")
    val lines = source.getLines().toList

    println(lines)
    source.close()
  }
}