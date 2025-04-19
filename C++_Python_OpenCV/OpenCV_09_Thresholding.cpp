# include <opencv2/opencv.hpp>
# include <iostream>

int main (){
	// Reading and showing the demo image
	cv::Mat img = cv::imread("demo_image.png", cv::IMREAD_GRAYSCALE);
	cv::imshow("Grayscale demo image", img);
	
	// Thresh: 127
	// Max Value: 255

	// Binary Threshold
	cv::Mat img_bin;
	cv::threshold(img, img_bin, 127, 255, cv::THRESH_BINARY);
	cv::imshow("Binary threshold (thresh:127, max:255)", img_bin);

	// Inverse Binary Threshold
	cv::Mat img_inv_bin;
	cv::threshold(img, img_inv_bin, 127, 255, cv::THRESH_BINARY_INV);
	cv::imshow("Inverse binary threshold (thresh:127, max:255)", img_inv_bin);

	// Truncate Threshold
	cv::Mat img_trun;
	cv::threshold(img, img_trun, 127, 255, cv::THRESH_TRUNC);
	cv::imshow("Truncate threshold (thresh:127, max:255)", img_trun);

	// Threshold to zero
	cv::Mat img_zero;
	cv::threshold(img, img_zero, 127, 255, cv::THRESH_TOZERO);
	cv::imshow("Threshold to zero (thresh:127, max:255)", img_zero);

	// Inverted Threshold to zero
	cv::Mat img_inv_zero;
	cv::threshold(img, img_inv_zero, 127, 255, cv::THRESH_TOZERO_INV);
	cv::imshow("Inverted threshold to zero (thresh:127, max:255)", img_inv_zero);
	
	// Waiting for key 0 to destroy all windows
	cv::waitKey(0);
	cv::destroyAllWindows();
	
	return 0;
}
