package q05a;

public class Q05a 
{

    public static void main(String[] args) 
	{
        int target = 4;
        int r = 1;
        int rs = 0;
        int rm = 0;

        while (r <= target)
        {
            rs = (int) Math.pow (r, 2);
            rm = r % 4;
            r = r + 1;
        }
    }
}