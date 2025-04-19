# include <opencv2/opencv.hpp>
# include <iostream>

int main (){
	// Reading and showing the demo image in grayscale
	cv::Mat img = cv::imread("demo_image.png", cv::IMREAD_COLOR);
	cv::imshow("Grayscale demo image", img);
 
    // Converting to Grayscale
    cv::Mat img_gray;
	cv::cvtColor(img, img_gray, cv::COLOR_BGR2GRAY);
	
	// Binary Threshold
	cv::Mat img_thresh;
	cv::threshold(img_gray, img_thresh, 150, 255, cv::THRESH_BINARY);
	cv::imshow("Thresholded image", img_thresh);
	
	// DETECTING CONTOURS

	// CHAIN_APPROX_NONE
	std::vector<std::vector<cv::Point>> contours_1;
	std::vector<cv::Vec4i> hierarchy_1;
	cv::findContours(img_thresh, contours_1, hierarchy_1, cv::RETR_TREE, cv::CHAIN_APPROX_NONE);
	// Copying the demo image
	cv::Mat img_approx_none = img.clone();
	// Drawing the contours
	// ContourIdx: -1
	// Color: Green (0, 255, 0)
	// Thickness: 2
	cv::drawContours(img_approx_none, contours_1, -1, cv::Scalar(0, 255, 0), 2);
	cv::imshow("None approximation", img_approx_none);

	// CHAIN_APPROX_SIMPLE
	std::vector<std::vector<cv::Point>> contours_2;
	std::vector<cv::Vec4i> hierarchy_2;
	cv::findContours(img_thresh, contours_2, hierarchy_2, cv::RETR_TREE, cv::CHAIN_APPROX_SIMPLE);
	// Copying the demo image
	cv::Mat img_approx_simple = img.clone();
	// Drawing the contours
	cv::drawContours(img_approx_simple, contours_2, -1, cv::Scalar(0, 255, 0), 2);
	cv::imshow("Simple approximation", img_approx_simple);

	// Contour detecting modes
	// RETR_TREE
	// RETR_LIST
	// RETR_EXTERNAL
	// RETR_CCOMP
	
	// Waiting for key 0 to destroy all windows
	cv::waitKey(0);
	cv::destroyAllWindows();
	
	return 0;
}
