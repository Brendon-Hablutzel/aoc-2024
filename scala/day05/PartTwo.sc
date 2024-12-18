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

// perform a kind of bubble sort, where pages are swapped towards the end of the list
// until they come after all their dependencies
def makeUpdateValid(update: List[Int]): List[Int] =
  def bubbleOnce(update: List[Int]): List[Int] = update match
    case x :: y :: rest if !isValid(update) => y +: bubbleOnce(x :: rest)
    case x :: rest                          => x +: bubbleOnce(rest)
    case Nil                                => Nil

  def sort(update: List[Int], n: Int): List[Int] =
    if n <= 1 then update else sort(bubbleOnce(update), n - 1)

  sort(update, update.length)

val soln = updates
  .filter(!isValid(_))
  .map(makeUpdateValid)
  .map(update =>
    // since `update` is a list, this will not be O(1), but it is better than
    // converting `update` to an IndexedSeq, since here we only have to traverse
    // half of the list, while conversion would require traversing the entire list
    val middleIdx = update.length / 2
    update(middleIdx)
  )
  .sum

println(soln)
