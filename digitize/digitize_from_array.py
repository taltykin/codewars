def digitize(n):
    
    input_str = str(n)
    reverse = []


    if n == 0:

        reverse.append(int(input_str))                            # int() convert string into integer

        return reverse
    else:

        i = 1
        while i <= len(input_str):
            reverse.append(int(input_str[len(input_str) - i]))    # int() convert string into integer
            i += 1
        
        return reverse
    
digitize(99551)