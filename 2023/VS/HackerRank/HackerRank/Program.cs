using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;
using System.Numerics;

class Result
{

	/*
     * Complete the 'extraLongFactorials' function below.
     *
     * The function accepts INTEGER n as parameter.
     */

	public static void extraLongFactorials(int n)
	{
		long sum = n;
		List<long> valuesToZero = new List<long>();
		for (int i = n; i != 0; i--)
		{
			valuesToZero.Add(i);
		}
		foreach (int i in valuesToZero)
		{
			sum = sum + (i * valuesToZero[valuesToZero.IndexOf(i) - 1]);
		}
		Console.WriteLine(sum);
		Console.ReadLine();
	}

}

class Solution
{
	public static void Main(string[] args)
	{
		int n = Convert.ToInt32(Console.ReadLine().Trim());

		Result.extraLongFactorials(n);
	}
}
