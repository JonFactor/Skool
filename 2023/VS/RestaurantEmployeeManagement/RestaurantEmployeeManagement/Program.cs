using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RestaurantEmployeeManagement
{
	internal class Program
	{
		static void Main(string[] args)
		{

			// test employee
			Employee john = new Employee(1, "Joe", "Phise", "manager", 12, DateTime.Now);

			// demote
			john.Demote(2);
			john.PrintDetails();
			Console.ReadLine();
			Console.Clear();

			// promote
			john.Promote(2);
			john.PrintDetails();
			Console.ReadLine();
			Console.Clear();

			List<Employee> staff = new List<Employee>()
			{
				new Employee(2, "Joe", "Phise", "manager", 12, DateTime.Now),
				new Employee(3, "Dan", "Phise", "owner", 100, DateTime.Now),
				new Employee(4, "Greg", "Phise", "team member", 11, DateTime.Now),
				new Employee(5, "Ralph", "Phise", "team member", 11, DateTime.Now),
			};

			// restruant
			Restaurant starbucks = new Restaurant();
			foreach (Employee s in staff)
			{
				starbucks.AddEmployee(s);
			}

			// display all
			starbucks.DisplayAllEmployees();
			Console.ReadLine();
			Console.Clear();

			// remove select emp
			starbucks.RemoveEmployee(3);
			starbucks.DisplayAllEmployees();
			Console.ReadLine();
			Console.Clear();

			// add new emp
			starbucks.AddEmployee(john);
			starbucks.DisplayAllEmployees();
			Console.ReadLine();
			Console.Clear();

			// add universal raise
			starbucks.DisplayAllEmployees();
			Console.ReadLine();
			starbucks.UniversalRaise(50);
			starbucks.DisplayAllEmployees();
			Console.ReadLine();
			Console.Clear();

			// find by role
			List<Employee> teamMembers = starbucks.FindByRole("team member");
			foreach (Employee teamMember in teamMembers)
			{
				teamMember.PrintDetails();
			}
			Console.ReadLine();
			Console.Clear();

		}
	}
}
