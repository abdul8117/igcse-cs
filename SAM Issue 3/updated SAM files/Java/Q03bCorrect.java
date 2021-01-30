public class Q03b
{
    String theDate = "";
    
    private static double toCelsius (double inTemp)
    {
        double celsius = 0;
        celsius = (5.0 / 9.0) * (inTemp - 32.0);
        return celsius;
    }

    private static double toFahrenheit (double inTemp)
    {
        double fahrenheit = ((9.0 / 5.0) * inTemp) + 32.0;
        return fahrenheit;
    }
    
    private static void waitTenSeconds () throws InterruptedException
    {
          Thread.sleep(10000);
    }
    
    private static void waitTime (int inMilliseconds) throws InterruptedException
    {
           Thread.sleep(inMilliseconds);
    }
    
    public static void main(String[] args) throws InterruptedException
    {
        System.out.println(toFahrenheit(0));
        System.out.println(toCelsius (212.0));  // This line does not work properly
        System.out.println("Sleeping for 10");
        waitTenSeconds();
        System.out.println (toCelsius (32.0));
        System.out.println ("Sleeping for 5");
        waitTime(5000);
        System.out.println (toFahrenheit (100.0));
    }  
}

