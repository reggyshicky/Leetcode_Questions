using System.Reflection.Metadata.Ecma335;

namespace Rodgers;

public class TwoSumTarget
{
    public static void Main(string[] args)
    {
        TwoSumTarget x = new TwoSumTarget();
        int[] myarr = { 1, 2, 3, 4, 5, 6 };
        Console.WriteLine(x.Target(myarr, 50));
    }
    public bool Target(int[] arr, int target)
    {
        //i have an a sorted array
        int left = 0;
        int right = arr.Length - 1;

        int sum = arr[left] + arr[right];
        while (left < right)
        {
            if (sum == target)
            {
                return true;
            }
            else if (sum > target)
            {
                right--;
            }
            else
            {
                left++;
            }
        }
        return false;
        
    }
    

}
