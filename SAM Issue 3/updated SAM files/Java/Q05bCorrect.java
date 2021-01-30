import java.util.Scanner;
public class Q05b 
{
    public static void main(String[] args) 
    {
		// Write your code here	
        Scanner input = new Scanner(System.in);
        int totalSpend = 0;
        System.out.println ("What is your total spend?");
        totalSpend = input.nextInt();
       
        if (totalSpend > 300)
            System.out.println ("Discount is 10%");
        else if (totalSpend > 0)
            System.out.println ("No discount");
        else
            System.out.println ("Invalid input");
    }
}
