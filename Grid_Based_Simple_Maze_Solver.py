Sure, here is a simple Python script for a grid-based maze solver:

```python
from queue import Queue

def is_valid(maze, moves):
    i = 0
    j = 0
    for move in moves:
        if move == 'L':
            i -= 1
        elif move == 'R':
            i += 1
        elif move == 'U':
            j -= 1
        elif move == 'D':
            j += 1
        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == 0):
            return False
    return True

def find_end(maze, moves):
    i = 0
    j = 0
    for move in moves:
        if move == 'L':
            i -= 1
        elif move == 'R':
            i += 1
        elif move == 'U':
            j -= 1
        elif move == 'D':
            j += 1
    if maze[j][i] == 2:
        print("Found: " + moves)
        return True
    return False

maze = [[1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 2]]

nums = Queue()
nums.put('')
add = ''
while not find_end(maze, add): 
    add = nums.get()
    for j in ['L', 'R', 'U', 'D']:
        put = add + j
        if is_valid(maze, put):
            nums.put(put)
```