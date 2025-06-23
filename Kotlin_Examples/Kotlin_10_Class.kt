// Definning a class
class Car(var brand: String, var model: String, var year: Int)

fun main() {
  val c1 = Car("Ford", "Mustang", 1969)
  val c2 = Car("Aston Martin", "db6", 1965)
  val c3 = Car("Ferrari", "250GT", 1960)

  println(c1.brand)
  println(c2.model)
  println(c3.year)
}
