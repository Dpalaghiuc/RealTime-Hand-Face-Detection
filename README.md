# RealTime-Hand-Face-Detection
# CS50P Final Project

[![YouTube Video Link](https://img.shields.io/badge/YouTube-Video-red)](https://www.youtube.com/watch?v=JSRrC0tUrPo&t=3s)

## Description

This project is an implementation of real-time video hand and face detection using computer vision techniques. The project is written in Python and uses two libraries, OpenCV and Mediapipe.

The project contains a single Python script, `project.py`, which uses two methods to detect and track hands and faces in a video:

- Face detection is performed using the Viola-Jones object detection framework. The framework uses a Haar feature-based cascade classifier to detect the presence of faces in an image or video frame.
- Hand detection is performed using the Mediapipe library. The library provides a pre-trained model for hand detection and tracking based on a convolutional neural network.

The script captures video input from a webcam and displays the resulting video stream with bounding boxes drawn around detected faces and landmarks drawn on detected hands. To exit the program, click on the camera window and press the 'q' key.

## Requirements

To run this project:

1. Install the required libraries. Open a terminal and run the following pip commands:

```bash
pip install opencv-python
pip install mediapipe


This will install OpenCV and Mediapipe libraries, which are required for this project. Make sure you have Python 3.x installed on your system before executing these commands.

## Running the Script
To run the script, follow these steps:

1. Clone the repository to your local machine
2. Open a terminal and navigate to the project directory
3. Run the command `python hand_face_detection.py`
4. The script will start processing the video input from your webcam and display the resulting video stream
5. Enjoy detecting and tracking faces and hands in real-time with this project!
6. To exit the program, click on the camera window and press the 'q' key.

## Unit Tests

The `test_project.py` file contains unit tests for the project. The tests cover functions such as loading the Haar cascade classifier, detecting faces, and detecting hands in the images. The test file uses the `unittest` module to perform the tests.

To run the tests, follow these steps:

1. Make sure you have the `test_face.jpeg` and `test_hand.jpeg` files in your project directory. These files should contain at least one face and one hand, respectively.
2. Open a terminal and navigate to the project directory.
3. Run the command `python test_project.py`.

The tests included in `test_project.py` are:

- `test_load_cascade`: This test checks if the Haar cascade classifier is loaded correctly.
- `test_detect_faces`: This test checks if the face detection function works correctly by detecting at least one face in the `test_face.jpeg` image.
- `test_detect_hands`: This test checks if the hand detection function works correctly by detecting at least one hand in the `test_hand.jpeg` image.


## Created by
Daniel Palaghiuc
