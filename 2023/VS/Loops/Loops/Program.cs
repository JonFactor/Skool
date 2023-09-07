using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Net;

namespace Loops
{
	internal class Program
	{
		static void Main(string[] args)
		{
			ForPrint(10);

			string[] shrimp = { "pineapple shrimp", "cocnut shrimp", "blackend shrimp", "shrimp gumbo"
				, "shrimp parm"};
			ForEachPrint(shrimp, "i like: ");

			WhileLoopPrint(12);

			DoWhileLoopPrint(21);
			Console.ReadKey();
		}

		static void ForPrint(int numberOfTacos)
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

		static void ForEachPrint(string[] stringList, string preListMessage)
		{
			foreach (string i in stringList)
			{
				Console.WriteLine($"{preListMessage} {i}");
			}


		}

		static void WhileLoopPrint(int iterationCount)
		{
			int i = 0;

			while (i < iterationCount)
			{
				Console.WriteLine($"i = {i}");
				i++;
			}
		}

		static void DoWhileLoopPrint(int iterationCount)
		{
			int i = 0;
			do
			{
				Console.WriteLine("Hey there dooood. {0}", i);
				i++;
			}
			while (i < iterationCount);
		}
	}
}
