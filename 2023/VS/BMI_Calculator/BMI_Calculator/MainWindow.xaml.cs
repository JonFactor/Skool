using System;
using System.Collections.Generic;
using System.Data;
using System.IO;
using System.Linq;
using System.Reflection;
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
using System.Xml;
using System.Xml.Serialization;


namespace BMI_Calculator
{
	/// <summary>
	/// Interaction logic for MainWindow.xaml
	/// </summary>
	[XmlRoot("BMI Calc", Namespace = "www.bmicalc.ninja")]
	public partial class MainWindow : Window
	{

		public string FilePath = "..//..//..//BMI_Calculator/";
		public string FileName = "yourBMI.xml";

		public class Customer
		{
			[XmlAttribute("Last Name")]
			public string firstName { get; set; }
			[XmlAttribute("First Name")]
			public string lastName { get; set; }
			[XmlAttribute("Phone Number")]
			public string phoneNumber { get; set; }
			[XmlAttribute("Height")]
			public int heightInches { get; set; }
			[XmlAttribute("Weight")]
			public int weightLbs { get; set; }
			[XmlAttribute("Customer BMI")]
			public int custBMI { get; set; }
			[XmlAttribute("Status")]
			public string statusTitle { get; set; }

			public Customer(string FirstName, string LastName, string PhoneNumber, int HeightInches, int WeightLbs, int CustBMI, string StatusTitle)
			{
				firstName = FirstName;
				lastName = LastName;
				phoneNumber = PhoneNumber;
				heightInches = HeightInches;
				weightLbs = WeightLbs;
				custBMI = CustBMI;
				statusTitle = StatusTitle;
			}

			public Customer()
			{

			}
		}

		List<TextBox> entrys = new List<TextBox>();
		public MainWindow()
		{
			InitializeComponent();
			loadStats();

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
			if (nullInList())
			{
				MessageBox.Show("Please fill in all entrys.");
				return;
			}
			int height = Int32.Parse(xHeightInchesBox.Text);
			int weight = Int32.Parse(entrys[3].Text);
			double bmi = weight / (double)Math.Pow(height, 2);
			bmi = (int)Math.Round(bmi * 703);
			string bmiStatus = BmiStatusCalc((int)bmi);

			Customer customer1;
			try
			{
				customer1 = new Customer(entrys[0].Text, entrys[1].Text, entrys[2].Text, Int32.Parse(entrys[4].Text), Int32.Parse(entrys[3].Text),(int)bmi, bmiStatus);
			}
			catch
			{
				MessageBox.Show("Enter all information in the intended format.");
				return;
			}

			lblBmi.Content = bmi;
			lblMessage.Content = bmiStatus;

			if (!File.Exists(FilePath + FileName))
			{
				FileStream fs = File.Create(FilePath + FileName);
				File.WriteAllText(FilePath + FileName, "<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n<Customer xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" Last_x0020_Name=\"Jon\" First_x0020_Name=\"Bob\" Phone_x0020_Number=\"33303333\" Height=\"432\" Weight=\"3412\" Customer_x0020_BMI=\"13\" Status=\"UnderWeight\" />".Replace("/", "//"));
			}

			TextWriter writer = new StreamWriter(FilePath + FileName);
			XmlSerializer serializer = new XmlSerializer(typeof(Customer));
			serializer.Serialize(writer, customer1);
			writer.Close();

			loadStats();

			MessageBox.Show($"The data you entered is: {string.Join("\n", customer1)}\nBmi: {bmi}\nBmi Status: {bmiStatus}", "BMI MESSAGE");
		}		
		private string BmiStatusCalc(int bmi)
		{
			string status = "NA";

			if (bmi < 18.5)
			{
				status = "UnderWeight";
			}
			else if (bmi < 24.9)
			{
				status = "Normal"; 
			}
			else if (bmi < 29.9)
			{
				status = "Overweight";
			}
			else
			{
				status = "Obese";
			}

			return status;
		}
		private void loadStats()
		{
			Customer tempCust = new Customer();

			XmlSerializer des = new XmlSerializer(typeof(Customer));
			using (XmlReader reader = XmlReader.Create(FilePath + FileName))
			{
				tempCust = (Customer)des.Deserialize(reader);

				xLastNameBox.Text = tempCust.lastName;
				xFirstNameBox.Text = tempCust.firstName;
				xPhoneBox.Text = tempCust.phoneNumber;
			}

			DataSet xmlData = new DataSet();
			xmlData.ReadXml(FilePath + FileName, XmlReadMode.Auto);
			xDataGrid.ItemsSource = xmlData.Tables[0].DefaultView;
		}

		private bool nullInList()
		{
			foreach(TextBox tx in entrys)
			{
				if (String.IsNullOrWhiteSpace(tx.Text))
				{
					return true;
				}
			}

			return false;
		}
	}
}
