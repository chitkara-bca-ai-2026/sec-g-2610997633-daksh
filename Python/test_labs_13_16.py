import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent


def run_lab(number, inputs):
    with tempfile.TemporaryDirectory() as directory:
        result = subprocess.run(
            [sys.executable, str(ROOT / f"Lab_{number}" / "solution.py")],
            input=inputs, text=True, capture_output=True, cwd=directory, timeout=5,
        )
    if result.returncode:
        raise AssertionError(result.stderr)
    return result.stdout


class LabsTest(unittest.TestCase):
    def test_inventory_operations(self):
        output = run_lab(13, "bad\n1\n2\nMarker\n4\n3\nPen\n3\nMissing\n2\n\n1\n5\n")
        self.assertIn("1. Eraser\n2. Marker\n3. Notebook\n4. Pen\n5. Ruler", output)
        self.assertIn('"Pen" removed', output)
        self.assertIn("Item not found", output)
        self.assertIn("Item name cannot be empty", output)
        self.assertIn("Choose a number from 1 to 5", output)
        self.assertIn("1. Eraser\n2. Marker\n3. Notebook\n4. Ruler", output)

    def test_library_operations(self):
        output = run_lab(14, "1\n2\nNew Book\nAuthor\n2026\nRobotics\n3\n4\nRobotics\n4\nMachine Learning\n5\n2\n\nAuthor\n2026\nAI\n4\n\nbad\n1\n6\n")
        self.assertIn("Total Books: 5", output)
        self.assertIn("Total Unique Genres: 4", output)
        self.assertIn("Already in Stock (Intersection &): ['AI', 'Robotics']", output)
        self.assertIn("Purchase Order Needed (Difference -): ['Cloud Computing', 'Cybersecurity', 'Machine Learning']", output)
        self.assertIn("All book fields are required", output)
        self.assertIn("Category cannot be empty", output)

    def test_student_operations_and_validation(self):
        output = run_lab(15, "1\n2\n102\n2\n999\n3\n101\n3\n104\nNeha\nBCA AI\n1\nabc\n101\n40\n40\n40\n4\n104\n2\n2\n2\n104\n5\n104\n6\n103\n6\n999\n1\n7\n")
        self.assertIn("Roll Number must be non-empty and unique", output)
        self.assertIn("Enter a whole number from 0 to 100", output)
        self.assertIn("Semester: 2", output)
        self.assertIn("Total Marks: 120 / 300", output)
        self.assertIn("Average Marks: 40.00%", output)
        self.assertIn("Final Result: PASS", output)
        self.assertIn("Record for 'Karan'", output)
        self.assertIn("Total Enrolled Students: 3", output)

    def test_student_failure_result(self):
        output = run_lab(15, "3\n104\nNeha\nBCA AI\n1\n39\n39\n39\n5\n104\n7\n")
        self.assertIn("Final Result: FAIL", output)

    def test_calculator_functions(self):
        spec = importlib.util.spec_from_file_location("calculator", ROOT / "Lab_16" / "solution.py")
        calculator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(calculator)
        self.assertEqual(calculator.add(25, 15), 40)
        self.assertEqual(calculator.subtract(50, 18.5), 31.5)
        self.assertEqual(calculator.multiply(-3, 2), -6)
        self.assertEqual(calculator.divide(9, 2), 4.5)
        self.assertIsNone(calculator.divide(1, 0))
        self.assertIsNone(calculator.modulus(1, 0))
        self.assertEqual(calculator.modulus(9, 2), 1)
        self.assertEqual(calculator.power(3), 9)
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.format_number(3.0), 3)

    def test_calculator_cli_history_and_bad_inputs(self):
        output = run_lab(16, "7\nx\n1\nwrong\n25\n15\n2\n50\n18.5\n3\n3\n2\n4\n9\n2\n5\n9\n2\n4\n1\n0\n5\n1\n0\n6\n3\n\n6\n2\n3\n6\n0\n-1\n6\n-2\n0.5\n6\n1e308\n2\n7\n8\n")
        self.assertIn("No calculations yet", output)
        self.assertIn("Enter a finite number", output)
        self.assertIn("Cannot divide or take modulus by zero", output)
        self.assertIn("Power is undefined", output)
        self.assertIn("Result is too large", output)
        self.assertIn("1. 25 + 15 = 40", output)
        self.assertIn("7. 2 ** 3 = 8", output)
        self.assertIn("3 ** 2 = 9", output)


if __name__ == "__main__":
    unittest.main()
