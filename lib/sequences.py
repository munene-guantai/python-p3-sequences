#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
        
    fibonacci_list = [0, 1]

    while len(fibonacci_list) < length:
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)

    print(fibonacci_list)


    pass