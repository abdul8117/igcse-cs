using System;
namespace Q03b_cs
{
    class Program
    {
        String theDate = "";

        private static double toCelsius(double inTemp)
        {
            double celsius = 0;
            celsius = (5.0 / 9.0) * (inTemp - 32.0);
            
        }

        private static double toFahrenheit(double inTemp)
        {
            double fahrenheit = ((9.0 / 5.0) * inTemp) + 32.0;
            return fahrenheit;
        }

        private static void waitTenSeconds()
        {
            System.Threading.Thread.Sleep(10000);
        }

        private static void waitTime(int inMilliseconds)
        {
            System.Threading.Thread.Sleep(inMilliseconds);
        }

        static void Main(String[] args)
        {
            Console.WriteLine(toFahrenheit(0));
            Console.WriteLine(toCelsius(212.0));	 // This line is not working as expected
            Console.WriteLine("Sleeping for 10");
            waitTenSeconds();
            Console.WriteLine(toCelsius(32.0));
            Console.WriteLine("Sleeping for 5");
            waitTime(5000);
            Console.WriteLine(toFahrenheit(100.0));
			
            Console.ReadKey();
        }
    }
}

