import scala.io.Source

val lines = Source.stdin.getLines
val patterns = lines.next().split(", ").toVector
lines.next()
val desiredDesigns = lines.toVector

def isDesignPossible(design: String): Boolean =
  var possible = false

  def helper(currentDesign: String): Unit =
    if possible || currentDesign.length == 0 then possible = true
    else
      for pattern <- patterns if currentDesign.startsWith(pattern) do
        helper(currentDesign.substring(pattern.length))

  helper(design)

  possible

val nPossible = desiredDesigns.count(isDesignPossible(_))
println(nPossible)
