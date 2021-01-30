public class Q01cCorrect 
{
    public static void main (String[] args)
	{
        int total = 0;
        for (int i=10;i<=100;i+=10)
		{
            total = total + i;
            if(i % 2 == 0)
                System.out.println("Even");
            else
			{
                System.out.println("Odd");
			}
        }
        System.out.println(total);
    }    
}
