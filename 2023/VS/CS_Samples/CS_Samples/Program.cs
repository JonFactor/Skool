using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Xml;

namespace CS_Samples
{
	internal class Program
	{
		static void Main(string[] args)
		{
			bool retry = true;

			while (retry)
			{ 
				Sample();
				Console.WriteLine("Would you like to retry? (y/n) ");

				while (true)
				{
					string yn = Console.ReadLine();
					if (yn == "y")
					{
						retry = true;
						break;
					}
					else if (yn == "n")
					{
						retry = false;
						break;
					}
					else
					{
						Console.WriteLine("please enter a y/n");
					}
				}

			}

		}

		static string ExpectedInput(char)
		{
			while (true) 
			{ 
				
			}
		}


		static void Sample() 
		{

			Console.ForegroundColor = ConsoleColor.Red;

			Console.WriteLine("Welcome, what is your name.");
			string strName = Console.ReadLine();

			Console.WriteLine($"hello {strName}. Welcome to Codecraft" + "\n hmmmmmmm");
			Thread.Sleep(1000);
			Console.Clear();

			/* Ctrl + D: Duplicate a line. */
			Console.WriteLine("i see you want to see the Coding rapper.");
			Console.WriteLine("i see you want to see the Coding rapper.");
			Console.WriteLine("You may see him with a gift of 100 peices of gold. How many peices do" +
				" you have? ");

			int intAmountOfGold = int.Parse(Console.ReadLine());
			if (intAmountOfGold >= 100)
			{
				Console.WriteLine($"Oh {intAmountOfGold} is a lot of gold, you must be very successful in business. Please follow" +
					"me to The man");
			}
			else
			{
				Console.WriteLine("Go away pesent");
			}





		}
	}
}
