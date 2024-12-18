import scala.io.Source

val lines =
  Source.stdin
    .getLines()
    .map((line: String) => line.split(" ").map((v: String) => v.toInt))

def isSafe(levels: Array[Int]): Boolean =
  def isSafeHelper(levelsSubarr: Array[Int], inc: Boolean): Boolean =
    if levelsSubarr.length == 1 then true
    else
      val diff = levelsSubarr(1) - levelsSubarr(0)

      if (diff < 0 && inc) || (diff > 0 && !inc) || (diff.abs > 3) || (diff.abs == 0)
      then false
      else isSafeHelper(levelsSubarr.drop(1), inc)

  if (levels(1) - levels(0) == 0) then false
  else isSafeHelper(levels, levels(1) - levels(0) > 0)

val numSafe = lines.map(isSafe).count(identity)

println(numSafe)
