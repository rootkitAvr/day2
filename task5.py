def arithmetic_mean(list):
    count = 0
    sum = 0

    for i in list:
        count += 1

    for i in list:
        sum += i
    number = sum/count
    return number
