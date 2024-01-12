import unittest
from food import eat, nap
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
    def test_short_nap(self):
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )
    def test_long_nap(self):
        self.assertEqual(
            nap(3),
            "Ugh I overslepft. I didn't mean to nap so long"
        )
                
        
if __name__ == "__main__":
    unittest.main()