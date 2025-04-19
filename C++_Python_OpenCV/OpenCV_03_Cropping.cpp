# include <opencv2/opencv.hpp>
# include <iostream>

int main (){
	// Reading and showing the demo image
	cv::Mat img = cv::imread("demo_image.png", cv::IMREAD_COLOR);
	cv::imshow("Demo image", img);
	
	// Cropping the image and saving it in the Mat 'img_crop'
	cv::Mat img_crop = img(cv::Range(65,430),cv::Range(10,375));
	
	// Display the cropped image
	cv::imshow("Cropped Image", img_crop);
	
	// Waiting for key 0 to destroy all windows
	cv::waitKey(0);
	cv::destroyAllWindows();
	
	return 0;
}
