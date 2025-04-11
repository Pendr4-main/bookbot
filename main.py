import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

from stats import get_num_words
from stats import get_num_char
from stats import get_list
def main():
	filepath = book_path
	book = get_book_text(filepath)
	num_words = get_num_words(book)
	num_char = get_num_char(book)
	char_list = get_list(num_char)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")
	print("----------- Word Count -----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count ---------")

	for item in char_list:
		char = item["char"]
		count = item["count"]
		if char.isalpha():
			print(f"{char}: {count}")

	print("============= END =============")

main()

