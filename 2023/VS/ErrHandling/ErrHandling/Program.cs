using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ErrHandling
{
	internal class Program
	{
		static void Main(string[] args)
		{
			string[] names = {"JOE" };

			try
			{
				Console.WriteLine("Input a 0: ");
				int index = int.Parse(Console.ReadLine());

				Console.WriteLine(names[index]); // out of index range err
			}
			catch (Exception ex)
			{
				Console.WriteLine($"These was an error: \n {ex}");
			}

			Console.ReadLine();

		}
	}
}
