namespace DataStructure;

public class Program
{
    public static void Main(String[] args)
    {
        Program p = new Program();
        p.WriteName();

        Console.WriteLine(ReturnNumber(90));

        int[] arr = { -10, -1000 };
        // var num = double.NegativeInfinity; //covers the lowest lowest values, double.PositiveInfinity covers all the max max values
        int num = 0;
        for (int i = 0; i < arr.Length; i++)
        {
            if (arr[i] > num)
            {
                num = arr[i];
            }
        }
        Console.WriteLine("my num " + num);

        Console.WriteLine("my other num is " + arr.Max());

    }

    public void WriteName()
    {
        Console.WriteLine("His name Michael and he eats a lot!");
    }

    public static int ReturnNumber(int num)
    {
        return num;
    }
}




