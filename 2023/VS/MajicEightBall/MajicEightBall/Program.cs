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
			bool keepPlaying = true;

			while(keepPlaying)
			{
				EightBallPlay();
				Console.WriteLine("would you like to exit? (y/n)");

				string userExit = Console.ReadLine();
				if(userExit == "y")
				{
					keepPlaying = false;
				}

			}
		}
		static void EightBallPlay()
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
					answer = "Dont count on it";
					break;
				case 4:
					answer = "Yes, defidently";
					break;
				case 5:
					answer = "You may rely on it";
					break;
				case 6:
					answer = "as i see it, yes";
					break;
				case 7:
					answer = "Most likely.";
					break;
				case 8:
					answer = "Outlook not so good.";
					break;
			}

			Console.WriteLine($"servey says: {answer}");
			Console.ReadLine();
		}
	}
}
