def square_sum(numbers):
    #your code here
    list_of_squers = []
    out = 0
    for item in numbers:
        list_of_squers.append(item * item)
    
    for item in list_of_squers:
        out += item
        
    return(out)   # important type RETURN not print.

square_sum([1, 2, 2])