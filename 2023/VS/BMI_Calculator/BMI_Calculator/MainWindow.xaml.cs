using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace BMI_Calculator
{
	/// <summary>
	/// Interaction logic for MainWindow.xaml
	/// </summary>
	public partial class MainWindow : Window
	{
		List<TextBox> entrys = new List<TextBox>();
		public MainWindow()
		{
			InitializeComponent();

			entrys = new List<TextBox>() {
				xFirstNameBox, xLastNameBox, xPhoneBox, xWeightLbsBox, xHeightInchesBox
			};

		}

		private void ClearBtn_Click(object sender, RoutedEventArgs e)
		{
			foreach (TextBox c in entrys)
			{
				if ((string.IsNullOrEmpty(c.Text)))
				{
					continue;
				}

				c.Text = "";
			}
		}

		private void ExitBtn_Click(object sender, RoutedEventArgs e)
		{
			Environment.Exit(0);
		}

		private void SubmitBtn_Click(object sender, RoutedEventArgs e)
		{

		}
	}
}
