import scala.collection.immutable.{HashSet, Queue}
import scala.io.Source

case class Cell(val rowIdx: Int, val colIdx: Int, val regionName: Char)

// read input
val gardens =
  Source.stdin
    .getLines()
    .zipWithIndex
    .map((line: String, rowIdx: Int) =>
      line.iterator.zipWithIndex
        .map((char: Char, colIdx: Int) => Cell(rowIdx, colIdx, char))
        .toVector
    )
    .toVector

def getRegion(startPosition: Cell): HashSet[Cell] =
  val startRegionName = startPosition.regionName
  def helper(
      queue: Queue[Cell],
      visited: HashSet[Cell],
      region: HashSet[Cell]
  ): HashSet[Cell] =
    if queue.isEmpty then region
    else

      val (currentPosition @ Cell(rowIdx, colIdx, regionName), newQueue) =
        queue.dequeue

      if visited.contains(currentPosition)
      then helper(newQueue, visited, region)
      else
        val newVisited = visited + currentPosition
        if regionName == startRegionName then
          val neighbors =
            List(
              (rowIdx + 1, colIdx),
              (rowIdx - 1, colIdx),
              (rowIdx, colIdx + 1),
              (rowIdx, colIdx - 1)
            )
              .filter((row, col) =>
                row >= 0 && row < gardens.length && col >= 0 && col < gardens(
                  0
                ).length
              )
              .map((row, col) => gardens(row)(col))

          helper(
            newQueue.enqueueAll(neighbors),
            newVisited,
            region + currentPosition
          )
        else helper(newQueue, newVisited, region)

  helper(Queue(startPosition), HashSet(), HashSet())

// get a collection of all regions
val (regions, _) =
  gardens.flatten.foldLeft(List[HashSet[Cell]](), HashSet[Cell]()) {
    case (acc @ (regions, visited), position) =>
      if visited(position) then acc
      else
        val region = getRegion(position)
        (region +: regions, visited ++ region)
  }

val totalCost = regions
  .map(region =>
    val area = region.size
    val perimeter = region
      .foldLeft(0)((acc, position) =>
        val Cell(rowIdx, colIdx, regionName) = position
        acc + (List(
          (rowIdx + 1, colIdx),
          (rowIdx - 1, colIdx),
          (rowIdx, colIdx + 1),
          (rowIdx, colIdx - 1)
        )
          .filter(pos =>
            val (row, col) = pos
            val outOfBounds =
              row < 0 || row >= gardens.length || col < 0 || col >= gardens(
                0
              ).length
            outOfBounds || gardens(row)(col).regionName != regionName
          )
          .length)
      )

    area * perimeter
  )
  .sum

println(totalCost)
