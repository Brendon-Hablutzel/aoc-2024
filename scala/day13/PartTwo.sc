import scala.collection.mutable.HashMap
import scala.collection.mutable.ArrayBuffer
import scala.io.Source

val buttonACost = 3
val buttonBCost = 1

val modifier = 10000000000000L

val buttonPattern = "Button [AB]: X\\+(\\d+), Y\\+(\\d+)".r
val prizePattern = "Prize: X\\=(\\d+), Y\\=(\\d+)".r

def parseButton(line: String): (Int, Int) = line match {
  case buttonPattern(x, y) => (x.toInt, y.toInt)
}

def parsePrize(line: String): (Int, Int) = line match {
  case prizePattern(x, y) => (x.toInt, y.toInt)
}

def bestPresses(
    buttonA: (Int, Int),
    buttonB: (Int, Int),
    prize: (Long, Long)
): (Double, Double) =
  val (aX, aY) = buttonA
  val (bX, bY) = buttonB
  val (prizeX, prizeY) = prize

  val detA = (aX * bY - bX * aY).toDouble

  val detAOfb1 = prizeX * bY - bX * prizeY

  val detAOfb2 = aX * prizeY - aY * prizeX

  (detAOfb1 / detA, detAOfb2 / detA)

val lines = Source.stdin.getLines()
val ans = lines
  .grouped(4)
  .foldLeft(0L)((acc, lines) =>
    val Seq(buttonALine, buttonBLine, prizeLine, _) = lines
    val buttonA = parseButton(buttonALine)
    val buttonB = parseButton(buttonBLine)
    val (prizeOriginalX, prizeOriginalY) = parsePrize(prizeLine)
    val prize = (prizeOriginalX + modifier, prizeOriginalY + modifier)

    val (aPresses, bPresses) = bestPresses(buttonA, buttonB, prize)

    if aPresses % 1 == 0 && bPresses % 1 == 0 then
      acc + (aPresses.toLong * buttonACost + bPresses.toLong * buttonBCost)
    else acc
  )

println(ans)
