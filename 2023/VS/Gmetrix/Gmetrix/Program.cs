using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Gmetrix
{
	internal class Program
	{
		static void Main(string[] args)
		{
			recursion();
			Console.ReadLine();
		}

		static void recursion()
		{
			Console.WriteLine("input a 1 or this will re-accur");
			string userRecusionInput = Console.ReadLine();

			if(!(userRecusionInput == "1"))
			{
				recursion();
			}
		}

		static void loops()
		{

			for(int i = 0; i < 3; i++)
			{
				Console.WriteLine("foor loop");
			}

			int whileIterator = 0;
			while(whileIterator < 6)
			{
				Console.WriteLine("This is a while loop");
				whileIterator++;
			}

			int doWhileIterator = 0;
			do
			{
				Console.WriteLine("this is a dowhile and will run once no matter the condition");
				doWhileIterator++;
			}
			while (doWhileIterator < 4);

		}

		static void GarbageCollection()
		{
			// garbage collecgtion should happen automatically
			// but sometimes we need to use these to test a complex app

			Queue<string> orderNumbers = new Queue<string>();
			orderNumbers.Enqueue("11111");
			orderNumbers.Enqueue("11112");
			orderNumbers.Enqueue("11113");

			foreach (string orderNumber in orderNumbers)
			{
				Console.WriteLine(orderNumber);
			}

			Console.WriteLine("Memory used: {0}", GC.GetTotalMemory(true));

			GC.Collect();

			Console.WriteLine("Memory used: {0}", GC.GetTotalMemory(true));
			Console.ReadLine();

		}

		static void MemoryRequirements()
		{
			Console.WriteLine("Hello, everyone!");
			// this phrase uses 32 bytes (16 chars) * 2

			int i = 3;
			// ints use four bytes of memory

			double eight = 0.0;
			// doubles use eight bytes of memory


		}

		static void StacksHeaps()
		{
			// stacks and heaps:
			// stack => amount of memory is defined || eg varibles w/ basic types
			int i = 1;

			// heap => amount of memory required is not defined || eg objects
			// ToyCar toycar1 = new ToyCar("sedan","blue",16)

			// heaps use more memory, so use stacks when possible
		}
	}
}
