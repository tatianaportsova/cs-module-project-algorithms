# python3 eating_cookies/test_eating_cookies.py -v

'''
Input: an integer
Returns: an integer
'''
import math

def eating_cookies(n):
  if (n == 1 or n == 0): 
    return 1
  elif (n == 2): 
    return 2
      
  else: 
    return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1) 

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

# def eating_cookies(n):
#     # print(n)
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     else:
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

def eating_cookies(n, cache=None):
    # base cases
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check if the work has already been done
    # by looking in the cache
    elif cache is not None and cache[n] > 0:
        # return the previously computed answer and don't recurse
        return cache[n]
    else:
        # might need to create our cache for the first time
        if cache is None:
            # initialize an empty list for a cache
            cache = [0 for i in range(n+1)]
        # store the value of the recursive call expressions in our cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    
    return cache[n]

eating_cookies(50)

'''
In order to show the redundant work going on,
add a print(n) statement at the beginning of 
eating cookies and run with a decent sized
input.
'''

'''
After discussing how to use a cache in theory
in LucidChart, now, make that a reality in
the code here.
'''