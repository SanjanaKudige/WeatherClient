from flask import Flask
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

url = 'http://w1.weather.gov/xml/current_obs/index.xml'

source_code = requests.get(url)

soup = BeautifulSoup(source_code.content)

lati = input("\nEnter Latitude:")
longi = input("\nEnter Longitude:")

while True:
    station = soup.findAll("station")

    for stat in station:
        lati = stat.find('latitude').get_text()
        if eval(lati) == eval(lati):
            longi = stat.find('longitude').get_text()
            if eval(longi) == eval(longi):
                link = stat.find('xml_url').get_text()
    try:
        print(link)
        ans1 = requests.get(link)
        ans2 = BeautifulSoup(ans1.content)
        try:
            humidity = ans2.find("relative_humidity").get_text()
        except AttributeError:
            humidity = "-"
        try:
            temperature = ans2.find("temperature_string").get_text()
        except AttributeError:
            temperature = "-"
        try:
            dew_point = ans2.find("dewpoint_string").get_text()
        except AttributeError:
            dew_point = "-"
        try:
            pressure = ans2.find("pressure_string").get_text()
        except AttributeError:
            pressure = "-"
        try:
            wind = ans2.find("wind_string").get_text()
        except AttributeError:
            wind = "-"
        print('Humidity:', humidity,'\nTemperature:', temperature,'\nDew_Point:', dew_point,'\nPressure:', pressure,'\nWind:', wind)
    except NameError:

        print("Please Enter the Latitude and Longitude from the List Provided")
        break
        ans1.close()
    break
    # check = input("Enter yes if you want to refresh the details else Enter no:")
    # if check != "yes":
    #     ans1.close()
    #     break
