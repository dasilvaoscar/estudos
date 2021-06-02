fun concatStringArray(args: List<String>): String {
  return args.joinToString()
}

fun main() {
  val arrayTest = listOf("Oscar", "da", "Silva")
  println(concatStringArray(arrayTest))
}
