using System;
namespace Q05b_cs
{
    class Program
    {
        static void Main(string[] args)
        {
			// Write your code here	
            int totalSpend = 0;
            Console.WriteLine("What is your total spend?");
            totalSpend = Convert.ToInt32(Console.ReadLine());
            if (totalSpend > 300)
                Console.WriteLine("Discount is 10%");
            else if (totalSpend > 0)
                Console.WriteLine("No discount");
            else
                Console.WriteLine("Invalid input");
        }
    }
}
