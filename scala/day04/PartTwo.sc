import scala.io.Source

case class Position(val row: Int, val col: Int)

extension (p: Position)
  def +(other: (Int, Int)) =
    Position(p.row + other._1, p.col + other._2)

  def getInGrid[A](grid: IndexedSeq[IndexedSeq[A]]): Option[A] =
    grid.lift(p.row).map(_.lift(p.col)).flatten

val puzzle =
  Source.stdin
    .getLines()
    .map((line: String) => line.chars().toArray.toIndexedSeq)
    .toArray
    .toIndexedSeq

def isXmas(
    startPos: Position
): Boolean =
  val middle = startPos.getInGrid(puzzle)
  val upleft = (startPos + (-1, -1)).getInGrid(puzzle)
  val upright = (startPos + (-1, 1)).getInGrid(puzzle)
  val downleft = (startPos + (1, -1)).getInGrid(puzzle)
  val downright = (startPos + (1, 1)).getInGrid(puzzle)

  middle.contains('A') &&
  ((upleft.contains('M') && downright.contains('S')) || (upleft.contains(
    'S'
  ) && downright.contains('M'))) &&
  ((upright.contains('M') && downleft.contains('S')) || (upright.contains(
    'S'
  ) && downleft.contains('M')))

val positions = for i <- 0 to puzzle.length; j <- 0 to puzzle(0).length
yield Position(i, j)

val found = positions.map(isXmas).count(identity)

println(found)
