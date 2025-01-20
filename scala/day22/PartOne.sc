import scala.io.Source

def transform(num: Long): Long =
  var n = num
  n = (n ^ (n * 64)) % 16777216
  n = (n ^ (n / 32)) % 16777216
  n = (n ^ (n * 2048)) % 16777216
  n

val ans = Source.stdin.getLines
  .map(_.toLong)
  .map(initialNum =>
    (1 to 2000).foldLeft(initialNum) { case (currentNum, _) =>
      transform(currentNum)
    }
  )
  .sum

println(ans)
