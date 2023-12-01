using System.ComponentModel;

namespace Nigel;

public class TwoSumTarget
{
    public static void Main(string[] args)
    {
        TwoSumTarget instance = new TwoSumTarget();
        int[] myarr = { 1, 2, 3, 4, 5 };
        Console.WriteLine(instance.TwoSum(myarr, 9));
    }
    public bool TwoSum(int[] arr, int target)
    {

        //This approach is used for a sorted array
        int left = 0;
        int right = arr.Length - 1;

        while (left < right)
        {
          
            if (arr[left] + arr[right] > target)
            {
                right--;
            }
            else if (arr[right] + arr[left] < target)
            {
                left++;
            }
            else
            {
                return true; //the numbers were found
            }

        }
        return false;
    }
}


