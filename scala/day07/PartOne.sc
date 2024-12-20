import scala.io.Source

val ops = Source.stdin.getLines.map(line =>
  val Array(targetStr, restStr) = line.split(":").map(_.trim)
  val target = targetStr.toLong
  val rest = restStr.split(" ").map(_.toInt)

  (target, rest.toList)
)

def solve(target: Long, rest: List[Int]): Boolean =

  def helper(rest: List[Int], currentSum: Long): Boolean =
    if currentSum > target then false
    else
      rest match
        case head :: next =>
          val multiply = helper(next, currentSum * head)
          val add = helper(next, currentSum + head)

          multiply || add
        case Nil =>
          currentSum == target

  helper(rest, 0)

val ans =
  ops
    .map((target: Long, rest: List[Int]) =>
      if solve(target, rest) then target else 0
    )
    .sum

println(ans)
