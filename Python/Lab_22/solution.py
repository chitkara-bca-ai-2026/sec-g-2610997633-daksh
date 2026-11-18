# Lab 22 - Keyword Search Utility
import os
import re


def ensure_sample_file(filename="report.txt"):
    if not os.path.exists(filename):
        sample_report = (
            "Annual Technology and AI Progress Report.\n"
            "The adoption of Artificial Intelligence accelerated across business units.\n"
            "AI algorithms improved diagnostic accuracy in healthcare operations.\n"
            "Data engineering pipelines were upgraded to support real-time data streaming.\n"
            "The company plans further investments in AI research and machine learning.\n"
        )
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(sample_report)
        except OSError as error:
            print(f"[ERROR] Could not initialize report file: {error}")


def search_keyword_in_file(filename="report.txt", keyword=""):
    keyword = keyword.strip()
    if not keyword:
        print("[ERROR] Keyword cannot be empty.")
        return
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except (OSError, UnicodeError) as error:
        print(f"[ERROR] Could not read file: {error}")
        return

    pattern = re.compile(rf"\b{re.escape(keyword)}\b", re.IGNORECASE)
    total_matches = 0
    matches_found = []

    for line_num, line in enumerate(lines, 1):
        clean_line = line.rstrip("\r\n")
        occurrences = len(pattern.findall(clean_line))
        if occurrences > 0:
            total_matches += occurrences
            match_word = "match" if occurrences == 1 else "matches"
            matches_found.append(f"Line {line_num} ({occurrences} {match_word}): {clean_line}")

    print(f"\n--- Search Results for '{keyword}' ---")
    if matches_found:
        for match_str in matches_found:
            print(match_str)
        print(f"\n[FOUND] Total occurrences of '{keyword}': {total_matches}")
    else:
        print(f"[INFO] No occurrences of '{keyword}' found in {filename}.")


def display_full_document(filename="report.txt"):
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except (OSError, UnicodeError) as error:
        print(f"[ERROR] Could not read file: {error}")
        return

    print(f"\n--- Full Report Document ({filename}) ---")
    for line_num, line in enumerate(lines, 1):
        print(f"{line_num} | {line.rstrip('\r\n')}")


def main():
    filename = "report.txt"
    ensure_sample_file(filename)
    print("KEYWORD SEARCH UTILITY")
    while True:
        print("\nSelect an operation:")
        print("1. Search Keyword in Document")
        print("2. View Full Document")
        print("3. Exit")
        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            kw = input("Enter keyword to search: ")
            search_keyword_in_file(filename, kw)
        elif choice == "2":
            display_full_document(filename)
        elif choice == "3":
            print("Thank you for using Keyword Search Utility. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please choose from 1 to 3.")


if __name__ == "__main__":
    main()
