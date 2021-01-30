public class Q01a 
{
    public static void main(String[] args) 
	{
        int[] myNumbers = {20, 30, 40, 50};
        int total = 0;
        for(int i=5; i<15; i++)
		{
            total = total + i;
            if (i < 10)
                System.out.println(i * 10 );
            else
                System.out.println(i);
        }
        System.out.println(total);
    }
}