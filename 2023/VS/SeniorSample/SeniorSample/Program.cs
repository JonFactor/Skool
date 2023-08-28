using System;
using System.Collections.Generic;
using System.Diagnostics.Eventing.Reader;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SeniorSample
{
	internal class Program
	{
		static void Main(string[] args)
		{
			string msgWelcome = "woah";
			Console.WriteLine(msgWelcome);

			if (DateTime.Now.DayOfWeek == DayOfWeek.Tuesday)
			{
				Console.WriteLine("first of the month")
			}
            else if (DateTime.Now.DayOfWeek == DayOfWeek.Wednesday)
            {
                 

            }
            Console.ReadKey();
		}


	}
}
