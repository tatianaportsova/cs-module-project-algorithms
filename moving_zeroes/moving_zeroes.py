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


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")