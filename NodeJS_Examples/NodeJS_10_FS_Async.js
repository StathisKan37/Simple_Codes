// Importing 2 methods from fs module
// 1. readFile
// 2. writeFile
const {readFile, writeFile} = require('fs');

// Reading the first .txt file
readFile('./Other_files/Test_1.txt', 'utf8', (err, result) => {
	// Printing the error if exists
	if (err){
		console.log(err);
		return;
	};
	// Saving the content of the file in a variable
	const test_1_txt = result;
	
	// Reading the second .txt file
	readFile('./Other_files/Test_2.txt', 'utf8', (err, result) => {
		if (err){
			console.log(err);
			return;
		}
		const test_2_txt = result;
		
		//Combining the 2 .txt files into a new one
		writeFile('./Other_files/New_text.txt', `Text file 1:\n${test_1_txt}\n\nText file 2:\n${test_2_txt}`, (err, result) => {
			if (err) {
				console.log(err);
				return;
			}
			console.log(result);
		}
		);
	}
	);
}
);
