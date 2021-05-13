using System;

namespace pythoagoras
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("------------Pythagoras-------------");
            Console.WriteLine("Skriv 0 for ukendt");
            Console.Write("Indsæt a: ");
            double a = Convert.ToDouble(Console.ReadLine());
            Console.Write("Indsæt b: ");
            double b = Convert.ToDouble(Console.ReadLine());
            Console.Write("Indsæt c: ");
            double c = Convert.ToDouble(Console.ReadLine());

            double num = pythagoras(a, b, c);
            Console.WriteLine($"Ukendt: {num}");
        }

        static double pythagoras(double a = 0, double b = 0, double c = 0)
        {
            if (a == 0 && b != 0 && c != 0)
            {
                return Math.Sqrt(c * c - b* b);
            }
            else if (a != 0 && b == 0 && c != 0)
            {
                return Math.Sqrt(c * c - a * a);
            }
            else if (a != 0 && b != 0 && c == 0)
            {
                return Math.Sqrt(a * a + b * b);
            }
            else
            {
                return 0;
            }
        }
        
    }
}