using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Conditionals
{
	internal class Program
	{
		static void Main(string[] args)
		{
			IfElseStuff();

			Console.ReadKey();

			SwtichStatments();

			Console.ReadKey();
		}

		static void IfElseStuff()
		{
			Console.WriteLine("enter the gold you have:");
			double goldBalence = double.Parse(Console.ReadLine());
			Console.WriteLine($"Your gold balence is: {goldBalence}");

			if (goldBalence >= 400)
			{
				Console.WriteLine("Congrats you have emough to buy a ticket for " +
					" you and your friend");
			}	
			else if (goldBalence >= 200)
			{
				Console.WriteLine("Congrats you can buy a ticket");
			}
			else
			{
				Console.WriteLine("Too bad, get more money broke boy");
			}
		}

		static void SwtichStatments()
		{
			Console.WriteLine("what is your current grade: ");
			char grade = char.Parse(Console.ReadLine().ToLower());
			Console.WriteLine(grade);

			switch (grade)
			{
				case 'a':
					Console.WriteLine("your pretty smart :) welcome to the team");
					break;
				case 'b':
					Console.WriteLine("not bad :) you made the team");
					break;
				case 'c':
					Console.WriteLine("you should study more but u made it");
					break;
				case 'd':
					Console.WriteLine("you barley made it");
					break;
				default:
					Console.WriteLine("No esports for you go study :)");
					break;
			}
		}
	}
}
