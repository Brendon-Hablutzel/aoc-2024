import scala.io.Source
import scala.collection.mutable.HashMap

val stones = Source.stdin.getLines().next().split(" ").map(_.toInt).toVector

val memo = HashMap[(Long, Int), Long]()

def computeStonesProduced(stone: Long, blinksRemaining: Int): Long =
  if blinksRemaining == 0 then 1
  else
    memo.get((stone, blinksRemaining)) match
      case Some(stonesProduced) => stonesProduced
      case None =>
        val stonesProduced = if stone == 0 then
          val stonesProduced = computeStonesProduced(1, blinksRemaining - 1)

          stonesProduced
        else if stone.toString.length % 2 == 0 then
          val stoneStr = stone.toString
          val midpointIdx = stoneStr.length / 2
          val firstHalf = stoneStr.substring(0, midpointIdx)
          val secondHalf = stoneStr.substring(midpointIdx)
          val stonesProduced = computeStonesProduced(
            firstHalf.toInt,
            blinksRemaining - 1
          ) + computeStonesProduced(secondHalf.toInt, blinksRemaining - 1)

          stonesProduced
        else
          val stonesProduced =
            computeStonesProduced(2024 * stone, blinksRemaining - 1)

          stonesProduced

        memo((stone, blinksRemaining)) = stonesProduced
        stonesProduced

val ans = stones.map(computeStonesProduced(_, 75)).sum
println(ans)
