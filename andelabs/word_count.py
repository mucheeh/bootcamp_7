def words(word):
	for c in word:
		if c.isspace():
			string_list = word.split()

	string_dict = {}

	for word in string_list:
		if word in string_dict:
			string_dict[word] = string_dict[word] + 1
		else:
			string_dict[word] = 1
	return string_dict

string = "olly olly in come free"
string1 = "one fish two fish red fish blue fish"
print words(string)
print words(string1)
print words('go Go GO')
print words('testing 1 2 testing')

