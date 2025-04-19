# include <opencv2/opencv.hpp>
# include <iostream>

int main (){
	// Reading and showing the demo image
	cv::Mat img = cv::imread("demo_image.png", cv::IMREAD_COLOR);
	cv::imshow("Demo image", img);
	
	// Image bluring
	cv::Mat img_blur;
	cv::blur(img, img_blur, cv::Size(5,5));
	cv::imshow("Blured image", img_blur);
	
	// Gaussian image bluring
	cv::Mat img_gus;
	cv::GaussianBlur(img, img_gus, cv::Size(5,5), 0, 0);
	cv::imshow("Gaussian blured image", img_gus);
	
	// Median bluring
	cv::Mat img_med;
	cv::medianBlur(img, img_med, (5,5));
	cv::imshow("Median blured image", img_med);
	
	// Bilateral filter
	cv::Mat img_bil;
	cv::bilateralFilter(img, img_bil, 9, 75, 75);
	cv::imshow("Bilateral filtered image", img_bil);
	
	// Blurring  using Custom 2D-Convolution Kernels
	// Kernel 1:
	// [ 1, 1, 1, 1, 1]
	// [ 1, 1, 1, 1, 1]
	// [ 1, 1, 1, 1, 1]
	// [ 1, 1, 1, 1, 1]
	// [ 1, 1, 1, 1, 1]
	cv::Mat kernel_1 = cv::Mat::ones(5,5, CV_64F);
	kernel_1 = kernel_1 / 25;
	cv::Mat img_ker_1;
	cv::filter2D(img, img_ker_1, -1 , kernel_1, cv::Point(-1, -1), 0, 4);
	cv::imshow("Kernel 1 blur", img_ker_1);

	// Kernel 2:
	// [  0, -1,  0 ]
	// [ -1,  5, -1 ]
	// [  0,  1,  0 ]
	cv::Mat kernel_2 =(cv::Mat_<double>(3,3) << 0,-1, 0,-1, 5,-1, 0,-1, 0);
	cv::Mat img_ker_2;
	cv::filter2D(img, img_ker_2, -1 , kernel_2, cv::Point(-1, -1), 0, cv::BORDER_DEFAULT);
	cv::imshow("Kernel 2 blur", img_ker_2);
	
	// Waiting for key 0 to destroy all windows
	cv::waitKey(0);
	cv::destroyAllWindows();
	
	return 0;
}
