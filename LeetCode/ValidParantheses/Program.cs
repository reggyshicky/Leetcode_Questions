namespace ValidParantheses
{
    public class Program
    {
        static void Main(string[] args)
        {
            Program program = new Program();
            string myString = "()[]{}";
            bool results = program.IsValid(myString);
            Console.WriteLine(results);
        }
        public bool IsValid(string str)
        {
            Stack<char> stack = new Stack<char>(); //this creates a stack of characters to keep track of the open brackets we encounter as we iterate through the input string

            foreach (char c in str)
            {
                if (c == '(' || c == '{' || c == '[')
                {
                    stack.Push(c);
                }
                else
                {
                    if (stack.Count == 0)
                    {
                        return false;
                    }
                    char openBracket = stack.Pop();
                    if ((c == ')' && openBracket != '(') ||
                        (c == '}' && openBracket != '{') ||
                        (c == ']' && openBracket != '['))
                    {
                        return false;
                    }
                }
            }
            return stack.Count == 0; //All brackets should be matched and closed
        }
    }
}