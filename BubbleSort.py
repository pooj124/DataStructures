def bubble(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements [i] > elements[i+1]:
                elements[i], elements[i+1] = elements[i+1], elements[i]
    return elements
    
    
print(bubble([2,3,5,1]))
