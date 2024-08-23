import scala.io.Source
object FileAnalysis{
  def main(args: Array[String]): Unit = {

    val source = Source.fromFile("D:/sample.txt")

    val lines = source.getLines().toList

    source.close()

    // split lines into words, change words to its lowercase
    val words = lines.flatMap(_.split("\\s+").map(_.toLowerCase))

    // Group words by identity
    // map values by its size
    // sort by words in descending order using negated values (-_.2)
    val wordCount = words.groupBy(identity).mapValues(_.size).toSeq.sortBy(-_._2)


    //Find the count of words
    val total = words.length
    println(s"Total no.of words: $total")

    //Find the word with maximum and minimum length
    println(s"--Minimum word--")
    wordCount.takeRight(1).foreach{case (word, count) => println(s"'$word' : $count ")}

    println(s"--Maximum word:--")
    wordCount.take(1).foreach{case (word, count) => println(s"'$word' : $count ")}

    
    
  }
}