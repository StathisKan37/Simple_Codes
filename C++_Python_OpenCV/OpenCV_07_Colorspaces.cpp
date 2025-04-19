# include <opencv2/opencv.hpp>
# include <iostream>

int main (){
	// Reading and showing the demo image
	cv::Mat img = cv::imread("demo_image.png", cv::IMREAD_COLOR);
	cv::imshow("BGR colorspace", img);
	
	// BGR to grayscale
	cv::Mat img_gray;
	cv::cvtColor(img, img_gray, cv::COLOR_BGR2GRAY);
	cv::imshow("Grayscale colorspace", img_gray);
	
	// BGR to RGB
	cv::Mat img_rgb;
	cv::cvtColor(img, img_rgb, cv::COLOR_BGR2RGB);
	cv::imshow("RGB colorspace", img_rgb);
	
	// BGR to LAB
	cv::Mat img_lab;
	cv::cvtColor(img, img_lab, cv::COLOR_BGR2Lab);
	cv::imshow("LAB colorspace", img_lab);
	
	// BGR to YCrCb
	cv::Mat img_ycrcb;
	cv::cvtColor(img, img_ycrcb, cv::COLOR_BGR2YCrCb);
	cv::imshow("YCrCb colorspace", img_ycrcb);
	
	// BGR to HSV
	cv::Mat img_hsv;
	cv::cvtColor(img, img_hsv, cv::COLOR_BGR2HSV);
	cv::imshow("HSV colorspace", img_hsv);
	
	// Waiting for key 0 to destroy all windows
	cv::waitKey(0);
	cv::destroyAllWindows();
	
	return 0;
}
