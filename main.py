def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    print(f"--- Begin Report of {book_path} ---")
    print(f"{count} words found in the document")
    print()
    char_count(text)
    print("--- End Report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lowered_text = text.lower()
    chars = list(lowered_text)
    dict_letter_count = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0,
        'i':0,
        'j':0,
        'k':0,
        'l':0,
        'm':0,
        'n':0,
        'o':0,
        'p':0,
        'q':0,
        'r':0,
        's':0,
        't':0,
        'u':0,
        'v':0,
        'w':0,
        'x':0,
        'y':0,
        'z':0
    }
    for i in range(0,len(chars)):
        if chars[i] in dict_letter_count:
            dict_letter_count[chars[i]] += 1
    sort_on(dict_letter_count)
    
def sort_on(dict):
    sorted_letter_counts = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_letter_counts:
        print(f"The '{char}' character was found {count} times")
main()