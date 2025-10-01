<ul>
<li>To run any <b>python code</b> named 'Python_code.py' type:</li>
<br>$ python3 Python_code.py
<hr>
<li>To compile and run a <b>C++</b> code from a file named 'C++_code.cpp' to a file named 'test' type:</li>
<br>$ g++ C++_code.cpp -o test
<br>$ ./test
<hr>
<li>To compile and run an <b>OpenCV C++</b> code from a file named 'C++_OpenCV.cpp' to a file named 'test' type:</li>
<br>$ g++ C++_OpenCV.cpp -o test `pkg-config --cflags --libs opencv4`
<br>$ ./test
<hr>
<li>To compile and run a <b>Kotlin</b> code from a file named 'Kotlin_code.kt' to a file named 'test.jar' type:</li>
<br>$ kotlin Kotlin_code.kt -include-runtime -d test.jar
<br>$ java -jar test.jar
<hr>
<li>To run a <b>PHP</b> file named 'index.php' in the terminal, type:</li>
<p>$ php -f index.php</p>
<li>To run a <b>PHP</b> file named 'index.php' in the browser, type:</li>
<p>$ php -S localhost:8000</p>
</ul>
