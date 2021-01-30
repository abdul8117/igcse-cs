using System;
namespace Q01a
{
    class Q01a
    {
        static void Main(string[] args)
        {
            int[] myNumbers = { 20, 30, 40, 50 };
            int total = 0;
			for (int i = 5; i < 15; i++)
            {
                total = total + i;
				if (i < 10)
                    Console.WriteLine(i * 10);
                else
                    Console.WriteLine(i);
            }
            Console.WriteLine(total);
            Console.ReadKey();
        }
    }
}