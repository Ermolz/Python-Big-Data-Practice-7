import unittest
import io
from contextlib import redirect_stdout
from app.io.output import print_to_console

class TestOutputFunctions(unittest.TestCase):
    def test_print_to_console(self):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            print_to_console("Test message")
        self.assertEqual(captured_output.getvalue().strip(), "Test message")

if __name__ == "__main__":
    unittest.main()
