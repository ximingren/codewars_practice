def binary_array_to_number(arr):
  result=0
  lengeth=len(arr)
  for t in range(lengeth):
      result+=arr[lengeth-t-1]*(2**t)
  return result

print(binary_array_to_number([1,1,1,1]))
