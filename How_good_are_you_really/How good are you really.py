def better_than_average(class_points, your_points):
    # Your code here

    summ = 0
    avrg = 0

    for i in class_points:
        summ += i
    
    avrg = summ / len(class_points)

    if(avrg < your_points):
        return True
    else:
        return False
        
better_than_average([2, 3], 5)