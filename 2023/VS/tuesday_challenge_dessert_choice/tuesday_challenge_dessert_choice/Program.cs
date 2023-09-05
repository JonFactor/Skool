using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace tuesday_challenge_dessert_choice
{
	internal class Program
	{
		static void Main(string[] args)
		{
			Desert_Choice();
		}

		static void Desert_Choice()
		{
			List<string> yesNoFeilds = new List<string>();
			yesNoFeilds.Add("y");
			yesNoFeilds.Add("n");

			string wantsDesert = RestrictedUserInput("would you like desert? (y/n)", yesNoFeilds);
			Console.Clear();
			if (wantsDesert == "y")
			{
				Console.WriteLine("Awesome ill grab you a dessert menu");
				Console.ReadKey();

				List<string> foodOptions = new List<string>();
				foodOptions.Add("rose waer rice pudding");
				foodOptions.Add("Tres Leches Cake");
				foodOptions.Add("Kulfi");
				foodOptions.Add("Bread Pudding");
				foodOptions.Add("Beigents");

				string finalChoice = RestrictedUserInput($"please select a option of the following: \n" +
					$"{string.Join("\n", foodOptions)}", foodOptions);

				Console.WriteLine($"excellent choice i will grab your {finalChoice} right away.");
			}
			else
			{
				Console.WriteLine("No worries ill grab your check");
			}


			Console.ReadLine();
		}

		static string RestrictedUserInput(string displayTxt, List<string> correctFeilds)
		{

			string usersInput = "";
			while (true)
			{
				Console.WriteLine(displayTxt);
				 usersInput = Console.ReadLine();

				foreach(string feild in correctFeilds)
				{
					if (feild == usersInput)
					{
						return usersInput;
					}

				}

				Console.WriteLine($"please input one of the following: {string.Join(", ", correctFeilds)}");
			}

		}
	}
}
