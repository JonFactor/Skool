namespace Contacts;

public partial class MainPage : ContentPage
{
	int count = 0;

	public MainPage()
	{
		InitializeComponent();
	}

	private void OnCounterClicked(object sender, EventArgs e)
	{
		Color welcomeLblColor;

		count++;
		if (count == 1) { 
			CounterBtn.Text = $"Clicked {count} time";
			welcomeLblColor = Colors.Red;

		}
		else
		{
			CounterBtn.Text = $"Clicked {count} times";
			welcomeLblColor = Colors.Blue;
		}


		WelcomeLbl.TextColor = welcomeLblColor;

		SemanticScreenReader.Announce(CounterBtn.Text);
	}
}

