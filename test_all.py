from main import check
import unittest

class TestAOC2019_04(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(2, check(12))
        self.assertEqual(2, check(14))
        self.assertEqual(654, check(1969))
        self.assertEqual(33583, check(100756))

if __name__ == '__main__':
    unittest.main()
