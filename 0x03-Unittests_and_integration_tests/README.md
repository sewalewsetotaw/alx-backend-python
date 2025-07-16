# 0x03. Unittests and Integration Tests

## 🎯 Purpose of the Project

The purpose of this project is to gain a deep understanding of **automated testing in Python**, focusing on:

- Writing **unit tests** for individual functions and methods
- Writing **integration tests** to ensure multiple components work together
- Using tools like `unittest`, `parameterized`, and `mock` to:
  - Validate functionality
  - Catch bugs early
  - Improve code reliability
- Practicing proper **test coverage**, **mocking external APIs**, and **using fixtures** to isolate logic
- Ensuring that all code complies with **PEP8 style** using `pycodestyle` (version 2.5)

---

## 🧪 How to Run the Tests

### 1. Install Dependencies

Make sure you have the required packages installed:

```bash
pip install parameterized requests

    ⚠️ You must use Python 3.7 as required by the project specification.

2. Run a Specific Test File

Example: run unit tests for utils.py:

python3 -m unittest test_utils.py

3. Run All Tests in the Project

python3 -m unittest discover

This will find and execute all test files that match the test*.py naming pattern.

```
