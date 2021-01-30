import java.util.Scanner;
public class Q02a 
{
    public static void main (String[] args)
	{
        Scanner input = new Scanner(System.in);
		
		// Print prompt and take country from user			
        System.out.print("Enter the country you are visiting from: ");
        String country = input.next();
		
		// Tell the user their country		
        System.out.println("You are from: " + country);
		
		// Take number of adults in party from user			
        System.out.print("Enter the number of adults in your party: ");
        int adults = input.nextInt();
		
		// Take number of children in party from user		
        System.out.print("Enter the number of children in your party: ");
        int children = input.nextInt();        
		
		// Calculate total number in party		
        int total = adults + children;
		
		// Tell the user the total number of people in their party		
        System.out.println("The total in your party is: " + total);    

    }   
}
