import sys
from stats import analyse_book

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

analyse_book(filepath)

#print(f"DEBUG: filepath is {filepath} and type is {type(filepath)}")

#get_chars("/Users/RJayne/workspace/github.com/dharil81/bookbot/books/frankenstein.txt")    
#get_num_words("/Users/RJayne/workspace/github.com/dharil81/bookbot/books/frankenstein.txt")
#get_book_text("/Users/RJayne/workspace/github.com/dharil81/bookbot/books/frankenstein.txt")