def fibo(n):
    if n < 2 or n > 20:
        return n
    else:
        return  fibo(n) + fibo(n-1)



import unittest

class TestFibo(unittest.TestCase):
    def test_0(self):
        self.assertEqual(fibo(0), 0)


