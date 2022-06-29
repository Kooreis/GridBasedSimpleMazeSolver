# Python Documentation

# Python Maze Solver

This Python script is a simple grid-based maze solver. It uses a breadth-first search algorithm to find the shortest path from the start to the end of a maze.

## Libraries Used

- `queue`: This is a built-in Python module used for creating queue data structures. In this script, it is used to store and manage the different paths that the algorithm explores in the maze.

## How It Works

The script represents the maze as a 2D list, where `1` represents a valid path, `0` represents a wall, and `2` represents the end of the maze. The script starts at the top left corner of the maze and tries to find a path to the end by moving left, right, up, or down.

The `is_valid` function checks if a given sequence of moves is valid. It iterates through each move in the sequence, updating the current position accordingly. If a move leads to a wall or outside the maze, the function returns `False`. Otherwise, it returns `True`.

The `find_end` function checks if a given sequence of moves leads to the end of the maze. Like the `is_valid` function, it iterates through each move in the sequence, updating the current position accordingly. If the final position is the end of the maze, the function prints the sequence of moves and returns `True`. Otherwise, it returns `False`.

The main part of the script uses a queue to systematically explore all possible paths through the maze. It starts by adding an empty sequence of moves to the queue. Then, it enters a loop where it repeatedly dequeues a sequence of moves, checks if it leads to the end of the maze, and if not, enqueues all valid sequences of moves that can be made by extending the current sequence with one additional move in each possible direction. The loop continues until a sequence of moves that leads to the end of the maze is found.

## Usage

To use this script, simply replace the `maze` variable with your own 2D list representing a maze. Then, run the script, and if a path to the end of the maze exists, it will be printed to the console.

---

# C# Documentation

# Maze Solver in C#

This repository contains a C# script that solves a given maze. The maze is represented as a 2D array, where 'S' represents the start point, 'E' represents the end point, '#' represents walls, and ' ' (space) represents open paths. The script uses a recursive algorithm to find a path from the start point to the end point.

## Script Explanation

The script defines a static 2D char array `maze` that represents the maze to be solved. It also defines a static list of tuples `path` that will store the path from the start to the end of the maze.

The `Main` method is the entry point of the script. It calls the `FindPath` method with the start coordinates (0, 0). If a path is found, it prints the coordinates of the path. If no path is found, it prints "No path found!".

The `FindPath` method is a recursive method that tries to find a path from a given point in the maze to the end point. It first checks if the given coordinates are valid and within the maze. If the current point is the end point, it adds the point to the path and returns true. If the current point is a wall or has been visited before, it returns false. It then marks the current point as visited by setting its value to '.'. It then recursively calls `FindPath` for the neighboring points (up, down, left, right). If any of these calls return true, it adds the current point to the path and returns true. If none of the calls return true, it means that there is no path from the current point to the end point, so it returns false.

## Imported Libraries

- `System`: This namespace contains fundamental classes and base classes that define commonly-used value and reference data types, events and event handlers, interfaces, attributes, and processing exceptions. In this script, it is used for the `Console` class to print output to the console.

- `System.Collections.Generic`: This namespace contains interfaces and classes that define generic collections, which allow users to create strongly typed collections that provide better type safety and performance than non-generic strongly typed collections. In this script, it is used for the `List` class to store the path and the `Tuple` class to store the coordinates of each point in the path.

---

# Java Documentation

# Maze Solver

This Java script is a simple maze solver. It uses a recursive depth-first search algorithm to find a path from the top left corner to the bottom right corner of a 2D maze. The maze is represented as a 2D array, where 1s represent walls and 0s represent open paths. The script will print out the path it found, or a message stating that no path was found.

## Code Explanation

The script contains a 2D array `maze` that represents the maze to be solved, a `LinkedList` `path` that stores the path found, and a 2D boolean array `wasHere` that keeps track of the cells that have been visited.

The `main` method calls the `solveMaze` method with the starting coordinates (0, 0). If a path is found, it prints out "Path found" and the path. If no path is found, it prints out "No path found."

The `solveMaze` method is a recursive method that tries to find a path from the current cell to the goal. It first checks if the current cell is the goal. If it is, it returns true. If the current cell is a wall or has been visited before, it returns false. It then marks the current cell as visited.

Next, it recursively calls `solveMaze` on the neighboring cells. If a call returns true, it means a path to the goal has been found, so it adds the current cell to the path and returns true. If all calls return false, it means there is no path to the goal from the current cell, so it returns false.

## Imported Libraries

- `java.util.LinkedList`: This library provides the LinkedList class which is used to store the path found. LinkedList is a linear data structure where the elements are not stored in contiguous locations and every element is a separate object with a data part and address part. The elements are linked using pointers and addresses. Each element is known as a node. Due to the dynamicity and ease of insertions and deletions, they are preferred over the arrays.

---
