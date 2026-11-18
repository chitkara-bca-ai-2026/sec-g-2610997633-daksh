# Lab 23 - File Handling Tool
import os


def ensure_sample_file(filename="student_marks.txt"):
    if not os.path.exists(filename):
        sample_data = "Aman,85\nRiya,92\nKaran,78\n"
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(sample_data)
        except OSError as error:
            print(f"[ERROR] Could not initialize marks file: {error}")


def display_records_and_average(filename="student_marks.txt"):
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return

    records = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or "," not in line:
                    continue
                parts = line.split(",")
                name = parts[0].strip()
                try:
                    marks = float(parts[1].strip())
                    records.append((name, marks))
                except ValueError:
                    continue
    except (OSError, UnicodeError) as error:
        print(f"[ERROR] Could not read file: {error}")
        return

    if not records:
        print(f"[INFO] No valid records found in '{filename}'.")
        return

    print("\nSTUDENT MARKS LEDGER")
    print(f"{'No.':<5} {'Student Name':<20} {'Marks Obtained':<15}")
    print("-" * 42)
    total_marks = 0.0
    for idx, (name, marks) in enumerate(records, 1):
        int_or_float = int(marks) if marks.is_integer() else marks
        print(f"{idx:<5} {name:<20} {int_or_float:<15}")
        total_marks += marks

    count = len(records)
    average = total_marks / count
    total_disp = int(total_marks) if total_marks.is_integer() else f"{total_marks:.2f}"
    print("-" * 42)
    print(f"Total Students : {count}")
    print(f"Total Marks    : {total_disp}")
    print(f"Class Average  : {average:.2f}")


def add_student_marks(filename="student_marks.txt"):
    name = input("Enter Student Name: ").strip()
    if not name:
        print("[ERROR] Student name cannot be empty.")
        return

    marks_str = input("Enter Marks (0-100): ").strip()
    try:
        marks = float(marks_str)
        if not (0 <= marks <= 100):
            print("[ERROR] Marks must be between 0 and 100.")
            return
    except ValueError:
        print("[ERROR] Please enter a valid numerical mark.")
        return

    stored_marks = int(marks) if marks.is_integer() else marks
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"{name},{stored_marks}\n")
    except OSError as error:
        print(f"[ERROR] Could not save student marks: {error}")
    else:
        print(f"[SUCCESS] Record for '{name}' ({stored_marks} marks) stored successfully.")


def main():
    filename = "student_marks.txt"
    ensure_sample_file(filename)
    print("STUDENT MARKS FILE HANDLING TOOL")
    while True:
        print("\nSelect an operation:")
        print("1. Display Records & Class Average")
        print("2. Add & Store Student Marks")
        print("3. Exit")
        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            display_records_and_average(filename)
        elif choice == "2":
            add_student_marks(filename)
        elif choice == "3":
            print("Thank you for using Student Marks Tool. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please choose from 1 to 3.")


if __name__ == "__main__":
    main()
