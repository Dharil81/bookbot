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
    get_num_words(filepath)
    lower = main(filepath).lower()
    chars = {}
    for char in lower:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    print (dict(chars))