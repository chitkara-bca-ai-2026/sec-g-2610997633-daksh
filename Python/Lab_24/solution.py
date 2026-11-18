# Lab 24 - Student Result Analysis System
import os
import csv


def ensure_sample_csv(filename="students_data.csv"):
    if not os.path.exists(filename):
        sample_rows = [
            ["RollNo", "Name", "Subject", "Marks"],
            ["101", "Aman", "Python", "85"],
            ["102", "Riya", "Python", "92"],
            ["103", "Karan", "Python", "45"],
            ["104", "Neha", "Python", "78"],
            ["105", "Rohit", "Python", "38"],
            ["106", "Pooja", "Python", "62"],
        ]
        try:
            with open(filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(sample_rows)
        except OSError as error:
            print(f"[ERROR] Could not initialize CSV file: {error}")


def read_all_students(filename="students_data.csv"):
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
    except (OSError, csv.Error) as error:
        print(f"[ERROR] Could not parse CSV file: {error}")
        return

    print("\nALL ENROLLED STUDENTS")
    print(f"{'Roll No':<10} {'Name':<15} {'Subject':<12} {'Marks':<8}")
    print("-" * 47)
    for row in rows:
        print(f"{row.get('RollNo', ''):<10} {row.get('Name', ''):<15} {row.get('Subject', ''):<12} {row.get('Marks', ''):<8}")
    print("-" * 47)
    print(f"Total Records: {len(rows)}")


def filter_students_above_threshold(filename="students_data.csv", threshold=50):
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
    except (OSError, csv.Error) as error:
        print(f"[ERROR] Could not parse CSV file: {error}")
        return

    qualified = []
    for row in rows:
        try:
            marks = float(row.get("Marks", 0))
            if marks > threshold:
                qualified.append(row)
        except ValueError:
            continue

    print(f"\nSTUDENTS WITH MARKS > {threshold}")
    print(f"{'Roll No':<10} {'Name':<15} {'Subject':<12} {'Marks':<8}")
    print("-" * 47)
    for row in qualified:
        print(f"{row.get('RollNo', ''):<10} {row.get('Name', ''):<15} {row.get('Subject', ''):<12} {row.get('Marks', ''):<8}")
    print("-" * 47)
    print(f"Qualified Students Count: {len(qualified)}")


def main():
    filename = "students_data.csv"
    ensure_sample_csv(filename)
    print("STUDENT RESULT ANALYSIS SYSTEM")
    while True:
        print("\nSelect an operation:")
        print("1. Display All Students from CSV")
        print("2. Filter Students (Marks > 50)")
        print("3. Exit")
        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            read_all_students(filename)
        elif choice == "2":
            filter_students_above_threshold(filename, threshold=50)
        elif choice == "3":
            print("Thank you for using Student Result Analysis System. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please choose from 1 to 3.")


if __name__ == "__main__":
    main()
