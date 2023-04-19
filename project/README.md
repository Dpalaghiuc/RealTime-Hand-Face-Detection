Video https://www.youtube.com/watch?v=JSRrC0tUrPo

Description:

This project is an implementation of real-time video hand and face detection using computer vision techniques. The project is written in Python and uses two libraries, OpenCV and Mediapipe.

The project contains a single Python script, hand_face_detection.py, which uses two methods to detect and track hands and faces in a video:

Face detection is performed using the Viola-Jones object detection framework. The framework uses a Haar feature-based cascade classifier to detect the presence of faces in an image or video frame. Hand detection is performed using the Mediapipe library. The library provides a pre-trained model for hand detection and tracking based on a convolutional neural network. The script captures video input from a webcam and displays the resulting video stream with bounding boxes drawn around detected faces and landmarks drawn on detected hands. To exit the program, click on the camera window and press the 'q' key.

Requirements:

To run this project

Install the required libraries. Open a terminal and run the following pip commands:

pip install opencv-python pip install mediapipe

This will install OpenCV and Mediapipe libraries, which are required for this project. Make sure you have Python 3.x installed on your system before executing these commands.

Running the Script: To run the script, follow these steps:

Clone the repository to your local machine Open a terminal and navigate to the project directory Run the command python project.py The script will start processing the video input from your webcam and display the resulting video stream Enjoy detecting and tracking faces and hands in real-time with this project!

Created by: Daniel Palaghiuc