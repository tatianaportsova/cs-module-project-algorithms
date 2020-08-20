def bubble_sort(arr):
  for i in range(0, len(arr)-1):
    for j in range(0, len(arr)-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

A = [2, 16, 91, 5, 18, 0, 1]
print("Bubble")
print(bubble_sort(A))

for i in range(0, len(A)-1):
  print(i)

def selection_sort(arr):
  for i in range (0, len(arr)-1):
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j
    if min_index != i:
      arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr

B = [2, 16, 91, 5, 18, 0, 1, 17]
print("Selection")
print(selection_sort(B))