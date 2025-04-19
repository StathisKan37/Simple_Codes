// Including the 2 usefull libraries
#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
	
    // Print OpenCV version
    std::cout << "OpenCV Version: " << CV_VERSION << std::endl;
    
    // Reading the demo image and saving it in the Mat 'img'
	cv::Mat img = cv::imread("demo_image.png", cv::IMREAD_COLOR);
	
	// Reading the demo image in grayscale and saving it
	cv::Mat img_gray = cv::imread("demo_image.png", cv::IMREAD_GRAYSCALE);

    // Alternatively:
	// IMREAD_COLOR: 1
	// IMREAD_GRAYSCALE: 0
	// IMREAD_UNCHANGED: -1

	// Create a window.
	cv::namedWindow( "Demo image", cv::WINDOW_AUTOSIZE );
	cv::namedWindow( "Grayscale image", cv::WINDOW_AUTOSIZE );

	// Show the image inside it.
	cv::imshow( "Demo image", img ); 
	cv::imshow( "Grayscale image", img_gray ); 
 
	// Wait for a keystroke.   
	cv::waitKey(0);  
 
	// Destroys all the windows created                         
	cv::destroyAllWindows();
	
    return 0;
}
