def summation(f, lower, upper):
    sum_to_return, i  = 0, lower
    while (i <= upper):
        sum_to_return, i = f(i), i+1
    return sum_to_return

