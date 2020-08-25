using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Learning
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Hvor gammel er du?: ");
            int age = Convert.ToInt32(Console.Read());
            if (age >= 17)
            {
                Console.WriteLine("Nice man u good");
            }    
        }
    }
}
