using System.ComponentModel.Design;

namespace Pascal_Triangle
{
    public class Program
    {
        //return a list of lists of the past triangle
        static void Main(string[] args)
        {
            Program program = new Program();
            List<List<int>> results = program.Pascal_Triangle(5);
            foreach(List<int> newlist in results)
            {
                Console.WriteLine(string.Join(" ", newlist));

            }
           
        }

        public List<List<int>> Pascal_Triangle(int n)
        {
            //n is the number of rows
            List<List<int>> listoflists = new List<List<int>>();

            for(int x = 0; x < n; x++)
            {
                List<int> list = new List<int>();

                for (int y = 0; y<=x; y++)
                {
                    if (y == 0 || y == x)
                    list.Add(1);
                    else
                    {
                        list.Add(listoflists[x - 1][y] + listoflists[x - 1][y - 1]);
                        
                    }
                  
                }
                listoflists.Add(list);
                
            }
            return listoflists;
        }
    }
}

/*
 * In Pascal's Triangle, each row has a number of elements equal to its row number (starting from row 0). For example:

Row 0 has 1 element.
Row 1 has 2 elements.
Row 2 has 3 elements.
Row 3 has 4 elements.
And so on. This pattern is represented by the loop condition y <= x. When x is 0, the loop will iterate only once (for y = 0). When x is 1, the loop will iterate twice (for y = 0 and y = 1), and so on.

The purpose of this loop is to iterate over the elements in the current row (ct) and calculate their values based on the conditions specified in the if-else block. It ensures that the loop iterates over the correct range of indices for the current row in Pascal's Triangle.

So, in summary, the condition y <= x ensures that the loop iterates over the valid indices for the current row, where y varies from 0 to the row number (x).
 */