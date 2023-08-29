using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace txtAdventure
{
	internal class Program
	{
		static void Main(string[] args)
		{
			Random rnd = new Random();

			Console.WriteLine(" You are walking home from work in youngstown. ");

			//traveler
			Console.WriteLine("You meet a traveler.");
			Console.WriteLine("Aproch Him? (y/n)");

			bool approchTraveler = UserInputBool();
			if (approchTraveler)
			{
				Console.WriteLine("He has a gun and robs you if you cant guess" +
					"his favorite number.");
				Console.WriteLine("What is his favorite number (1-2) ?");

				int usersGuess = 0;
				try
				{
					usersGuess = int.Parse(Console.ReadLine());
				}
				catch (Exception ex) 
				{
					Console.WriteLine("input a number 1-2");
				}

				int robbersFavNumber = rnd.Next(2);
				if (usersGuess == robbersFavNumber)
				{
					Console.WriteLine("You are set free!");
				}
				else
				{
					Console.WriteLine("Wrong, you get shot ;-;");
					Console.ReadKey();
					return;
				}

			}

			//dog
			Console.Clear();

			Console.WriteLine("A dog runs up to you!!!");
			Console.WriteLine("Do you run away (y) or greet the dog (n)");

			bool fleeDog = UserInputBool();
            if (fleeDog)
            {
				Console.WriteLine("The dog is now sad ;-;");
            }
			else
			{
				string kindOfDog = "nice";
				if (rnd.Next(2) == 1) 
				{
					kindOfDog = "ulgy";
				}
				else
				{
					kindOfDog = "rat";
				}
				Console.WriteLine($"You meet a {kindOfDog} dog!");
				Console.WriteLine("He now follows you where ever you go");
			}
			Console.ReadKey();

			//cat
			Console.Clear();

			Console.WriteLine("you meet a lot of cats would you like to know there names? (y/n)");
			bool wantToKnowNames = UserInputBool();
            if ( wantToKnowNames)
			{
				string[] catNames = { "gabby", "shabby", "fabby", "nabby", "eabby",
					"walter", "shalter", "baggage", "vabby"};

				Console.WriteLine($"the names are: {string.Join(", ", catNames)}");
            }
			else
			{
				Console.WriteLine("mmmk");
			}
			Console.ReadKey();

			//home
			Console.Clear();

			Console.WriteLine("You made it home :)");
			Console.ReadKey();
        }

		static bool UserInputBool()
		{
			string input = "y";
			while (true)
			{
				try
				{
					input = Console.ReadLine();
				}
				catch (Exception ex)
				{
					Console.WriteLine("invalid input, please try again.");
				}

				if (input == "y")
				{
					return true;
				}
				else if (input == "n")
				{
					return false;
				}
				else
				{
					Console.WriteLine("Please input a y/n");
				}
			}
		}

	}
}
