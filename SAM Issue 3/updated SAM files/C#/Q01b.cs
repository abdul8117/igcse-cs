using System;
namespace Q01a
{
    class Q01b
    {
        static void Main(string[] args)
        {
            int x = 44;
            int t = 0;
            for (int i = 0; i < 60;i++)
            {
                t = t + i - x + 12;
                if (i >= 10)
                    Console.WriteLine(i * 10 / 14);
                else
                    Console.WriteLine(i);
            }
            Console.WriteLine(t);
            Console.ReadKey();
        }
    }
}