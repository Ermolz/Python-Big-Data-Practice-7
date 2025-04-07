import os
import unittest
import io
from contextlib import redirect_stdout
from app.io.output import print_to_console, write_to_file


class TestOutputFunctions(unittest.TestCase):
    def test_print_to_console(self):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            print_to_console("Test message")
        self.assertEqual(captured_output.getvalue().strip(), "Test message")

    def test_write_to_file(self):
        test_path = "test_output.txt"
        test_text = "File output test"

        write_to_file(test_path, test_text)

        with open(test_path, "r", encoding="utf-8") as f:
            content = f.read()

        os.remove(test_path)
        self.assertEqual(content, test_text)

if __name__ == "__main__":
    unittest.main()
