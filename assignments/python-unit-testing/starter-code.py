import unittest

# TODO: Implement your functions to be tested here
# Example function (uncomment and modify):
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def divide(a, b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a / b


class TestBasicFunctions(unittest.TestCase):
    """Test cases for basic arithmetic functions"""
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        # TODO: Initialize any test data needed for your tests
        pass
    
    def tearDown(self):
        """Clean up after each test method"""
        # TODO: Clean up resources if needed
        pass
    
    # TODO: Write your test methods here
    # Test names must start with "test_"
    # Example:
    # def test_add_positive_numbers(self):
    #     self.assertEqual(add(2, 3), 5)
    #
    # def test_add_negative_numbers(self):
    #     self.assertEqual(add(-2, -3), -5)
    #
    # def test_divide_by_zero_raises_error(self):
    #     with self.assertRaises(ValueError):
    #         divide(10, 0)


class TestEdgeCases(unittest.TestCase):
    """Test cases for edge cases and boundary conditions"""
    
    # TODO: Write test methods for edge cases
    # Examples:
    # def test_empty_input_handling(self):
    #     pass
    #
    # def test_large_numbers(self):
    #     pass
    #
    # def test_type_validation(self):
    #     with self.assertRaises(TypeError):
    #         add("string", 5)


class TestTDD(unittest.TestCase):
    """Test-driven development: Write tests before implementing functions"""
    
    # TODO: Write test cases that specify expected behavior
    # Then implement the functions to make these tests pass
    # Example:
    # def test_square_function(self):
    #     self.assertEqual(square(5), 25)
    #     self.assertEqual(square(0), 0)
    #     self.assertEqual(square(-3), 9)


if __name__ == '__main__':
    # Run all tests and display results
    unittest.main()
