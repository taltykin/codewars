def digitize(n):
    
    input_str = str(n)
    reverse = []


    if n == 0:

        reverse.append(int(input_str))

        return reverse
    else:

        i = 1
        while i <= len(input_str):
            reverse.append(int(input_str[len(input_str) - i]))
            i += 1
        
        return reverse
    
digitize(99551)