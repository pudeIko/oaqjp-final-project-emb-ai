from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        # Test joy
        joy = emotion_detector("I am glad this happened")
        self.assertEqual(joy["dominant_emotion"], "joy")

        # Test anger
        anger = emotion_detector("I am really mad about this")
        self.assertEqual(anger["dominant_emotion"], "anger")

        # Test disgust
        disgust = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(disgust["dominant_emotion"], "disgust")

        # Test sadness
        sadness = emotion_detector("I am so sad about this")
        self.assertEqual(sadness["dominant_emotion"], "sadness")

        # Test fear
        fear = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(fear["dominant_emotion"], "fear")


unittest.main()