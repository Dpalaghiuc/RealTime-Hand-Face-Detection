import cv2
import mediapipe as mp
import pathlib

# Initialize Mediapipe Hands solution
mp_hands = mp.solutions.hands

def load_cascade():
    # Load the pre-trained Haar Cascade classifier for face detection
    cascade_path = pathlib.Path(cv2.__file__).parent / "data/haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(str(cascade_path))
    return cascade

def detect_faces(cascade, img):
    # Convert the image to grayscale, as Haar Cascade works with grayscale images
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Detect faces using the Haar Cascade classifier
    # scaleFactor: The factor by which the image is reduced in size at each image scale (1.3 means 30% reduction)
    # minNeighbors: The number of neighbors a candidate rectangle should have to retain it (higher value for higher quality)
    faces = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    return faces

def detect_hands(img):
    # Create a Mediapipe Hands object to detect hand landmarks
    hands = mp_hands.Hands()

    # Utility for drawing landmarks on the image
    mp_drawing = mp.solutions.drawing_utils

    # Process the image and detect hand landmarks
    results = hands.process(img)
    return results, mp_drawing

def main():
    # Load the Haar Cascade classifier for face detection
    cascade = load_cascade()

    # Open the default video camera (index 0)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a frame from the video
        success, img = cap.read()

        # If the frame was not captured successfully, exit the loop
        if not success:
            break

        # Convert the image to RGB format (required by Mediapipe)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # This is where hands code starts
        results, mp_drawing = detect_hands(img)

        # Draw landmarks on the image for detected hands
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        # This is where hands code ends

        # This is where face code starts
        faces = detect_faces(cascade, img)

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # This is where face code ends

        # Show the resulting image in a window
        cv2.imshow("Detection", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the video capture and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
