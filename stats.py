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

def sort_to_list(letters):
    sorted_list = []
    for char, count in letters.items():
        temp_dictionary = {"char": char, "num": count}
        sorted_list.append(temp_dictionary)
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dictionary):
    return dictionary["num"]