import sys
from stats import get_word_count
from stats import get_char_counts
from stats import sort_dictionary

def get_book_text(file_path):
    file_contents = None
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
def print_report(num_words, char_counts):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k, v in char_counts.items():
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    document = get_book_text(path_to_book)
    num_words = get_word_count(document)
    num_chars = get_char_counts(document)
    sorted_num_chars = sort_dictionary(num_chars)
    print_report(num_words, sorted_num_chars)

main()

