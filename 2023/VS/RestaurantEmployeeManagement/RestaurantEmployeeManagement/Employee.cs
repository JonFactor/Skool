using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RestaurantEmployeeManagement
{
	internal class Employee
	{
		private int id;
		private string firstName;
		private string lastName;
		private string role;
		private double salary;
		private DateTime dateOfHire;

		public int Id
		{
			get { return id; }
			set { id = value; }
		}
		public double Salary
		{
			get { return salary; }
			set { salary = value; }
		}
		public string Role
		{
			get { return role; }
		}
		public Employee(int id, string FirstName, string LastName, string Role, double Salary, DateTime DateOfHire)
		{
			Id = id;
			firstName = FirstName;	
			lastName = LastName;
			role = Role;
			salary = Salary;
			dateOfHire = DateOfHire;
		}
		public void Promote(double salaryIncreaseAmount)
		{
			salary += salaryIncreaseAmount;
		}
		public void Demote(double salaryDecreaseAmount)
		{
			salary -= salaryDecreaseAmount;
		}
		public string FullName()
		{
			return firstName + " " + lastName;
		}
		public int GetId()
		{
			return id;
		}
		public void PrintDetails()
		{
			Console.WriteLine($"ID: {id}\nName: {FullName()}\nRole: {role}\nSalary {salary}\ndate of hire {dateOfHire}");
		}
	}
}
