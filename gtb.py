class SwapTestSuite(unittest.TestCase):
    """
        Swap Operation Test Case
    """
    def setUp(self):
        self.a = 1
        self.b = 2

    def test_swap_operations(self):
        instance = Swap(self.a,self.b)
        value1, value2 =instance.get_swap_values()
        self.assertEqual(self.a, value2)
        self.assertEqual(self.b, value1)


class OddOrEvenTestSuite(unittest.TestCase):
    """
        This is the Odd or Even Test case Suite
    """
    def setUp(self):
        self.value1 = 1
        self.value2 = 2

    def test_odd_even_operations(self):
        instance1 = OddOrEven(self.value1)
        instance2 = OddOrEven(self.value2)
        message1 = instance1.get_odd_or_even()
        message2 = instance2.get_odd_or_even()
        self.assertEqual(message1, 'Odd')
        self.assertEqual(message2, 'Even')
