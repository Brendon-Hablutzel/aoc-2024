import scala.collection.immutable.{HashMap, HashSet}
import scala.io.Source

def transform(num: Long): Long =
  var n = num
  n = (n ^ (n * 64)) % 16777216
  n = (n ^ (n / 32)) % 16777216
  n = (n ^ (n * 2048)) % 16777216
  n

def first2000Prices(initial: Long): Vector[Long] =
  LazyList
    .unfold((initial)) { case prev: Long =>
      Some((prev % 10, transform(prev)))
    }
    .take(2000)
    .toVector

def computeResultsMap(
    initial: Long,
    results: HashMap[(Long, Long, Long, Long), Long]
): HashMap[(Long, Long, Long, Long), Long] =
  val prices = first2000Prices(initial);

  def helper(
      diffsBought: HashSet[(Long, Long, Long, Long)],
      i: Int,
      results: HashMap[(Long, Long, Long, Long), Long]
  ): HashMap[(Long, Long, Long, Long), Long] =
    if i + 3 >= prices.length then results
    else
      val diffs = (
        prices(i) - prices(i - 1),
        prices(i + 1) - prices(i),
        prices(i + 2) - prices(i + 1),
        prices(i + 3) - prices(i + 2)
      )

      val nextPrice = prices(i + 3)

      if !diffsBought.contains(diffs) then
        helper(
          diffsBought + diffs,
          i + 1,
          results.updatedWith(diffs) {
            case None                => Some(nextPrice)
            case Some(currentResult) => Some(currentResult + nextPrice)
          }
        )
      else helper(diffsBought, i + 1, results)

  helper(HashSet(), 1, results)

val completeResults = Source.stdin.getLines
  .map(_.toLong)
  .foldLeft(HashMap[(Long, Long, Long, Long), Long]()) {
    case (map, initialNum) =>
      computeResultsMap(initialNum, map)
  }

val best = completeResults.maxBy((_, v) => v)
println(best._2)
