fun stringConcat(): String {
  val frase = "Kotlin é uma linguagem"
  return "\n$frase TOP!"
}

fun tryCatch(args: Any): Any {
  try {
    args.toString().toInt()
  }catch (e: NumberFormatException) {
    return "\nEssa String não pode ser convertido para numero"
  }catch (e: Exception) {
    return "\n" + e.message
  }
  return "\n$args"
}

fun multiplica(numeros: Array<Int>) = "\nResultado: " + (numeros[0] * numeros[1])

fun main() {
  print(stringConcat())
  print(imutableVariable())
  print(mutableVariable())
  print(multiplica(arrayOf<Int>(1, 10)))
  print(tryCatch("asdasd"))
}