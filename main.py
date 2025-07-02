import sys
from stats import (
    count_words,
    count_letters, 
    sort_to_list,
    get_book_text,
    print_report,
)

def main():
    if  len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    letters = count_letters(book_text)
    sorted_list = sort_to_list(letters)
    print_report(file_path, num_words, sorted_list)

main()