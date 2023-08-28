using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace Basic_Data_Types2
{
	internal class Program
	{
		static void Main(string[] args)
		{
			//StringDataTypes();

			OperatorandNumbers();

			Console.ReadKey();
		}

		static void StringDataTypes()
		{
			string firstName;
			string lastName;
			string esport;

			Console.Write("howdy what is first name? \n ");
			firstName = Console.ReadLine();

			Console.Write("Whats your last name? \n");
			lastName = Console.ReadLine();

			Console.Write("What esport are you registering for? \n");
			esport = Console.ReadLine();

			Console.Clear();
			Console.WriteLine("Welcome " + firstName + " " + lastName + "." +
				"i have you regiseted for " + esport);

		}

		static void OperatorandNumbers()
		{
			double num1 = 0;
			double num2 = 0;
			double num3 = 0;	
			double num4 = 0;
			double[] numbers = { num1, num2, num3, num4 };

			int iterator = 0;
			while (iterator < 5)
			{
				Console.WriteLine($"Enter A Value for your {iterator + 1} number: ");
				numbers[iterator] = double.Parse(Console.ReadLine());
			}

			double addition = num1 + num2;	
			double sutraction = num1 - num2;
			double mulitplication = num1 * num2;
			double division = num1 / num2;

			Console.WriteLine($"Addition of {num1} + {num2} = {addition}");
			Console.WriteLine($"Subtraction of {num1} - {num2} = {sutraction}");
			Console.WriteLine($"Multiplication of {num1} * {num2} = {mulitplication}");
			Console.WriteLine($"Divison of {num1} / {num2} = {division}");

		}
	}
}
