using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace Loops
{
	internal class Program
	{
		static void Main(string[] args)
		{
			ForLoop(10);
			Console.ReadKey();
		}

		static void ForLoop(int numberOfTacos = 10)
		{

			// initilizer; condition; iterator
			for (int i = 0; i < numberOfTacos; i++)
			{
				Console.WriteLine(i);
			}

			for (int i = 0; i < numberOfTacos; numberOfTacos--)
			{
				Console.WriteLine($"i have {numberOfTacos} Tacos");
				System.Threading.Thread.Sleep(10);
			}

			Console.WriteLine("now i am sad because i have no tacos");

		}
	}
}
