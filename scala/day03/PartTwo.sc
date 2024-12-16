import scala.util.matching.Regex.Match
import scala.io.Source
import scala.util.matching.Regex

val mulPattern: Regex = "mul\\((\\d+),(\\d+)\\)|do\\(\\)|don't\\(\\)".r

val input = Source.stdin.getLines().mkString

var enabled = true
var sum = 0
for matched <- mulPattern.findAllMatchIn(input) do
  matched.group(0) match {
    case "do()"    => enabled = true
    case "don't()" => enabled = false
    case _ if enabled =>
      sum += matched.group(1).toInt * matched.group(2).toInt
    case _ => ()
  }

println(sum)
