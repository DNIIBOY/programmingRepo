using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace testPoop
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("--------Primtals Generator--------");
                Console.Write("Hvad er det højeste primtal du vil se?: ");
                int usr = Convert.ToInt32(Console.ReadLine());
                List<int> nums = prim(usr);
                foreach (int i in nums)
                {
                    Console.Write(i+", ");
                }
                Console.WriteLine();
            }
        }

        static List<int> prim(int n)
        {
            List<int> primes = new List<int>();
            
            for (int i = 2; i < n; i++)
            {
                bool isPrime = true;
                for (int x = 2; x < i; x++)
                {
                    if (i % x == 0)
                    {
                        isPrime = false;
                    }
                }
                if (isPrime)
                {
                    primes.Add(i);
                }
            }
            return primes;
        }
    }
}