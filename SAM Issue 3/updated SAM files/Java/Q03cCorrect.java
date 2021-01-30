import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.Scanner;

public class Q03c 
{
    // Do not use any other data structure such as an array or a list.
    public static void main(String[] args) throws FileNotFoundException, UnsupportedEncodingException 
    {
        int count = 0;          // A counter for the line numbers
        String theLine;         // Holds each line of the file
        Scanner theFile;
        PrintWriter outFile;

        // Open "Cities.txt" as input
        theFile = new Scanner(new BufferedReader(new FileReader("cities.txt")));
        // Open "Numbered.txt" as output
        outFile = new PrintWriter("Numbered.txt", "UTF-8");
        // Use loop to read each line of
        // the input file into a variable named 'theLine'   
        while (theFile.hasNextLine()) 
        {
            theLine = theFile.nextLine();
            // Increment the line count variable
            count++;
            // Add the line number to the front of the line
            // followed by a space
            theLine = (Integer.toString(count) + " " + theLine);
            // print the line to the display
            System.out.println(theLine);
            // Write the new line to the output file
            outFile.println(theLine);
        }

        // Close the input file
        theFile.close();
        // Close the output file
        outFile.close();
    }
}
