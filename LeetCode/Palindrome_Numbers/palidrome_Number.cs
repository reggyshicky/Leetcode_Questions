using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Palindrome_Numbers
{
	public class palidrome_Number
	{
		
		public bool IsPalindrome(int x)
		{
			int OriginalX = x; //store the original number
			int reverse = 0;
			int remainder;
			while (x > 0)
			{
				remainder = x % 10;
				reverse = reverse * 10 + remainder;
				x = x / 10;
			}
			return OriginalX == reverse; //compare the original number with the reversed number
		}
		

	}
}



//Question: Given an integer x, return true if x is a palindrome and false otherwise