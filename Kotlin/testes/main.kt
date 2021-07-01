enum class Languages {
    PYTHON,
    JS,
    KOTLIN
}

fun MyName(): String {
    return "Oscar da Silva"
}

// Imutável 
fun MyArray(): Array<Int> {
    return arrayOf(1, 2, 3)
}

// Mutável 
fun MyArrayList(): ArrayList<Int> {
    return arrayListOf(1, 2, 3)
}

// Mutável, não ordenável e não aceita repetições
fun MyHashMap(): HashSet<String> {
    return HashSet<String>()
}

fun main() {
   val imutavel = MyName()
   print(imutavel)
   
   val my_array = MyArray()
   var my_array_list = MyArrayList()
   var my_hash_set = MyHashMap()
   
   my_array_list.add(4)
   my_array_list.addAll(arrayListOf(5, 6, 7))
   my_hash_set.add("Oscar")
   my_hash_set.add("da")
   my_hash_set.addAll(listOf("Silva", "Dondi"))
   
   print("Array: ")
   for(item in my_array) {
   	print(item)    
   }
   
   print("\nArrayList: ")
   for(item in my_array_list) {
   	print(item)    
   }
   
   print("\nHashSet: ")
   for(item in my_hash_set) {
       print(item)
   }
   
   print("\nENUM: ")
   for(lang in Languages.values()) {
       print(lang)
   }
}