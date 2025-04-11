def get_num_words(book_text):
        word_list = book_text.split()
        count = len(word_list)
        return count

def get_num_char(book_text):
	word_dic = {}
	for char in book_text:
		char = char.lower()
		if char in word_dic:
			word_dic[char] += 1
		else:
			word_dic[char]= 1
	return word_dic 

def get_list(num_char):
	char_list = []
	for char, count in num_char.items():
		char_list.append({"char": char, "count": count})

	def sort_on(dict):
		return dict["count"]

	char_list.sort(reverse=True, key=sort_on)
	return char_list
