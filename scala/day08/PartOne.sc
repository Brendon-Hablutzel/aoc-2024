import scala.util.{Try, Failure, Success}
import scala.io.Source
import scala.collection.immutable.HashMap

case class Cell(val rowIdx: Int, val colIdx: Int, val value: Char)

// read input
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

// make a map of antenna freq => locations
val antennas =
  map.flatten.foldLeft(HashMap[Char, Vector[Cell]]())((antennasMap, cell) =>
    cell.value match
      case '.' => antennasMap
      case antenna =>
        val newEntry =
          (antenna, antennasMap.getOrElse(antenna, Vector()) :+ cell)
        antennasMap + newEntry
  )

def getPos(map: Vector[Vector[Cell]], position: (Int, Int)): Option[Cell] =
  map.lift(position._1).map(_.lift(position._2)).flatten

def getAntinodes(
    map: Vector[Vector[Cell]],
    antennaA: Cell,
    antennaB: Cell
): Try[(Option[Cell], Option[Cell])] =
  val rowDist = (antennaB.rowIdx - antennaA.rowIdx).abs
  val colDist = (antennaB.colIdx - antennaA.colIdx).abs

  if antennaA.rowIdx > antennaB.rowIdx && antennaA.colIdx > antennaB.colIdx then
    Success(
      (
        getPos(map, (antennaB.rowIdx - rowDist, antennaB.colIdx - colDist)),
        getPos(map, (antennaA.rowIdx + rowDist, antennaA.colIdx + colDist))
      )
    )
  else if antennaB.rowIdx > antennaA.rowIdx && antennaB.colIdx > antennaA.colIdx
  then
    Success(
      (
        getPos(map, (antennaA.rowIdx - rowDist, antennaA.colIdx - colDist)),
        getPos(map, (antennaB.rowIdx + rowDist, antennaB.colIdx + colDist))
      )
    )
  else if antennaA.rowIdx > antennaB.rowIdx && antennaB.colIdx > antennaA.colIdx
  then
    Success(
      (
        getPos(map, (antennaA.rowIdx + rowDist, antennaA.colIdx - colDist)),
        getPos(map, (antennaB.rowIdx - rowDist, antennaB.colIdx + colDist))
      )
    )
  else if antennaB.rowIdx > antennaA.rowIdx && antennaA.colIdx > antennaB.colIdx
  then
    Success(
      (
        getPos(map, (antennaB.rowIdx + rowDist, antennaB.colIdx - colDist)),
        getPos(map, (antennaA.rowIdx - rowDist, antennaA.colIdx + colDist))
      )
    )
  else Failure(UnsupportedOperationException("invalid configuration of nodes"))

val antinodes = scala.collection.mutable.HashSet[Cell]()
for (antenna, locations) <- antennas do
  for c <- locations.combinations(2) do
    val (a1, a2) = getAntinodes(map, c(0), c(1)).get
    a1 match
      case Some(v) => antinodes.add(v)
      case None    => // nothing
    a2 match
      case Some(v) => antinodes.add(v)
      case None    => // nothing
println(antinodes.size)
