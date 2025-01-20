import scala.io.Source
import scala.collection.immutable.{HashSet, HashMap}

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

def isInterconnected(computerGroup: (String, String, String)): Boolean =
  val (a, b, c) = computerGroup

  val aConnections = connections(a)
  val bConnections = connections(b)
  val cConnections = connections(c)

  val groupSet = HashSet(a, b, c)

  groupSet.intersect(aConnections).size == 2 &&
  groupSet.intersect(bConnections).size == 2 &&
  groupSet.intersect(cConnections).size == 2

val numValidGroups = computers.toList
  .combinations(3)
  .filter(combination =>
    isInterconnected((combination(0), combination(1), combination(2)))
  )
  .filter(combination => combination.count(_.startsWith("t")) >= 1)
  .size

println(numValidGroups)
