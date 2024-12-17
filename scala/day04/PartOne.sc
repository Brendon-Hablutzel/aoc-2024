import scala.io.Source

val puzzle =
  Source.stdin.getLines().map((line: String) => line.chars().toArray).toArray

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

def getCharOpt(pos: (Int, Int)): Option[Int] =
  val row = pos._1
  val col = pos._2
  puzzle.lift(row).map(_.lift(col)).flatten

def applyDiff(pow: (Int, Int), diff: (Int, Int)): (Int, Int) =
  (pow._1 + diff._1, pow._2 + diff._2)

def isXmas(
    startPos: (Int, Int),
    matcher: ((Int, Int), (Int, Int), (Int, Int))
): Boolean =
  val first = getCharOpt(startPos)
  val second = getCharOpt(applyDiff(startPos, matcher._1))
  val third = getCharOpt(applyDiff(startPos, matcher._2))
  val fourth = getCharOpt(applyDiff(startPos, matcher._3))

  first.contains('X') && second.contains('M') && third.contains('A') && fourth
    .contains('S')

val found = (0 to puzzle.length)
  .map((row: Int) => (0 to puzzle(0).length).map((col: Int) => (row, col)))
  .flatten
  .map((pos: (Int, Int)) =>
    matchers
      .map((matcher) => isXmas((pos._1, pos._2), matcher))
      .count(identity)
  )
  .sum

println(found)
