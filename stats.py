def main(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_book_text(filepath):
    print(main(filepath))

def get_num_words(filepath):
    num_words = len(main(filepath).split())
    print(f"Found {num_words} total words")   

def get_chars(filepath):
    lower = main(filepath).lower()
    chars = {}
    for char in lower:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_chars(filepath):
    output = get_chars(filepath)
    char_counts = [{"char": char, "num": count} for char, count in output.items()]
    char_counts.sort(reverse=True, key=sort_on)
    return char_counts

def analyse_book(filepath):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words(filepath)
    sorted = sort_chars(filepath)
    for item in sorted:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")