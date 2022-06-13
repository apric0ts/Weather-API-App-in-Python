import requests
from datetime import datetime

API_KEY = "ea0548b9a7b28a55f6cc4ed5fce3a3bd"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#--------------------FUNCTIONS-----------------------------

#prints introduction of location
def printIntroduction():
    location = data["name"]
    country = data["sys"]["country"]
    now = datetime.now()
    currentTime = now.strftime("%A, %B %d, %Y\nTime: %H:%M:%S")
    print("Date:", currentTime)
    print(f"Location: {location}, {country}")
    

#prints sunrise/sunset
def sunRiseSet():
    sunrise = data["sys"]["sunrise"]
    sunrise = data["sys"]["sunset"]

#prints weather type
def printWeatherType():
    weather = data["weather"][0]["description"]
    print("Weather:",weather)

#prints temperature
def printTemperature():
    temperature = round(data["main"]["temp"], 2)
    print("Temperature:",temperature, "fahrenheit")

#prints humidity
def printHumidity():
    humidity = data["main"]["humidity"]
    if humidity>=75:
        print("Humidity: Very Humid")
    elif humidity>=50: 
        print("Humidity: Humid")
    else:
        print("Humidity: Not Humid")

#prints cloud status
def printIsCloudy():
    cloudy = data["clouds"]["all"]
    if cloudy>=80:
        print("Clouds: Dark Skies")
    elif cloudy>=50:
        print("Clouds: Cloudy")
    elif cloudy>=30:
        print("Clouds: Partly Cloudy")
    else:
        print("Clouds: No clouds in view")

#prints wind status
def printIsWindy():
    wind = data["wind"]["speed"]
    if fahrOrCelc == "c":
        print("Wind Speed:",wind," meters/second")
    elif fahrOrCelc == "f":
        print("Wind Speed:",wind," miles/hr")


#--------------------CODE-----------------------------

request_url = ""
#asks user for either city or zip code
cityOrZip = input("Do you want to locate by zip code or city? (zip/city): ")
#creates URL based on user
if cityOrZip=="zip":
    zip = input("Enter the zip code: ")
    with open("recents.txt","a") as file1:
        file1.write(zip)

    request_url = f"{BASE_URL}?appid={API_KEY}&q={zip}"
elif cityOrZip=="city":
    city = input("Enter a city name: ")
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    with open("recents.txt","a") as file1:
        file1.write(city)
else:
    print("An error has occurred")

#asks user for either fahrenheit or celcius
fahrOrCelc = input("Would you like the data in fahrenheit or celcius? (f/c): ")

if fahrOrCelc=="f":
    request_url += "&units=imperial"
elif fahrOrCelc =="c":
    request_url += "&units=metric"
else:
    print("An error has occurred")

#requests data
response = requests.get(request_url)

#if no errors, print what user wants
if response.status_code == 200:
    data = response.json()
    
    #printing weather analysis

    print("\n\n------------------------")
    printIntroduction()
    printWeatherType()
    printIsCloudy()
    printTemperature()
    printHumidity()
    printIsWindy()
    print("------------------------\n\n")

    with open("recents.txt","r") as file1:
        contents = file1.read()
        print(contents)
else:
    print("An error occurred.")




