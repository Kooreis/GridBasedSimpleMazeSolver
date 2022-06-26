```CSharp
using System;
using System.Collections.Generic;

public class Program
{
    static char[,] maze = {
        { 'S', '#', '#', '#', '#', '#'},
        { '#', ' ', ' ', ' ', '#', ' '},
        { '#', ' ', '#', ' ', ' ', ' '},
        { '#', ' ', '#', '#', '#', ' '},
        { '#', ' ', ' ', ' ', '#', ' '},
        { '#', '#', '#', '#', '#', 'E'}
    };

    static List<Tuple<int, int>> path = new List<Tuple<int, int>>();

    public static void Main()
    {
        if (FindPath(0, 0))
        {
            foreach (var point in path)
            {
                Console.WriteLine($"({point.Item1}, {point.Item2})");
            }
        }
        else
        {
            Console.WriteLine("No path found!");
        }
    }

    static bool FindPath(int x, int y)
    {
        if (x < 0 || y < 0 || x >= maze.GetLength(0) || y >= maze.GetLength(1))
        {
            return false;
        }

        if (maze[x, y] == 'E')
        {
            path.Add(new Tuple<int, int>(x, y));
            return true;
        }

        if (maze[x, y] != ' ' && maze[x, y] != 'S')
        {
            return false;
        }

        maze[x, y] = '.';

        if (FindPath(x - 1, y) || FindPath(x + 1, y) || FindPath(x, y - 1) || FindPath(x, y + 1))
        {
            path.Add(new Tuple<int, int>(x, y));
            return true;
        }

        return false;
    }
}
```