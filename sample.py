from stepbystep import stepbystep_wrapper

def sum(n1, n2):
  print("n1:", n1)
  print("n2:", n2)
  print("sumando:", n1 + n2)
  suma = n1 + n2
  return suma

@stepbystep_wrapper(time_between_steps=0.5)
def bubbleSort(array, *args):
  size = len(array)
  for i in range(size):
    swapped = False
    for j in range(size - i - 1):
      array, j, j+1, -1, -1
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
        swapped = True
    if not swapped:
      break
  return array



print("la suma es:", sum(1, 2))
      
print(bubbleSort([4, 5, 3, 4, 5, 2, 3]))
print(sum(1, 2))
print("hello")