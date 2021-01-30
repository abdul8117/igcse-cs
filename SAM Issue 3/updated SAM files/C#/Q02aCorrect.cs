using System;
namespace Q02a
{
    class Q02a
    {
        static void Main(String[] args)
        {	
			// Print prompt and take country from user			
            Console.WriteLine("Enter the country you are visiting from: ");
            String country = Console.ReadLine();
            Console.WriteLine("You are from: " + country);
			
			// Tell the user their country			
            Console.WriteLine("Enter the number of adults in your party: ");
			
			// Take number of adults in party from user
            int adults = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter the number of children in your party: ");
			
			// Take number of children in party from user			
            int children = Convert.ToInt32(Console.ReadLine());
			
			// Calculate total number in party			
            int total = adults + children;
			
			// Tell the user the total number of people in their party			
            Console.WriteLine("The total in your party is: " + total);
			
			Console.ReadKey();
        }
    }
}
