import scala.io.Source

val lines =
  Source.stdin
    .getLines()
    .map((line: String) =>
      line.split(" ").map((v: String) => v.toIntOption).collect {
        case Some(i) => i
      }
    )

def isSafe(levels: Array[Int]): Boolean =
  def isSafeHelper(levels_subarr: Array[Int], inc: Boolean): Boolean =
    if levels_subarr.length == 1 then true
    else
      val diff = levels_subarr(1) - levels_subarr(0)

      if (diff < 0 && inc) || (diff > 0 && !inc) || (diff.abs > 3) || (diff.abs == 0)
      then false
      else isSafeHelper(levels_subarr.drop(1), inc)

  isSafeHelper(levels, levels(1) - levels(0) > 0)

val numSafe = lines.map(isSafe).count((a: Boolean) => a)

println(numSafe)
