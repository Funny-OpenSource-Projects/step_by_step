# Step by Step

## Installation

```bash
pip install stepbystep
```

## Usage

To inspect your snippet step by step you should surround your snippet with `@stepbystep_wrapper` decorator, thats all now you can run your script and enjoy the magic!


```python
from stepbystep import stepbystep_wrapper

@stepbystep_wrapper
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
```