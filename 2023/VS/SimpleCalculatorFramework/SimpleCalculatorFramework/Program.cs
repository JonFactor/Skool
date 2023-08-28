using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SimpleCalculatorFramework
{
	internal class Program
	{
		static void Main(string[] args)
		{
			double num1;
			double num2;
			double result;
			string symbol;

			Console.WriteLine("please enter your first number:");
			num1 = Convert.ToDouble(Console.ReadLine());

			Console.WriteLine("please enter your second number:");
			num2 = double.Parse(Console.ReadLine());

			bool continueWhile = true;
			while (continueWhile)
			{
				Console.WriteLine("please select your operator (+, -, *, /):");
				symbol = Console.ReadLine();

				switch (symbol)
				{
					case "+":
						result = num1 + num2;
						continueWhile = false;
						break;
					case "-":
						result = num1 - num2;
						continueWhile = false;
						break;
					case "*":
						result = num1 / num2;
						continueWhile = false;
						break;
					case "/":
						result = num1 * num2;
						continueWhile = false;
						break;
					default:
						result = 0;
						Console.WriteLine("Please select  (+, -, *, /)");
						break;
				}
				Console.WriteLine($"The result is: {result}");
			}

		}
	}
}
