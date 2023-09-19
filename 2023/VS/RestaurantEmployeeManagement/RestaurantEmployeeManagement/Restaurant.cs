using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace RestaurantEmployeeManagement
{
	internal class Restaurant
	{
		private List<Employee> employees = new List<Employee>();
		public void AddEmployee(Employee employee)
		{
			employees.Add(employee);
		}
		public void RemoveEmployee(int empId)
		{
			foreach (Employee emp in employees)
			{
				if (emp.Id == empId)
				{
					employees.Remove(emp);
					return;
				}
			}
		}
		public Employee GetEmployee(int empId)
		{

			foreach (Employee emp in employees)
			{
				if (emp.Id == empId)
				{
					return emp;
				}
			}
			return null;

		}

		public void DisplayAllEmployees()
		{
			foreach (Employee emp in employees)
			{
				emp.PrintDetails();
			}
		}

		public void UniversalRaise(int percent)
		{
			foreach(Employee emp in employees)
			{
				emp.Promote(emp.Salary * (percent * .01));
			}
		}

		public List<Employee> FindByRole(string roleName)
		{
			List<Employee> filteredEmps = new List<Employee>();

			foreach (Employee emp in employees)
			{
				if (emp.Role == roleName)
				{
					filteredEmps.Add(emp);
				}
			}

			return filteredEmps;
		}
	}
}
