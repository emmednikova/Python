import unittest

def number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum == i
    return sum == num

class Test(unittest.TestCase):
    def test_num(self):
        self.assertEqual(number(26), True)

if __name__ == '__main__':
    unittest.main()