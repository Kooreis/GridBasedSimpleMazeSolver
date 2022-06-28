```python
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
```