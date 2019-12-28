from main import check
import unittest

class TestAOC2019_04(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(2, check(12))
        self.assertEqual(2, check(14))
        self.assertEqual(966, check(1969))
        self.assertEqual(50346, check(100756))

if __name__ == '__main__':
    unittest.main()
