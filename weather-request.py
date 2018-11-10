import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=41.82387&lon=-71.4119899")

soup = BeautifulSoup(page.content, 'html.parser')

detailed = soup.find(id="detailed-forecast-body")
detailed_forecast = detailed.find_all(class_ = "row row-odd row-forecast")

forecasts = []

for forecast in detailed_forecast:
    forecasts.append(
        forecast.find(class_ = "forecast-label").get_text()
        + ": " + forecast.find(class_ = "forecast-text").get_text())

print(" 7 Day Forecast ")
print("----------------") 
for text_forecast in forecasts:
    print(text_forecast)