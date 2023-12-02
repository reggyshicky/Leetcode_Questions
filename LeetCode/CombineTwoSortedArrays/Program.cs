using System.ComponentModel.DataAnnotations;

namespace CombineTwoSortedArrays
{
    public class Program
    {
        static void Main(string[] args)
        {
            Program program = new Program();
            int[] arr1 = { 1, 2, 3, 4, 5 };
            int[] arr2 = { 10, 15, 25, 29 };
            List<int> results = program.AddTwoSortedArrays(arr1, arr2); 

            foreach(int element in results)
            {
                
                Console.WriteLine(element + " ");
            }
        }

        public List<int> AddTwoSortedArrays(int[] arr1, int[] arr2)
        {
            List<int> list = new List<int>();
            int i = 0;
            int j = 0;

            while (i < arr1.Length && j < arr2.Length)
            {
                if (arr1[i] < arr2[j])
                {
                    list.Add(arr1[i]);
                    i++;
                } 
                else
                {
                    list.Add(arr2[j]);
                    j++;
                }
            }
            while (i < arr1.Length)
            {
                list.Add(arr1[i]);
                i++;
            }
            while (j < arr2.Length)
            {
                list.Add(arr2[j]);
                j++;
            }
            return list;
            
        } 
    }
}