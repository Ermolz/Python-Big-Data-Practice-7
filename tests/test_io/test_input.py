import unittest
import os
from app.io.input import read_file_builtin


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")
TXT_PATH = os.path.join(DATA_DIR, "test_file.txt")
NON_EXISTENT_TXT = os.path.join(DATA_DIR, "nonexistent.txt")

class TestInputFunctionsV1(unittest.TestCase):

    def setUp(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(TXT_PATH, "w", encoding="utf-8") as f:
            f.write("Hello, test!\nSecond line.")

    def tearDown(self):
        if os.path.exists(TXT_PATH):
            os.remove(TXT_PATH)

    # --- Tests for read_file_builtin ---
    def test_builtin_read_content(self):
        result = read_file_builtin(TXT_PATH)
        self.assertIn("Hello, test!", result)

    def test_builtin_read_is_string(self):
        result = read_file_builtin(TXT_PATH)
        self.assertIsInstance(result, str)

    def test_builtin_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_file_builtin(NON_EXISTENT_TXT)

if __name__ == "__main__":
    unittest.main()
