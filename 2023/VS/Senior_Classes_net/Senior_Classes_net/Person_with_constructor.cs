using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Senior_Classes_net
{
	internal class Person_with_constructor
	{
		private string name;
		private int age;
		private double height;

		public string Name
		{
			get { return name; }
			set { name = value; }
		}
		public int Age
		{
			get { return age; }
			set { age = value; }
		}
		public double Height
		{
			get { return height; }
			set { height = value; }
		}

		public void Intro()
		{
			Console.WriteLine($"Hello, my name is {name} and i am {age} years old. I am {height} ft tall");
		}
		public Person_with_constructor(string Name, int Age, double Height)
		{
			name = Name;
			age = Age;
			height = Height;
		}
	}
}
