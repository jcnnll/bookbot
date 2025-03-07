
def get_word_count(document):
    words = document.split()
    return len(words)

def get_char_counts(document):
    char_counts = {}
    for word in document.lower().split():
        for char in list(word):
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sort_dictionary(dictionary):
    sorted_list = sorted(dictionary.items())
    sorted_dict = {}
    for k, v in sorted_list:
        if k.isalpha():
            sorted_dict[k] = v
    return sorted_dict
