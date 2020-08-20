# python3 moving_zeroes/test_moving_zeroes.py -v

'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
  for i in range(len(arr)):
    current = arr[i]
    j = i
    while j != 0 and current != 0:   # arr[j-1]
      arr[j] = arr [j-1]
      j -= 1
    arr[j] = current    
  return arr

'''
what if we had a pointer that started at the beginning
and a pointer that started at the end
and they moved towards each other in the middle?

if the left pointer "sees" a zero and the right pointer "sees" a non-zero
swap

if the left sees a non-zero increment
if the right sees a zero increment
'''

# def moving_zeroes(arr):
#   # initialize a left and right pointer
#   l = arr[0]
#   r = arr[-1]
#   # left is 0
#   if l == 0:
    
#   # right is last index in arr

#   while l <= r:
#     #   if l points at a zero and right points at non-zero
#           swap left and right items in original arr
#           increment left
#           decrement right
#       else
#           if left is non-zero:
#               increment left
#           if right is zero:
#               decrement right

#     return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    
'''
What can I do to avoid having nested loops or needing to slice the arrays?
What about the names of my variable names? Could those also be improved?
'''