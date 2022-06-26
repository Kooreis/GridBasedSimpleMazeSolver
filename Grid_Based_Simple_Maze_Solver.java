```java
import java.util.LinkedList;

public class MazeSolver {

    static int[][] maze = {
            {1, 1, 1, 1, 1, 0, 0, 1, 1, 1},
            {1, 0, 0, 1, 1, 1, 0, 1, 0, 1},
            {1, 1, 1, 0, 0, 1, 1, 1, 0, 1},
            {0, 0, 1, 1, 1, 0, 0, 1, 1, 1},
            {1, 1, 1, 0, 0, 1, 1, 0, 0, 1},
            {1, 0, 1, 1, 1, 1, 0, 1, 0, 0},
            {1, 0, 0, 0, 0, 1, 0, 1, 1, 1},
            {1, 1, 1, 1, 1, 1, 1, 1, 0, 0},
            {1, 0, 0, 0, 0, 0, 0, 0, 0, 1},
            {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
    };

    static LinkedList<Integer> path = new LinkedList<Integer>();
    static boolean[][] wasHere = new boolean[10][10];

    public static void main(String[] args) {
        if (solveMaze(0, 0)) {
            System.out.println("Path found");
            System.out.println(path);
        } else {
            System.out.println("No path found.");
        }
    }

    public static boolean solveMaze(int x, int y) {
        if (x == 9 && y == 9) return true;
        if (maze[y][x] == 0 || wasHere[y][x]) return false;
        wasHere[y][x] = true;
        if (y != 0)
            if (solveMaze(x, y - 1)) {
                path.push(x);
                path.push(y);
                return true;
            }
        if (y != 9)
            if (solveMaze(x, y + 1)) {
                path.push(x);
                path.push(y);
                return true;
            }
        if (x != 0)
            if (solveMaze(x - 1, y)) {
                path.push(x);
                path.push(y);
                return true;
            }
        if (x != 9)
            if (solveMaze(x + 1, y)) {
                path.push(x);
                path.push(y);
                return true;
            }
        return false;
    }
}
```