using System;

namespace Q05a
{
    class Program
    {
        static void Main(string[] args)
        {
            int target = 4;
            int r = 1;
            int rs = 0;
            int rm = 0;

            while (r <= target)
            {
                rs = (int) Math.Pow (r, 2);
                rm = r % 4;
                r = r + 1;
            }
        }
    }
}