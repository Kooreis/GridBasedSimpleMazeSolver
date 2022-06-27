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
```