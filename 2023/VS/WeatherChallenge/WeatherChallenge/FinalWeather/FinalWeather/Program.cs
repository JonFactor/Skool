using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace FinalWeather
{
	internal class Program
	{
		static void Main(string[] args)
		{
			Task<string> weatherRaw = requesting();
			string weatherString = weatherRaw.Result.ToString();

			dynamic weatherJson = JsonConvert.DeserializeObject(weatherString);

			dynamic Days = weatherJson.properties.periods;

			Console.WriteLine(Days);
			Console.ReadLine();
		}

		static async Task<string> requesting()
		{
			using (HttpClient client = new HttpClient())
			{
				var userAgentValues = new string[] { "7658493076-843567-45364356", "4578023498475832475-3245702-5" };
				client.DefaultRequestHeaders.Add("User-Agent", userAgentValues);

				//"gridId": "CLE",
				//    "gridX": 114,
				//    "gridY": 50,

				string getUrl = "https://api.weather.gov/gridpoints/CLE/114,50/forecast"; // https://api.weather.gov/points/41.1001,-80.8553
				HttpResponseMessage getResponse = await client.GetAsync(getUrl);

				string getResponseBody = await getResponse.Content.ReadAsStringAsync();
				return getResponseBody;
			}


		}
	}
}
