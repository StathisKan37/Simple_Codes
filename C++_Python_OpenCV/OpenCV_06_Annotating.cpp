# include <opencv2/opencv.hpp>
# include <iostream>

int main (){
	// Reading the demo image
	cv::Mat img = cv::imread("demo_image.png", cv::IMREAD_COLOR);
	
	// Drawing a LINE
	// From (50,50) to (450,450)
	// Color: Blue (255,0,0)
	// Thickness: 6px
	cv::Point pointA(50,50);
	cv::Point pointB(450,450);
	cv::line(img, pointA, pointB, cv::Scalar(255, 0, 0), 6, 8, 0);
	
	// Drawing a CIRCLE
	// Center: (70,170)
	// Radius: 50px
	// Color: Green (0,255,0)
	// Thickness: 6px
	cv::circle(img, cv::Point(70,170), 50,  cv::Scalar(0, 255, 0), 6, 8, 0);
	
	// Drawing a FILLED CIRCLE
	// Center: (70,300)
	// Radius: 50px
	// Color: Red (0,0,255)
	cv::circle(img, cv::Point(70,300), 50,  cv::Scalar(0,0,255), -1, 8, 0);
	
	// Drawing a RECTANGLE
	// Top-left: (130, 30)
	// Buttom-right: (450, 100)
	// Color: Magenta (255,0,255)
	// Thickness: 6px
	cv::rectangle(img, cv::Point(130,30), cv::Point(450,100), cv::Scalar(255,0,255), 6, 8, 0);

	// Drawing an ELLIPSE
	// Center: (350, 160)
	// Axis: (120, 45)
	// Angle: 0 degrees
	// Perimeter: 0-360 degrees
	// Color: Cyan (255,255,0)
	// Thickness: 6px
	cv::ellipse(img,  cv::Point(350,160),  cv::Point(120,45), 0, 0, 360, cv::Scalar(255, 255, 0), 6, 8, 0);
	
	// Drawing an HALF-ELLIPSE
	// Center: (350, 190)
	// Axis: (120, 45)
	// Angle: 0 degrees
	// Perimeter: 0-180 degrees
	// Color: Cyan (0,255,255)
	// Thickness: 6px
	cv::ellipse(img,  cv::Point(350,190),  cv::Point(120,45), 0, 0, 180, cv::Scalar(0,255,255), 6, 8, 0);
	
	// TEXT
	// Text: 'Hello World!'
	// Position: (10,470)
	// Font: 3 (FONT_HERSHEY_COMPLEX)
	// Scale: 2
	// Color: Blue (255,0,0)
	// Thickness: 3
	cv::putText(img, "Hello World!", cv::Point(10,470), 3, 2, cv::Scalar(255,0,0),3);
	
	// Alternative Fonts:
	// FONT_HERSHEY_SIMPLEX        = 0
	// FONT_HERSHEY_PLAIN          = 1
	// FONT_HERSHEY_DUPLEX         = 2
	// FONT_HERSHEY_COMPLEX        = 3
	// FONT_HERSHEY_TRIPLEX        = 4
	// FONT_HERSHEY_COMPLEX_SMALL  = 5
	// FONT_HERSHEY_SCRIPT_SIMPLEX = 6
	// FONT_HERSHEY_SCRIPT_COMPLEX = 7
	// FONT_ITALIC                 = 16
	
	// Showing the drawed image
	cv::imshow("Drawed image", img);
	
	// Waiting for key 0 to destroy all windows
	cv::waitKey(0);
	cv::destroyAllWindows();
	
	return 0;
}
