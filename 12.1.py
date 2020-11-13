def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
            
    return d

def most_frequent(s):
    a=histogram(s)
 
    new_dict = {}
    for c, d in a.items():
        new_dict[d] = c
    
    
    
    for c in sorted(new_dict,reverse=True):
        
        
        reverse=( new_dict[c])

        print (reverse)

s='aaaxxxabbxxxxbdxxxx'
most_frequent(s)
