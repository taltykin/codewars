def digitize(n):
    
    reverse = []

    i = 1
    while i <= len(n):
        reverse.append(n[len(n) - i])
        i += 1
    
    return reverse
    
digitize([7,5,3,2,8,5,3,2])