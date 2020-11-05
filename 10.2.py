def cumsum(t):
   
    total = 0
    assign = []
    for x in t:
        total += x
        assign.append(total)
    return assign


t = [3,1,4,6,4,3]
print (cumsum(t))
