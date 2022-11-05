import unittest
from function_def import che_list, input_n, decimal_binary, interSection


# Тест №1 к задаче №1:
class TestSplitFunction(unittest.TestCase):
    def test_che_list(self):
        self.assertEqual(che_list ('frd   hjn     hjn    trf')), ('hjn')

if __name__ == '__main__':
    unittest.main()


# Тест №2 к задаче №2:

# class TestSplitFunction(unittest.TestCase):
#     def input_n (self):
#         self.assertTrue(0)

# if __name__ == '__main__':
#     unittest.main()


# Тест №3 к задаче №3:

# class TestSplitFunction(unittest.TestCase):
#     def test_decimal_binary(self):
#          self.assertEqual(decimal_binary (2), (10))

# if __name__ == '__main__':
#      unittest.main()

# Тест №4 к задаче №4:

# class TestSplitFunction(unittest.TestCase):
#     def test_interSection(self):
#          self.assertIs((interSection ["k", "u", "o"], ["k", "h"]), ["k"])
# if __name__ == '__main__':
#     unittest.main() 