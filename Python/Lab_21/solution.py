# Lab 21 - Document Statistics Tool
import os


def ensure_sample_file(filename="document.txt"):
    if not os.path.exists(filename):
        sample_text = (
            "Python is a versatile and powerful programming language.\n"
            "It supports multiple programming paradigms including procedural and object oriented.\n"
            "File handling in Python is simple and efficient.\n"
            "Students practice file reading, writing, and text processing operations.\n"
        )
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(sample_text)
        except OSError as error:
            print(f"[ERROR] Could not initialize document file: {error}")


def calculate_document_stats(filename="document.txt"):
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return None
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except (OSError, UnicodeError) as error:
        print(f"[ERROR] Could not read file: {error}")
        return None

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line.rstrip("\r\n")) for line in lines)
    return {"lines": line_count, "words": word_count, "characters": char_count}


def display_document_content(filename="document.txt"):
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except (OSError, UnicodeError) as error:
        print(f"[ERROR] Could not read file: {error}")
        return

    print(f"\n--- Document Content ({filename}) ---")
    for index, line in enumerate(lines, 1):
        print(f"{index} | {line.rstrip('\r\n')}")


def main():
    filename = "document.txt"
    ensure_sample_file(filename)
    print("DOCUMENT STATISTICS TOOL")
    while True:
        print("\nSelect an operation:")
        print("1. Calculate Document Statistics")
        print("2. Display Document Content")
        print("3. Exit")
        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            stats = calculate_document_stats(filename)
            if stats:
                print(f"\nDOCUMENT SUMMARY ({filename})")
                print(f"Total Lines      : {stats['lines']}")
                print(f"Total Words      : {stats['words']}")
                print(f"Total Characters : {stats['characters']}")
        elif choice == "2":
            display_document_content(filename)
        elif choice == "3":
            print("Thank you for using Document Statistics Tool. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please choose from 1 to 3.")


if __name__ == "__main__":
    main()
