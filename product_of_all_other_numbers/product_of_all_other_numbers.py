# python3 product_of_all_other_numbers/test_product_of_all_other_numbers.py -v

'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
  left_p = [0]*len(arr) # initialize left array 
  right_p = [0]*len(arr) # initialize right array
  
  left_p[0] = 1 # the left most is 1
  right_p[-1] = 1 # the right most is 1
  result = [] # output
  
  for i in range(1, len(arr)):
      left_p[i] = left_p[i-1]*arr[i-1]
      right_p[len(arr) - i - 1] = right_p[len(arr) - i]*arr[len(arr) - i]
      
  for i in range(len(arr)):
      result.append(left_p[i]*right_p[i])

  return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")


# def product_of_previous_two_numbers(arr):
#   result = []
#   a = 1
#   for i in arr:
#     a = i * a
#     result.append(a)
#   return result

# arr = [1, 2, 3, 4, 5]
# result = [1, 2, 6, 24, 120]