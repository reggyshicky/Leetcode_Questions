namespace Palindrome_Numbers
{
	public class Program
	{
		static void Main(string[] args)
		{
			palidrome_Number palindromeNUm = new palidrome_Number();
			Console.WriteLine(palindromeNUm.IsPalindrome(124));
			Program program = new Program();
			Console.WriteLine(program.palindrome("radar"));
			Console.WriteLine(program.palindrome("radaj"));

        }

		//testing for a palindrome -str
		public bool palindrome(String str)
		{
			str = str.ToLower();
			int left = 0;
			int right = str.Length - 1;

			while (left < right)
			{
				if (str[left] != str[right])
				{
					return false;
				}
				else
				{
					left++;
					right--;
				}
			}
			return true;
		}
	}
}