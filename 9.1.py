def read(words):
    file = open(words)
    for line in file:
        word = line.strip()
        if len(word) > 20:
            print (word)
			
read('words.txt')

