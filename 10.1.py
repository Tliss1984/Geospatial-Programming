def nested_sum(t):


   
    summed = 0
    for value in t:
        summed += sum(value)
    return summed



t = [[1, 2], [3], [4, 5, 6],[7,8,9]]

print (nested_sum(t))
