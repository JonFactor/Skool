using System.Text;

namespace CS_330_JonFactor
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		private void Form1_Load(object sender, EventArgs e)
		{
			try
			{
				loadAwnserFromTxt();
			}
			catch (Exception ex)
			{
				MessageBox.Show(ex.ToString());
				return;
			}
		}

		private async void loadAwnserFromTxt()
		{
			StringBuilder FeildsFromText = new StringBuilder();

			char[] result;
			string filePath = "C:\\Users\\Factor_Jon\\Documents\\GitHub\\Skool\\2023\\VS\\CS_330_JonFactor\\CS_330_JonFactor\\quizquestion.txt";
			using (StreamReader sr = File.OpenText(filePath))
			{
				result = new char[sr.BaseStream.Length];
				await sr.ReadAsync(result, 0, (int)sr.BaseStream.Length);
			}

			foreach (char c in result)
			{
				if (char.IsLetterOrDigit(c))
				{
					StringBuilder.ap
				}
			}
		}
	}
}