def words_dict(s):

    text = open("words.txt")
    final=dict()
    for line in text:
       final[line.strip()]=1
    if s in final:
        print (True)
    else:
        print(False)
    print(final)



words_dict("aahs")
