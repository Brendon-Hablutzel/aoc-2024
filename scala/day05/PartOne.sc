import scala.collection.immutable.LinearSeq
import scala.io.Source
import scala.collection.immutable.{HashMap, HashSet}

val lines = Source.stdin.getLines()

// page -> dependencies
val dependsOn = lines
  .takeWhile(_.length > 0)
  .foldLeft(new HashMap[Int, HashSet[Int]])((map, dependencyString) =>
    val components = dependencyString.split("\\|")
    val dependency = components(0).toInt
    val page = components(1).toInt
    map + (page -> (map.getOrElse(page, HashSet()) + dependency))
  )

val updates = lines.map(line => line.split(",").map(_.toInt).toList)

def isValid(update: List[Int]): Boolean =
  def isValidHelper(
      toBeUpdatedSet: HashSet[Int],
      toBeUpdatedSeq: List[Int]
  ): Boolean =
    toBeUpdatedSeq match
      case Nil | List(_) => true
      case head :: next =>
        val thisValid = dependsOn.get(head) match
          case None => true
          case Some(dependencies) =>
            toBeUpdatedSet.intersect(dependencies).size == 0

        thisValid && isValidHelper(toBeUpdatedSet - head, next)

  isValidHelper(HashSet(update*), update)

val soln = updates
  .filter(isValid)
  .map(update =>
    val middleIdx = update.length / 2
    update(middleIdx)
  )
  .sum

println(soln)
