def count_positives_sum_negatives(arr):
    b = []
    c = 0
    if not arr:
        return arr
    else:
        for item in arr:
            if (item >0 ):
                b.append(item)
            else:
                c += item
        
        ret = [len(b), c]

        return ret



count_positives_sum_negatives([])