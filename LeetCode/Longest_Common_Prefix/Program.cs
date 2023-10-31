namespace Longest_Common_Prefix
{
    public class Program
    {
        static void Main(string[] args)
        {
            //Find the longest Common Prefix.
            //First sort the array of the strings and the compare the first and the last string of the sorted array
            Program program = new Program();
            string[] input = { "flower", "flow", "flight" };
            string result = program.LongestCommonPrefix(input);
            Console.WriteLine(result);
        }

        public string LongestCommonPrefix(string[] strs)
        {
            if (strs == null || strs.Length == 0)
            {
                return "";
            }
            Array.Sort(strs); 
            char[] first = strs[0].ToCharArray();
            char[] last = strs[strs.Length - 1].ToCharArray();

            int minLength = Math.Min(first.Length, last.Length);

            for(int i = 0; i < minLength; i++)
            {
                if (first[i] != last[i])
                    return new string(first, 0, i);

            }
            return new string(first, 0, minLength);
            
            //The for loop iterates through characters of the first and last strings upto the minLenth, it chevks if the characters at the same index in both the strings are equal. If they are not, it returns a substring of the
            //first string from index 0 to i
            //the min length bten the character arrrays of the 1st and 2nd string is calculated. This is done to prevent an index out-of-range error in the loop, as the common prefix can't be longer than the shortest string
            //sorts the array in ascending lexicographic order meaning it arranges the strings alphabetical order from A to Z
            //char[] is a datatype that holds an array of characters, strs[0] access the 1st element of an array.ToCharArray(), converts the string into a character array
            //in C#, strings are immutable, which means their contents cannot be modified after creation, converting the string to a character array allwoes you to access and manipulate individual characters in the string
        
        }
    }
}