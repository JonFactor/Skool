using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LoopExploration
{
	internal class Program
	{
		static void Main(string[] args)
		{
			MenuSystem();
			Console.ReadKey();
		}
		static void CountDownTimer()
		{
			// count down timer
			for (int i = 0; i <= 5; i++)
			{
				Console.WriteLine($"Counting down: {i}");
				System.Threading.Thread.Sleep(1000);
			}

			Console.WriteLine("Blast off!");
		}

		static void IterateFruits()
		{
			// iterate over fruits
			string[] fruits = { "apple", "banana", "Cherry" };
			Console.WriteLine("\nList of Fruits:");
			foreach (string f in fruits)
			{
				Console.WriteLine(f);
			}
		}
		static void PassChecker()
		{
			// pass checker
			int[] combination = { 9, 9, 9, 9 };
			for(int i=0; i<=4;)
			{
				Console.WriteLine("Guess " +
					"your {0} number:", i + 1);
				int userGuess = int.Parse(Console.ReadLine());
				if (userGuess == combination[i])
				{
					Console.WriteLine("you guessed this one correctly");
					i++;
				}
				else
				{
					Console.WriteLine("Guess again.");
				}
			}
		}

		static void MenuSystem()
		{
			Console.Clear();
			Console.WriteLine("Menu: \n 1. display fruits \n 2. start countdown \n 3. exit");
			int userOption = int.Parse(Console.ReadLine());

			do
			{
				switch(userOption)
				{
					case 1:
						IterateFruits();
						break;
					case 2:
						CountDownTimer();
						break;
					case 3:
						break;
					default:
						Console.WriteLine("please choose a 1 || 2 || 3");
						break;
				}
				Console.ReadKey();
			}
			while (userOption != 3);
		}

	}
}
