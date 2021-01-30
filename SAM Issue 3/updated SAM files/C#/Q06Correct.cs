using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication2
{
    class Q06
    {
        static void Main(String[] args)
        {
            String[,] theArtists = {{"Andy", "Warhol", "1928"},
                               {"Pablo", "Picasso", "1881"},
                               {"Salvador", "Dali", "1904"},
                               {"Lavinia", "Fontana", "1552"},
                               {"Jackson", "Pollock", "1912"},
                               {"Henri", "Matisse", "1869"},
                               {"Frida", "Kahlo", "1907"},
                               {"Georgia", "O'Keeffe", "1887"},
                               {"Kara", "Walker", "1969"},
                               {"Yayoi", "Kusama", "1929"}};

            String[] theLabels = new String[10];  // Put the new user labels into this structure
                                                  // Make the artist labels
            for (int i = 0; i < theLabels.Length; i++)
            {
                String newRecord = Convert.ToString(theArtists[i,1][0]) +
                        Convert.ToString(theArtists[i,0][0]) +
                        theArtists[i,2];
                theLabels[i] = newRecord;
                Console.WriteLine(newRecord);
                Console.WriteLine("The new userIDs are: " + theLabels[i]);
            }
            // Find and print the youngest person and their birthdate
            int maxDate = 0;
            String maxPerson = "";
            for (int i =0; i< theLabels.Length;i++)
            {
                if (Convert.ToInt32(theArtists[i,2]) > maxDate)
                {
                    maxDate = Convert.ToInt32(theArtists[i,2]);
                    maxPerson = theArtists[i,0] + " " + theArtists[i,1];
                }
            }
            Console.WriteLine(maxPerson + " is youngest " + maxDate);
            Console.ReadKey();
        }
    }
}
