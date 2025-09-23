def main(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_book_text(filepath):
    print(main(filepath))

def get_num_words(filepath):
    num_words = len(main(filepath).split())
    print(f"Found {num_words} total words")   