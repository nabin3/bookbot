# getting text
def get_text(path):
    with open(path) as f:
        return f.read()
    
# count words
def count_words(file_contents):
    word_List = file_contents.split()
    return len(word_List)

#count each charachter
def letters_frequency(file_contents):
    char_dict = {}
    sentence = file_contents.lower()
    for c in sentence:
        if c.isalpha():
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
    return char_dict

# sorting key
def sort_condition(a):
    return a["char_num"]

# creating and sorting list
def sorted(input):
    sorted_List = []
    for ch in input:
        sorted_List.append({"char" : ch , "char_num" : input[ch]})
    sorted_List.sort(reverse = True, key = sort_condition)
    return sorted_List

def main():
    file_source = "books/frankenstein.txt"
    file_contents = get_text(file_source)
    print(f"---- begin report of {file_source} ----")
    words_number = count_words(file_contents)
    print(f"this book has {words_number} words")
    print()
    rec = letters_frequency(file_contents)
    char_List = sorted(rec)
    for item in char_List:
        print(f"'{item['char']}' was found {item['char_num']} times")

main()


