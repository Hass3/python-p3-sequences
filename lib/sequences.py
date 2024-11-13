#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []
    if length <= 0:
        print([])
        return
    elif length == 1:
      fibonacci = [0]
    else:
       fibonacci=[0,1]
       for i in range(2,length):
          next_number = fibonacci[-1] + fibonacci[-2]
          fibonacci.append(next_number)
    print(fibonacci)

    


