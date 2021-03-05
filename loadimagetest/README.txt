To build and execute loadimage, I ran these commands in the terminal: 

g++ $(pkg-config --cflags --libs /usr/local/Cellar/opencv/4.5.1_2/lib/pkgconfig/opencv4.pc) -std=c++11 loadimage.cpp -o loadimage
./loadimage

The pkgconfig is dependent on where you install openCV on your computer. The general format is "g++ $(pkg-config --cflags --libs opencv) -std=c++11  yourFile.cpp -o yourFileProgram". 'opencv' might have to be replaced path/to/opencv.pc (wherever your opencv.pc file is located, mine was /usr/local/Cellar/opencv/4.5.1_2/lib/pkgconfig/opencv4.pc).