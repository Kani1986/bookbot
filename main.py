from stats import (
    count_words,
    count_letters, 
    sort_to_list,
)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    letters = count_letters(book_text)
    sorted_list = sort_to_list(letters)
    print(sorted_list)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def print_report():
    pass

main()