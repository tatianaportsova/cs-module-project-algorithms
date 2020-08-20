# python3 sliding_window_max/test_sliding_window_max.py -v

'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
  result = []
  max_num = 0
  for i in range(len(nums) - k + 1): 
      max_num = nums[i] 
      for j in range(1, k): 
          if nums[i + j] > max_num: 
              max_num = nums[i + j] 
      result.append(max_num) 

  return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
