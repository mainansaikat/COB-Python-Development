import requests
from bs4 import BeautifulSoup

# Enter city name
city = input("Please enter the city name:- ")

# Create the URL and send a GET request
url = f"https://www.google.com/search?q=weather+{city}"
html = requests.get(url).content

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Extract the weather information
temperature = soup.find('div', class_='BNeawe iBp4i AP7Wnd').get_text()
weather_info = soup.find('div', class_='BNeawe tAd8D AP7Wnd').get_text()

# Extract additional information
additional_info = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')

# Print the data
print("Temperature: " + temperature)
print(weather_info)
for info in additional_info:
    if 'Wind' in info.get_text():
        print(info.get_text())