import scala.io.Source

case class Position(val row: Int, val col: Int)

extension (p: Position)
  def +(other: (Int, Int)) =
    Position(p.row + other._1, p.col + other._2)

  def getInGrid[A](grid: Array[Array[A]]): Option[A] =
    grid.lift(p.row).map(_.lift(p.col)).flatten

val matchers = List(
  ((0, -1), (0, -2), (0, -3)), // left
  ((0, 1), (0, 2), (0, 3)), // right
  ((-1, 0), (-2, 0), (-3, 0)), // up
  ((1, 0), (2, 0), (3, 0)), // down
  ((-1, -1), (-2, -2), (-3, -3)), // up left diagonal
  ((-1, 1), (-2, 2), (-3, 3)), // up right diagonal
  ((1, -1), (2, -2), (3, -3)), // down left diagonal
  ((1, 1), (2, 2), (3, 3)) // down right diagonal
)

val puzzle =
  Source.stdin.getLines().map((line: String) => line.chars().toArray).toArray

def isXmas(
    startPos: Position,
    matcher: ((Int, Int), (Int, Int), (Int, Int))
): Boolean =
  val first = startPos.getInGrid(puzzle)
  val second = (startPos + matcher._1).getInGrid(puzzle)
  val third = (startPos + matcher._2).getInGrid(puzzle)
  val fourth = (startPos + matcher._3).getInGrid(puzzle)

  first.contains('X') && second.contains('M') && third.contains('A') && fourth
    .contains('S')

val positions = for i <- 0 to puzzle.length; j <- 0 to puzzle(0).length
yield Position(i, j)

val found = positions
  .map(pos => matchers.map(matcher => isXmas(pos, matcher)).count(identity))
  .sum

println(found)
