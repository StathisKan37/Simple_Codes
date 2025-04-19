# include <opencv2/opencv.hpp>
# include <iostream>

int main (){
	// Reading and showing the demo image
	cv::Mat img = cv::imread("demo_image.png", cv::IMREAD_COLOR);
	cv::imshow("Demo image", img);
	
	// Image Rotation
	// Angle: 45 degrees
	// Calculating the center of the image
	cv::Point2f img_center((img.cols - 1) / 2.0, (img.rows - 1) / 2.0);
	// Rotating the matrix by 45 degrees
	cv::Mat rotation_matix = cv::getRotationMatrix2D(img_center, 45, 1.0);
	// Rotating the image using warpAffine
	cv::Mat img_rot;
	cv::warpAffine(img, img_rot, rotation_matix, img.size());
	// Showing the rotated image
	cv::imshow("Rotated image", img_rot);
	
	// Waiting for key 0 to destroy all windows
	cv::waitKey(0);
	cv::destroyAllWindows();
	
	return 0;
}
