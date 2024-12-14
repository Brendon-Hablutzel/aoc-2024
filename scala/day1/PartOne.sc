import scala.io.Source
import scala.collection.mutable.ListBuffer
import scala.collection.mutable.PriorityQueue
import scala.util.{Try, Success, Failure}

class DoublePQIter(val pq1: PriorityQueue[Int], val pq2: PriorityQueue[Int])
    extends Iterator[Option[(Int, Int)]] {
  override def hasNext: Boolean = pq1.length > 0 && pq2.length > 0

  override def next(): Option[(Int, Int)] =
    (Try(pq1.dequeue), Try(pq2.dequeue)) match
      case (Success(v1), Success(v2)) => Some((v2, v1))
      case _                          => None
}

val lines = Source.stdin
  .getLines()
  .map(_.split(" +"))
  .filter(_.length == 2)
  .map((a: Array[String]) => (a(0).toIntOption, a(1).toIntOption))
  .collect { case (Some(a), Some(b)) =>
    (a, b)
  }

val pq1 = PriorityQueue()(Ordering.Int.reverse)
val pq2 = PriorityQueue()(Ordering.Int.reverse)

for (a, b) <- lines do
  pq1 += a
  pq2 += b

val res = DoublePQIter(pq1, pq2).takeWhile(_.isDefined).foldLeft(0) {
  case (acc: Int, Some(value)) => acc + (value(0) - value(1)).abs
  case _                       => 0
}

println(res)
