#include <chrono>
#include <fstream>
#include <opencv2/opencv.hpp>
#include <sstream>
#include <stdio.h>

// Read an image from the camera
static cv::Mat GetImageFromCamera(cv::VideoCapture& camera)
{
    cv::Mat frame;
    camera >> frame;
    return frame;
}

// Read an image from a file
static cv::Mat GetImageFromFile(const std::string& filename)
{
    return cv::imread(filename);
}

int main(int argc, char** argv)
{
	cv::VideoCapture camera(0);

	while ((cv::waitKey(1) & 0xFF) != 27)
    {
        // Get an image from the camera. (Alternatively, call GetImageFromFile to read from file)
        //cv::Mat image = GetImageFromCamera(camera);
        cv::Mat image = GetImageFromCamera(camera);


        // Display the image
        cv::imshow("SimpleSort", image);


        ////// call model ///////




        ////////////////////////
    }


	return 0;
}
