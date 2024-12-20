import scala.io.Source

val ops = Source.stdin.getLines.map(line =>
  val Array(targetStr, restStr) = line.split(":").map(_.trim)
  val target = targetStr.toLong
  val rest = restStr.split(" ").map(_.toLong)

  (target, rest.toList)
)

def solve(target: Long, rest: List[Long]): Boolean =

  def helper(rest: List[Long], currentSum: Long): Boolean =
    if currentSum > target then false
    else
      rest match
        case head :: next =>
          val multiply = helper(next, currentSum * head)
          val add = helper(next, currentSum + head)
          val concatenated = currentSum.toString + head.toString
          val concatenate = helper(next, concatenated.toLong)

          multiply || add || concatenate
        case Nil =>
          currentSum == target

  helper(rest, 0)

val ans =
  ops
    .map((target: Long, rest: List[Long]) =>
      if solve(target, rest) then target else 0
    )
    .sum

println(ans)
