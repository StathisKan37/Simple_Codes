// Including the 2 usefull libraries
#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    
    // Reading an 500x500 png image and saving it in the Mat 'img'
	cv::Mat img = cv::imread("demo_image.png", cv::IMREAD_COLOR);
	
	// Showing the image in the normal size
	cv::imshow( "500x500 image", img );

	// Scaling the image and shwoing the result
	// 250x250
	cv::Mat img_1;
	cv::resize(img, img_1, cv::Size(250,250), cv::INTER_LINEAR);
	cv::imshow("250x250 resized", img_1);
	// 750x750
	cv::Mat img_2;
	cv::resize(img, img_2, cv::Size(750,750), cv::INTER_LINEAR);
	cv::imshow("750x750 resized", img_2);
	
	// Waiting for key 0 to destroy all windows
	cv::waitKey(0);
	cv::destroyAllWindows();
	
    return 0;
}
