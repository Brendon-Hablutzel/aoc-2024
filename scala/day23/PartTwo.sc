import scala.collection.mutable.ListBuffer
import scala.io.Source
import scala.collection.immutable.{HashSet, HashMap}
import scala.collection.mutable

val (computers, connections) = Source.stdin.getLines.foldLeft(
  (HashSet[String](), HashMap[String, HashSet[String]]())
) { case ((computers, connections), line) =>
  val Array(first, second) = line.split("-")

  (
    computers + first + second,
    connections
      .updatedWith(first) {
        case None              => Some(HashSet(second))
        case Some(existingSet) => Some(existingSet + second)
      }
      .updatedWith(second) {
        case None              => Some(HashSet(first))
        case Some(existingSet) => Some(existingSet + first)
      }
  )
}

var cliques = ListBuffer[HashSet[String]]()

def bronKerbosch(
    currentClique: HashSet[String],
    toSearch: scala.collection.mutable.HashSet[String],
    exclude: scala.collection.mutable.HashSet[String]
): Unit =
  if (toSearch.isEmpty && exclude.isEmpty) then cliques += currentClique
  else
    val pivot = (toSearch ++ exclude).head
    val nonNeighbors = toSearch.filter(!connections(pivot).contains(_))
    for (v <- nonNeighbors) do
      bronKerbosch(
        currentClique + v,
        toSearch.intersect(connections(v)),
        exclude.intersect(connections(v))
      )

      toSearch -= v
      exclude += v

bronKerbosch(
  HashSet.empty,
  mutable.HashSet.from(computers),
  mutable.HashSet.empty
)

val largest = cliques.maxBy(_.size)

println(largest.toVector.sorted.mkString(","))
