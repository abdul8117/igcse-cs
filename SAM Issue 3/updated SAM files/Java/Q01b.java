public class Q01b 
{
    public static void main(String[] args) 
	{
        int x = 44;
        int t = 0;
        for(int i=0; i<60; i++){
            t = t + i - x + 12;
            if(i >= 10)
                System.out.println(i * 10 / 14);
            else
                System.out.println(i);
        }
        System.out.println(t);        
    }    
}
