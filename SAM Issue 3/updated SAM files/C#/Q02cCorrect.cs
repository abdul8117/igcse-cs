using System;
namespace Q02c
{
    class Q02c
    {
        static void Main(string[] args)
        {
            int[] attendanceList = { 800, 1499, 1600, 200 };
            int[] incomeList = { 23000, 10000, 47000, 10000 };
            int income;
            int attendance;
            for (int i = 0; i < attendanceList.Length; i++)
            {
                income = incomeList[i];
                attendance = attendanceList[i];
                Console.WriteLine("Attendance: " + attendance + " income: " + income);

                if ((attendance >= 1500) || (income >= 45000))
                    Console.WriteLine("Sufficient profit made this week");
                else if ((attendance >= 750) && (income >= 22500))
                    Console.WriteLine("income in line with attendance this week");
                else if (attendance < 500)
                    Console.WriteLine("Attendance is very low this week.  Contact the fan club.");
                else
                    Console.WriteLine("Possible accounting error.");
            }

            Console.ReadKey();
        }
    }
}
