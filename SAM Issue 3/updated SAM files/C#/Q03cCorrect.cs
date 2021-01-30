using System;

namespace Q03c_cs
{
   // Do not use any other data structure such as an array or a list.
    class Program
    {
        static void Main(string[] args)
        {
            int count = 0;      // a counter for the line numbers
            String theLine;     // holds each line of the file

            // open Cities.txt as input
            System.IO.StreamReader fileReader = new System.IO.StreamReader("Cities.txt"); 
            // open Numbered.txt as output
            System.IO.StreamWriter fileWriter = new System.IO.StreamWriter("Numbered.txt"); 
            // use loop to read each line of the input file into a variable named theLine
            while (fileReader.Peek() >= 0)
            {
                theLine = fileReader.ReadLine();
                // increment the line count variable
                count = count + 1;
                // add the line number to the front of the line followed by a space
                theLine = Convert.ToString(count) + " " + theLine;
                // print the line to the display
                Console.WriteLine(theLine);
                // write new line to the output file
                fileWriter.WriteLine(theLine);
            }
            // close the input file
            fileReader.Close();
            // close the output file
            fileWriter.Close();
            Console.ReadKey();
        }
    }
}
