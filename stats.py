def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_letters(book_text):
    lowercase = book_text.lower()
    letters = {}
    for l in lowercase:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

def sort_on(dictionary):
    return dictionary["num"]

def sort_to_list(letters):
    sorted_list = []
    for char, in letters:
        sorted_list.append({"char": char, "num": letters[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def print_report(file_path, num_words, sort_to_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort_to_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

