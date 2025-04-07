import unittest
import pandas as pd
import os
from app.io.input import read_file_builtin, read_file_pandas


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")
TXT_PATH = os.path.join(DATA_DIR, "test_file.txt")
CSV_PATH = os.path.join(DATA_DIR, "test_file.csv")
NON_EXISTENT_TXT = os.path.join(DATA_DIR, "nonexistent.txt")
NON_EXISTENT_CSV = os.path.join(DATA_DIR, "does_not_exist.csv")

class TestInputFunctionsV2(unittest.TestCase):

    def setUp(self):
        os.makedirs(DATA_DIR, exist_ok=True)

        # Set up for read_file_builtin tests
        with open(TXT_PATH, "w", encoding="utf-8") as f:
            f.write("Hello, test!\nSecond line.")

        # Set up for read_file_pandas tests
        df = pd.DataFrame({
            "name": ["Alice", "Bob"],
            "age": [25, 30]
        })
        df.to_csv(CSV_PATH, index=False)

    def tearDown(self):
        if os.path.exists(TXT_PATH):
            os.remove(TXT_PATH)
        if os.path.exists(CSV_PATH):
            os.remove(CSV_PATH)

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

    # --- Tests for read_file_pandas ---
    def test_pandas_read_dataframe(self):
        result = read_file_pandas(CSV_PATH)
        self.assertIsInstance(result, pd.DataFrame)

    def test_pandas_read_content(self):
        df = read_file_pandas(CSV_PATH)
        self.assertEqual(df.shape, (2, 2))  # 2 rows, 2 columns

    def test_pandas_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_file_pandas(NON_EXISTENT_CSV)

if __name__ == "__main__":
    unittest.main()
