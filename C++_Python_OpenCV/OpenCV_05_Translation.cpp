# include <opencv2/opencv.hpp>
# include <iostream>

int main (){
	// Reading and showing the demo image
	cv::Mat img = cv::imread("demo_image.png", cv::IMREAD_COLOR);
	cv::imshow("Demo image", img);
	
	// Getting the height and width of the image
	int img_height = img.rows;
	int img_width = img.cols;
	
	// The translation matrix
	float warp_values[] = { 1.0, 0.0, 100, 0.0, 1.0, 100 };
	cv::Mat trans_mat = cv::Mat(2, 3, CV_32F, warp_values);
	
	// Applying and showing the translation
	cv::Mat img_trans;
	warpAffine(img, img_trans, trans_mat, img.size());
	cv::imshow("Translated image", img_trans);
	
	// Waiting for key 0 to destroy all windows
	cv::waitKey(0);
	cv::destroyAllWindows();
	
	return 0;
}
