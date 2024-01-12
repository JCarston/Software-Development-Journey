import unittest
from food import eat
class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self): #Test One
        self.assertEqual(
            eat("broccoli", is_healthy=True), #Behavior that is expected
            "I'm eating broccoli, because my body is a temple.", #Expected Response
        )
    def test_eat_unhealthy(self): #Test Two
        self.assertEqual(
            eat("pizza", is_healthy=False), #Behavior that is expected
            "I'm eating pizza, because YOLO!" #Expected Response
        )
if __name__ == "__main__":
    unittest.main()