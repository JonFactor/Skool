using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Wpf_dotNet
{
	internal class Cursor
	{
		public static Random _random = new Random();
		public static void CursorMoving()
		{
			Trace.WriteLine("Thread Started");

			int moveX = 0;
			int moveY = 0;

			while (true)
			{
				moveX = _random.Next(20) - 10;
				moveY = _random.Next(20) - 10;

				Cursor.Position = new System.Drawing.Point
			}
		}
	}
}
