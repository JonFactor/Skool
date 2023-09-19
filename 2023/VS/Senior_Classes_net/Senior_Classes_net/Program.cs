using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Senior_Classes_net
{
	internal class Program
	{
		static void Main(string[] args)
		{
			Person_Class();
			Console.ReadLine();
		}
		static void Person_Class()
		{
			Person_with_constructor person = new Person_with_constructor("John", 17, 6.4);
			person.Intro();

			List <Person_with_constructor> employee = new List<Person_with_constructor>()
			{
				new Person_with_constructor("John", 17, 6.4), new Person_with_constructor("1", 17, 6.4), new Person_with_constructor("2", 17, 6.4),
				new Person_with_constructor("3", 17, 6.4), new Person_with_constructor("4", 17, 6.4)
			};

			foreach(Person_with_constructor emp in  employee)
			{
				emp.Intro();
			}
		}
	}
}
