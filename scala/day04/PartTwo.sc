import scala.io.Source

val puzzle =
  Source.stdin.getLines().map((line: String) => line.chars().toArray).toArray

def getCharOpt(pos: (Int, Int)): Option[Int] =
  val row = pos._1
  val col = pos._2
  puzzle.lift(row).map(_.lift(col)).flatten

def isXmas(
    startPos: (Int, Int)
): Boolean =
  val middle = getCharOpt(startPos)
  val upleft = getCharOpt((startPos._1 - 1, startPos._2 - 1))
  val upright = getCharOpt((startPos._1 - 1, startPos._2 + 1))
  val downleft = getCharOpt((startPos._1 + 1, startPos._2 - 1))
  val downright = getCharOpt((startPos._1 + 1, startPos._2 + 1))

  middle.contains('A') &&
  ((upleft.contains('M') && downright.contains('S')) || (upleft.contains(
    'S'
  ) && downright.contains('M'))) &&
  ((upright.contains('M') && downleft.contains('S')) || (upright.contains(
    'S'
  ) && downleft.contains('M')))

val found = (0 to puzzle.length)
  .map((row: Int) => (0 to puzzle(0).length).map((col: Int) => (row, col)))
  .flatten
  .map(isXmas)
  .count(identity)

println(found)
