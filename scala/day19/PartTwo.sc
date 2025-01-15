import scala.compiletime.ops.double
import scala.io.Source

val lines = Source.stdin.getLines
val patterns = lines.next().split(", ").toVector
lines.next()
val desiredDesigns = lines.toVector

def numWaysPossible(design: String): Long =
  def helper(soFar: Vector[Long], n: Int): Vector[Long] =
    if n == design.length then soFar
    else
      val ways =
        for pattern <- patterns
        yield
          val patternStartIdx = n - pattern.length + 1
          if patternStartIdx >= 0 && pattern == design.substring(
              patternStartIdx,
              n + 1
            )
          then if n - pattern.length >= 0 then soFar(n - pattern.length) else 1
          else 0

      helper(soFar :+ ways.sum, n + 1)

  val vec = helper(Vector(), 0)
  vec.last

val totalWaysPossible = desiredDesigns.map(numWaysPossible).sum
println(totalWaysPossible)
