using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using System.Windows.Forms;

namespace WpfApp2
{
    class ThreadingSamples
    {
        public static Random _random = new Random();

        public static void CrazyMouseThread()
        {
            Trace.WriteLine("lol");

            int moveX = 0;
            int moveY = 0;

            int randomSize = 20;
            while (true)
            {
                moveX = _random.Next(randomSize);
                moveY = _random.Next(randomSize);

                System.Windows.Forms.Cursor.Position = new System.Drawing.Point(
                    )
            }
        }
    }
}
