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