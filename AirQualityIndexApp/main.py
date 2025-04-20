import requests
import json
import pyttsx3

engine = pyttsx3.init()

city = input("Enter the name of city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1b5f37617eb5503f47979feac183bedc"

r = requests.get(url)
weather_dict = json.loads(r.text)
lon = weather_dict["coord"]["lon"]
lat = weather_dict["coord"]["lat"]

url2 = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid=1b5f37617eb5503f47979feac183bedc"

r2 = requests.get(url2)
aqi_dict = json.loads(r2.text)
aqi = aqi_dict["list"][0]["main"]["aqi"]

if aqi == 1:
    quality = "Good"
elif aqi == 2:
    quality = "Fair"
elif aqi == 3:
    quality = "Moderate"
elif aqi == 4:
    quality = "Poor"
elif aqi == 5:
    quality = "Very Poor"

engine.say(f"The air pollution condition in {city} is {quality} and it's air quality index of is {aqi}.")
engine.runAndWait()