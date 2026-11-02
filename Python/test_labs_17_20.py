import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parent


def load(lab):
    spec = importlib.util.spec_from_file_location(f"lab{lab}", ROOT / f"Lab_{lab}" / "solution.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(lab, inputs, directory):
    result = subprocess.run(
        [sys.executable, str(ROOT / f"Lab_{lab}" / "solution.py")],
        input=inputs, text=True, capture_output=True, cwd=directory, timeout=10,
    )
    if result.returncode:
        raise AssertionError(result.stderr)
    return result.stdout


class LabsTest(unittest.TestCase):
    def test_student_results_and_duplicate(self):
        lab = load(17)
        self.assertEqual(lab.calculate_results([88, 91, 84]), (263, 263 / 3))
        records = {}
        with contextlib.redirect_stdout(io.StringIO()):
            lab.add_student(records, "104", "Neha", [88, 91, 84])
            lab.add_student(records, "104", "Replacement", [0, 0, 0])
            lab.add_student(records, "105", "Invalid", [101, 0, 0])
        self.assertEqual(records, {"104": {"Name": "Neha", "Marks": [88, 91, 84]}})

    def test_student_cli(self):
        with tempfile.TemporaryDirectory() as directory:
            output = run(17, "invalid\n1\n2\n104\nNeha\nwrong\n101\n88\n91\n84\n3\n104\n3\n999\n2\n101\n4\n", directory)
        self.assertIn("Total Students: 3", output)
        self.assertIn("Average: 87.67%", output)
        self.assertIn("No student found", output)
        self.assertIn("must be non-empty and unique", output)
        self.assertIn("Goodbye!", output)

    def test_recursion(self):
        lab = load(18)
        self.assertEqual(lab.factorial(0), 1)
        self.assertEqual(lab.factorial(5), 120)
        self.assertEqual([lab.fibonacci(i) for i in range(8)], [0, 1, 1, 2, 3, 5, 8, 13])
        with tempfile.TemporaryDirectory() as directory:
            output = run(18, "9\n1\n-1\n1\nabc\n1\n0\n1\n5\n2\n8\n2\n0\n2\n31\n1\n501\n3\n", directory)
        self.assertIn("(0!) = 1", output)
        self.assertIn("(5!) = 120", output)
        self.assertIn("[0, 1, 1, 2, 3, 5, 8, 13]", output)
        self.assertIn("(0 terms): []", output)
        self.assertIn("0 to 30", output)

    def test_notes_missing_write_read_and_overwrite(self):
        lab = load(19)
        with tempfile.TemporaryDirectory() as directory:
            filename = Path(directory) / "notes.txt"
            self.assertIn("No notes file", lab.read_notes(filename))
            with contextlib.redirect_stdout(io.StringIO()):
                lab.write_notes(filename, "पहली note")
                lab.write_notes(filename, "replacement")
            self.assertEqual(lab.read_notes(filename), "replacement")
            output = run(19, "2\n1\nFinal note\n2\n9\n3\n", directory)
            self.assertEqual(filename.read_text(), "Final note")
            self.assertIn("Final note", output)

    def test_notes_file_errors(self):
        lab = load(19)
        with tempfile.TemporaryDirectory() as directory:
            self.assertIn("[ERROR]", lab.read_notes(directory))
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                lab.write_notes(directory, "note")
            self.assertIn("[ERROR]", output.getvalue())

    def test_log_preserves_entries_between_runs(self):
        with tempfile.TemporaryDirectory() as directory:
            output = run(20, "1\n02:15 PM - Network security patch applied.\n2\n3\n", directory)
            filename = Path(directory) / "daily_log.txt"
            first = filename.read_text()
            self.assertIn("Total Logged Entries: 3", output)
            self.assertTrue(first.startswith("09:00 AM - System server startup verified.\n"))
            output = run(20, "1\nFinal entry\n2\n3\n", directory)
            self.assertEqual(filename.read_text(), first + "Final entry\n")
            self.assertIn("Total Logged Entries: 4", output)

    def test_log_missing_empty_and_errors(self):
        lab = load(20)
        with tempfile.TemporaryDirectory() as directory:
            filename = Path(directory) / "daily_log.txt"
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                lab.display_log(filename)
                lab.append_entry(filename, " ")
                lab.append_entry(directory, "entry")
                lab.display_log(directory)
            self.assertFalse(filename.exists())
            self.assertIn("No log file", output.getvalue())
            self.assertEqual(output.getvalue().count("[ERROR]"), 3)


if __name__ == "__main__":
    unittest.main()
