def insert_squares(arr, num):
    # add square of numbers from 1 to num to the list named arr and return list
    for i in range(1, num):
        arr.append(i * i)
    return arr
