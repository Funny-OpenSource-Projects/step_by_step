<div align=center>

# Step by Step



![](docs/screenrecording.png)

</div>

## Installation

```bash
pip install stepbystep
```

## Usage

To inspect your snippet step by step you should surround your snippet with `@stepbystep_wrapper` decorator, thats all now you can run your script and enjoy the magic!

> You should specify the time intervals beetwen steps in seconds using the time_between_steps argument 

```python

```python
from stepbystep import stepbystep_wrapper

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
```