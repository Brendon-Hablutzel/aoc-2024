import scala.collection.immutable.{HashSet, Queue}
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
      searched: Set[Cell],
      nines: Set[Cell]
  ): Set[Cell] =
    if queue.isEmpty then nines
    else
      val (currentPosition @ Cell(rowIdx, colIdx, value), newQueue) =
        queue.dequeue

      if searched(currentPosition) then bfs(newQueue, searched, nines)
      else if value == 9 then
        bfs(newQueue, searched + currentPosition, nines + currentPosition)
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

        bfs(newQueue.enqueueAll(neighbors), searched + currentPosition, nines)

  val searched: HashSet[Cell] = HashSet()
  val nines: HashSet[Cell] = HashSet()
  val q = Queue(startPosition)

  bfs(q, searched, nines)

val ans = startingPositions.map(findTrails).map(_.size).sum
println(ans)
