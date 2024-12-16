import scala.io.Source
import scala.collection.mutable.HashMap

val lines = Source.stdin
  .getLines()
  .map(_.split(" +"))
  .filter(_.length == 2)
  .map((a: Array[String]) => (a(0).toInt, a(1).toInt))
  .toList

val (l1, l2) = lines.unzip

val l2Freq = HashMap[Int, Int]()

for n <- l2 do
  l2Freq.updateWith(n) {
    case Some(freq) => Some(freq + 1)
    case None       => Some(1)
  }

val res = l1.map((n: Int) => n * l2Freq.getOrElse(n, 0)).sum

println(res)
