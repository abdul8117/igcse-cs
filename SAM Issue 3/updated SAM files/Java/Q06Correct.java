package q06;
import java.util.ArrayList;
public class Q06 {

    public static void main(String[] args) {
        String[][] theArtists = {{"Andy", "Warhol", "1928"},
        {"Pablo", "Picasso", "1881"},
        {"Salvador", "Dali", "1904"},
        {"Lavinia", "Fontana", "1552"},
        {"Jackson", "Pollock", "1912"},
        {"Henri", "Matisse", "1869"},
        {"Frida", "Kahlo", "1907"},
        {"Georgia", "O'Keeffe", "1887"},
        {"Kara", "Walker", "1969"},
        {"Yayoi", "Kusama", "1929"}
        };

        ArrayList<String> theLabels = new ArrayList ();  // Put the new user labels into this structure
        
		// Make the artist labels
        for (int i = 0; i < theArtists.length; i++) {
            String newRecord = String.valueOf(theArtists[i][1].charAt(0))
                    + String.valueOf(theArtists[i][0].charAt(0))
                    + theArtists[i][2];
            theLabels.add (newRecord);
            System.out.println(newRecord);
            System.out.println("The new userIDs are: " + theLabels.get(theLabels.size() - 1));
        }
		
        // Find and print the youngest person and their birthdate
        int maxDate = 0;
        String maxPerson = "";
        for (String[] person : theArtists) {
            if (Integer.parseInt(person[2]) > maxDate) {
                maxDate = Integer.parseInt(person[2]);
                maxPerson = person[0] + " " + person[1];
            }
        }
        System.out.println(maxPerson + " is youngest " + maxDate);
    }
}
