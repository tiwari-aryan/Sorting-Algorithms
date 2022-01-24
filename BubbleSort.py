def is_sorted(list_sort):
  for i in range(0, len(list_sort) - 1):
    if list_sort[i] > list_sort[i+1]:
      return False
  return True
def bubble_sort(list_sort):
  for i in range(0, len(list_sort) - 1):
    if list_sort[i] > list_sort[i+1]:
      temp = list_sort[i]
      list_sort[i] = list_sort[i+1]
      list_sort[i+1] = temp
  if is_sorted(list_sort):
    return list_sort
  else:
    bubble_sort(list_sort)