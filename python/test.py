import unittest
# Create your tests here.
class TestSumFunction(unittest.TestCase):
    
    def test_sum_positive_numbers(self):
        self.assertEqual(sum(1, 2), 5)

def sum(a,b):
    return a+b

if __name__ == '__main__':
    unittest.main()
