# Sorting Algorithm Visualizer

A sorting algorithm visualizer using python and tkinter.

run ```main.py``` to start program.

- - -
You can add a custom sort by adding a python script in the  ```\algorithms``` folder and adding the script name in ```root.py```.



The script must be in the form as the following :

```python
NAME = 'Algorithm Name'
INFO = 'Time complexity\n  ' \
       'Ω(1)\n  Θ(1)\n  O(1)\n\n' \
       'Space complexity\n  ' \
       'O(1)'  # or some other infos of the algorithm

def sort(array):      # The main script of sort
    while True:
        array[0] = 0  # Some modifications to array
        yield         # The function should be a iterator that each step of the sort is an interation
                      # Seperate each step with 'yield'

def some_sub_func():  # Can define other subfunctions if needed
    pass
```

After adding the script file, you should add the script in ```root.py```, line 17.

```python
SORT_ALGORITHMS = [
    'bubble', 'insertion', 'selection', 'shell', 'merge', 'quick', 'radix'  # Add the script name here
]
```

- - -
> made by 19-006 권순호 / Data Structure assignment