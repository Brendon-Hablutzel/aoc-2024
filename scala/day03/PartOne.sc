import scala.util.matching.Regex.Match
import scala.io.Source
import scala.util.matching.Regex

val mulPattern: Regex = "mul\\((\\d+),(\\d+)\\)".r

val input = Source.stdin.getLines().mkString

val total =
  mulPattern
    .findAllMatchIn(input)
    .map((matched: Match) => matched.group(1).toInt * matched.group(2).toInt)
    .sum

println(total)
