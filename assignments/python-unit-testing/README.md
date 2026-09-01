# 📘 Assignment: Testing Your Code with Unit Tests

## 🎯 Objective

Learn professional testing practices by writing unit tests for Python code. You'll master test-driven development, learn to write meaningful test cases, and understand how to verify that your code works correctly. This assignment introduces industry-standard testing patterns that separate amateur from professional developers.

## 📝 Tasks

### 🛠️ Write Basic Unit Tests

#### Description
Create test cases for simple functions using Python's `unittest` framework. Practice writing assertions to verify function behavior, including normal cases and edge cases. Organize tests into a test class with multiple test methods.

#### Requirements
Completed program should:

- Import and use the `unittest` framework
- Create a test class that inherits from `unittest.TestCase`
- Write multiple test methods (test_* naming convention)
- Use assertions: `assertEqual()`, `assertTrue()`, `assertFalse()`, `assertRaises()`
- Test both expected outputs and edge cases (empty inputs, negative numbers, etc.)
- Run tests and display results with passed/failed counts
- Include at least 8 different test methods


### 🛠️ Test Functions with Multiple Scenarios

#### Description
Write comprehensive tests for more complex functions that handle different input types and conditions. Practice grouping related tests and using test fixtures to set up common test data.

#### Requirements
Completed program should:

- Write tests for functions with multiple parameters and return types
- Create setup and teardown methods using `setUp()` and `tearDown()`
- Test success cases, error cases, and boundary conditions
- Use `self.fail()` to explicitly fail tests when conditions aren't met
- Document test cases with descriptive docstrings
- Verify that functions raise appropriate exceptions for invalid input


### 🛠️ Implement Test-Driven Development

#### Description
Practice writing tests before implementing functions (TDD). Define test cases that specify expected behavior, then write functions to pass those tests. This approach ensures your code meets requirements and prevents future regressions.

#### Requirements
Completed program should:

- Write tests for a function before implementing it
- Implement the function to make all tests pass (make tests green)
- Verify all tests pass without modification
- Write tests for at least 3 different functions following TDD
- Include tests for both valid and invalid input scenarios
- Document which tests correspond to which requirements
