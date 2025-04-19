# include <opencv2/opencv.hpp>
# include <iostream>

int main (){
	// Reading and showing the demo image in grayscale
	cv::Mat img = cv::imread("demo_image.png", cv::IMREAD_GRAYSCALE);
	cv::imshow("Grayscale demo image", img);
 
    // Blurring the demo image
    cv::Mat img_blur;
    cv::GaussianBlur(img, img_blur, cv::Size(3,3), 0);
	
	// Sobel Edge Detection on the X axis
	cv::Mat img_sobelX;
	cv::Sobel(img_blur, img_sobelX, CV_64F, 1, 0, 5);
	cv::imshow("Sobel X Edge detection", img_sobelX);

	// Sobel Edge Detection on the Y axis
	cv::Mat img_sobelY;
	cv::Sobel(img_blur, img_sobelY, CV_64F, 0, 1, 5);
	cv::imshow("Sobel Y Edge detection", img_sobelY);

	// Sobel Edge Detection on the X and Y axis
	cv::Mat img_sobelXY;
	cv::Sobel(img_blur, img_sobelXY, CV_64F, 1, 1, 5);
	cv::imshow("Sobel X and Y Edge detection", img_sobelXY);
 
    // Canny Edge Detection
	cv::Mat img_canny;
    cv::Canny(img_blur, img_canny, 50, 150, 3, false);
	cv::imshow("Canny edge detection", img_canny);
	
	// Waiting for key 0 to destroy all windows
	cv::waitKey(0);
	cv::destroyAllWindows();
	
	return 0;
}
