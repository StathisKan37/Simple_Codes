fun main(){
	// Definning an array
	val cars = arrayOf("Fiat Panda", "Hyundai i20", "Kia Ceed", "Suzuki Swift", "Toyota Yaris")
	
	println("There are " + cars.size + " cars:")
	
	// Printing all cars
	for (i in cars){
		println(i)}
		
	// Searching for Hyundai i20
	if ("Hyundai i20" in cars){
		println("Hyundai i20 exists in the list")}
}
