import scala.collection.immutable.HashSet
import scala.collection.immutable.HashMap
import scala.io.Source

case class Cell(val row: Int, val col: Int, var value: Char)

val guardCases = HashMap(
  // guard position -> (rotated right position, row change, col change)
  '^' -> ('>', -1, 0),
  '>' -> ('v', 0, 1),
  'v' -> ('<', 1, 0),
  '<' -> ('^', 0, -1)
)

// given a map and a guard cell, performs a turn and returns the new guard's position,
// or `None` if this turn would cause the guard to exit the map
def turn(
    map: Vector[Vector[Cell]],
    guardCell: Cell
): Option[Cell] =
  val (rotatedRight, rowChange, colChange) = guardCases(guardCell.value)

  val newRow = guardCell.row + rowChange
  val newCol = guardCell.col + colChange

  if newRow < 0 || newRow >= map.length || newCol < 0 || newCol >= map(0).length
  then None
  else
    val newCell = map(newRow)(newCol)

    Some(newCell.value match {
      // guard is blocked, rotate right
      case '#' => guardCell.copy(value = rotatedRight)
      // guard is not blocked, advance
      case _ => newCell.copy(value = guardCell.value)
    })

def checkLoop(map: Vector[Vector[Cell]]): Boolean =
  def helper(
      guardCell: Cell,
      visited: HashSet[Cell]
  ): Boolean =
    if visited.contains(guardCell) then true
    else
      turn(map, guardCell) match
        case Some(newGuardCell) =>
          helper(newGuardCell, visited + guardCell)
        case None => false

  helper(map.flatten.find(_.value == '^').get, HashSet())

val map =
  Source.stdin
    .getLines()
    .zipWithIndex
    .map((line: String, rowIdx: Int) =>
      line
        .chars()
        .toArray
        .zipWithIndex
        .map((char: Int, colIdx: Int) => Cell(rowIdx, colIdx, char.toChar))
        .toVector
    )
    .toVector

val mapRows = map.length
val mapCols = map(0).length

// NOTE: does not check for case where a block is placed directly in front of the guard,
// but this does not affect output for my input
val loopingCells = for row <- 0 until mapRows; col <- 0 until mapCols
yield map(row)(col).value match
  case '#' | '^' => false
  case _ => {
    map(row)(col).value = '#'
    val doesLoop = checkLoop(map)
    map(row)(col).value = '.'
    doesLoop
  }

println(loopingCells.count(identity))
