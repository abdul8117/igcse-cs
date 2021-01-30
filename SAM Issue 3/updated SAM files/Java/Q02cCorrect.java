package q02c;
public class Q02c 
{
    public static void main(String[] args) 
    {
        int[] attendanceList = {800, 1499, 1600, 200};
        int[] incomeList = {23000, 10000, 47000, 10000};
        int income;
        int attendance;
        
        for (int i=0; i<attendanceList.length; i++)
        {
           income = incomeList[i];
           attendance = attendanceList[i];
           System.out.println("Attendance: " + attendance + " income: " + income);

           if ((attendance >= 1500) || (income >= 45000))
               System.out.println("Sufficient profit made this week");
           else if ((attendance >= 750) && (income >= 22500))
               System.out.println("income in line with attendance this week");
           else if (attendance < 500)
               System.out.println("Attendance is very low this week.  Contact the fan club.");
           else
               System.out.println("Possible accounting error.");
         }   
    }   
}
