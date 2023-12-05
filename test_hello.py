import unittest

# Import the module that contains the functions you want to test
import my_module


class MyModuleTests(unittest.TestCase):
    def test_add_numbers(self):
        result = my_module.add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_multiply_numbers(self):
        result = my_module.multiply_numbers(4, 5)
        self.assertEqual(result, 20)

    def test_divide_numbers(self):
        result = my_module.divide_numbers(10, 2)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
