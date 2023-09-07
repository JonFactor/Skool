using System;
using System.Collections.Generic;
using System.ComponentModel.Design.Serialization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MajicEightBall
{
	internal class Program
	{
		static void Main(string[] args)
		{
			Console.WriteLine("Majic Eight Ball: Ask a quesiton...");
			string userQuestion = Console.ReadLine();

			Random ran = new Random();
			int randomNumber = ran.Next(1, 9);

			string answer = "";
			switch (randomNumber)
			{
				case 1:
					answer = "It is certain";
					break;
				case 2:
					answer = "Reply hasty, try again.";
					break;
				case 3:
			}
		}
	}
}
