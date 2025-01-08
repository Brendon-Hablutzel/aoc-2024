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

def outOfBounds(pos: (Int, Int)) =
  val (row, col) = pos
  row < 0 || row >= gardens.length || col < 0 || col >= gardens(
    0
  ).length

val totalCost = regions
  .map(region =>
    val area = region.size
    val nCorners = region
      .foldLeft(0)((acc, position) =>
        val Cell(rowIdx, colIdx, regionName) = position

        val left = (rowIdx, colIdx - 1)
        val up = (rowIdx - 1, colIdx)
        val right = (rowIdx, colIdx + 1)
        val down = (rowIdx + 1, colIdx)

        val outerCorners = List(
          (left, up),
          (up, right),
          (right, down),
          (down, left)
        ).count(sides =>
          val (sideA, sideB) = sides
          val (rowA, colA) = sideA
          val (rowB, colB) = sideB
          (outOfBounds(sideA) || gardens(rowA)(
            colA
          ).regionName != regionName) && (outOfBounds(sideB) || gardens(rowB)(
            colB
          ).regionName != regionName)
        )

        val leftUp = (rowIdx - 1, colIdx - 1)
        val leftDown = (rowIdx + 1, colIdx - 1)
        val rightUp = (rowIdx - 1, colIdx + 1)
        val rightDown = (rowIdx + 1, colIdx + 1)

        val innerCorners = List(
          (left, up, leftUp),
          (up, right, rightUp),
          (right, down, rightDown),
          (down, left, leftDown)
        ).count(sides =>
          val (sideA, sideB, sideC) = sides
          val (rowA, colA) = sideA
          val (rowB, colB) = sideB
          val (rowC, colC) = sideC
          (!outOfBounds(sideA) && gardens(rowA)(
            colA
          ).regionName == regionName) && (!outOfBounds(sideB) && gardens(rowB)(
            colB
          ).regionName == regionName) && (outOfBounds(sideC) || gardens(rowC)(
            colC
          ).regionName != regionName)
        )

        acc + outerCorners + innerCorners
      )

    area * nCorners
  )
  .sum

println(totalCost)
