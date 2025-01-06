import scala.collection.immutable.{Vector, Queue}
import scala.io.Source

case class Cell(val rowIdx: Int, val colIdx: Int, val value: Int)

// read input
val map =
  Source.stdin
    .getLines()
    .zipWithIndex
    .map((line: String, rowIdx: Int) =>
      line.iterator.zipWithIndex
        .map((char: Char, colIdx: Int) => Cell(rowIdx, colIdx, char - '0'))
        .toVector
    )
    .toVector

val startingPositions = map.flatten.filter(cell => cell.value == 0)

def findTrails(startPosition: Cell) =
  def bfs(
      queue: Queue[Cell],
      nines: Vector[Cell]
  ): Vector[Cell] =
    if queue.isEmpty then nines
    else
      val (currentPosition @ Cell(rowIdx, colIdx, value), newQueue) =
        queue.dequeue

      if value == 9 then bfs(newQueue, nines :+ currentPosition)
      else
        val neighbors =
          List(
            (rowIdx + 1, colIdx),
            (rowIdx - 1, colIdx),
            (rowIdx, colIdx + 1),
            (rowIdx, colIdx - 1)
          )
            .filter((row, col) =>
              row >= 0 && row < map.length && col >= 0 && col < map(0).length
            )
            .filter((row, col) => map(row)(col).value - 1 == value)
            .map((row, col) => map(row)(col))

        bfs(newQueue.enqueueAll(neighbors), nines)

  val nines: Vector[Cell] = Vector()
  val q = Queue(startPosition)

  bfs(q, nines)

val ans = startingPositions.map(findTrails).map(_.size).sum
println(ans)
