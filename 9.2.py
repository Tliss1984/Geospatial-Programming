def has_no_e(word):
	if "e" not in word:
		return True
	else:
		return False

def aretherees(f):
    no_e = 0
    all_words = 0
    file = open(f)
    for line in file:
        all_words += 1
        word = line.strip()
        if has_no_e(word):
             print (word)
             no_e += 1
    print (no_e / all_words*100)


aretherees('words.txt')
