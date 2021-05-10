using System;

namespace testing
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            string msg = "HEJJJ GUSTAVVVV, DU er en ";
            var rand = new Random();
            while (true){
                int num = rand.Next(1, 20);
                string res = msg + Convert.ToString(num) + "/10";
                Console.ReadKey();
                Console.WriteLine(res);
            }
        }
    }
}