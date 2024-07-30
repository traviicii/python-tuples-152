import unittest

from whiteboard import solution

class MatchTestCase(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(solution("RaceCar"),True)
    def test_example_two(self):
        self.assertEqual(solution("mom"),True)
    def test_example_three(self):
        self.assertEqual(solution("Shoha"),False)
    def test_taco(self):
        self.assertEqual(solution("TacoCat"),True)

if __name__ == '__main__':
    unittest.main()