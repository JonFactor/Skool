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
			//ForLoop(10);

			string[] shrimp = { "pineapple shrimp", "cocnut shrimp", "blackend shrimp", "shrimp gumbo"
				, "shrimp parm"};
			LoopPrint(shrimp, "i like: ");

			Console.ReadKey();
		}

		static void ForLoop(int numberOfTacos)
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

		static void LoopPrint(string[] stringList, string preListMessage)
		{
			foreach(string i in stringList)
			{
				Console.WriteLine($"{preListMessage} {i}");
			}


		}
	}
}
