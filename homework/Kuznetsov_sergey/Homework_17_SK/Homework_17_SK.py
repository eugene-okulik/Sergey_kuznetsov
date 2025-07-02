import os
import argparse
import sys


def find_text_in_logs(folder_path, search_text):
    results = []

    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line_num, line in enumerate(file, 1):
                        if search_text in line:
                            words = line.split()
                            try:
                                index = words.index(search_text)
                                start = max(0, index - 5)
                                end = index + 6
                                context = ' '.join(words[start:end])
                                results.append((file_name, line_num, context))
                            except ValueError:
                                results.append((file_name, line_num, line.strip()))
            except (UnicodeDecodeError, PermissionError):
                continue

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="folder")
    parser.add_argument("--text", help="Text")
    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"Error: {args.folder} is not a valid directory", file=sys.stderr)
        sys.exit(1)

    if not args.text:
        print("Error: --text argument is required", file=sys.stderr)
        sys.exit(1)

    results = find_text_in_logs(args.folder, args.text)

    if not results:
        print(f"No occurrences of '{args.text}' found.")
        return

    print(f"Found {len(results)} occurrence(s) of '{args.text}':\n")
    for file_name, line_num, context in results:
        print(f"File: {file_name}, Line: {line_num}")
        print(f"Context: {context}\n")


if __name__ == '__main__':
    main()
