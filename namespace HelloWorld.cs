namespace HelloWorld
using System.Threading;
{
    class Program
    {
        static void Main(string[] args)
        {
            //Console.WriteLine("Hello World!");
            
            System.Console.WriteLine("Hello World!");

            string ok = System.Console.Readline();
            public int a = 0 + 1;

            public int b = 5%2;

            b++;


            b *= 2;
            b /= 2;

            if (b == 1 || b == 2)
            {
                Thread.Sleep(1);
                System.Console.WriteLine("b is 1 or 2");
            }
            else if (!(b == 3))
            {
                System.Console.WriteLine("b is 3");
            }
            else
            {
                System.Console.WriteLine("b is not 1, 2 or 3");
            }

            for (int i = 0; i < 5; i++)
            {
                if (i == 2)
                {
                    break;

                }
                System.Console.WriteLine(i);
            }
                char[] array = {'a', 'b', 'c', 'd', 'e'};

                Console.WriteLine(array[2]);

                for (int i = 0; i < array.Length; i++)
                {
                    System.Console.WriteLine(array[i]);
                }

                array.sort(array);

            while (i < 5) {
                System.Console.WriteLine(i);
                i++;
            }

            foreach (char letter in array)
            {
                System.Console.WriteLine(letter);
            }



            int maximum = Math.Max(5, 10);

            int minimum = Math.Min(5, 10);

            int absolute = Math.Abs(-4);

            int power = Math.Pow(4, 2);

            int square = Math.Sqrt(16);

            int cube = Math.Cbrt(8);

            int round = Math.Round(4.7);

            int ceil = Math.Ceiling(4.2);

            int floor = Math.Floor(4.7);

            int random = Math.Random(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

            string var = "Hello World!";

            int legnth = var.Length;

            string upper = var.ToUpper();

            string lower = var.ToLower();

            string sub = var.Substring(6);

            string replace = var.Replace("Hello", "Hi");

            string concat = var.Concat(" How are you?");

            string[] split = var.Split("l");

            Console.WriteLine(split);

            string[] arr = new string[5];




        }
    }
}

// yield return new WaitForSeconds(1f);

//public bool this = true;
/*
bool
char
string
int
float
double
*/

// void


// if

// || && += -= <= >= == !=

//Debug.Log
// Console.writeline

/*

*/