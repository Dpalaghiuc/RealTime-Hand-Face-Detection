import cv2
import project
import unittest


class TestProject(unittest.TestCase):

    def test_load_cascade(self):
        cascade = project.load_cascade()
        self.assertIsInstance(cascade, cv2.CascadeClassifier)

    def test_detect_faces(self):
        cascade = project.load_cascade()
        img = cv2.imread("test_face.jpeg")  # Use a test image with at least one face
        faces = project.detect_faces(cascade, img)
        self.assertTrue(len(faces) > 0)

    def test_detect_hands(self):
        img = cv2.imread("test_hand.jpeg")  # Use a test image with at least one hand
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results, _ = project.detect_hands(img)
        self.assertTrue(results.multi_hand_landmarks)


if __name__ == '__main__':
    unittest.main()
