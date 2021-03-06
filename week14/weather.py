import json
from tkinter import *
import requests

api_key = '4344b0c5d63fb946ca403d0675a37478'
city_name = 'yangsan'
weather_url = 'https://api.openweathermap.org/data/2.5/weather?&q='+city_name+'&lang=kr&appid='+api_key
# https://api.openweathermap.org/data/2.5/weather?id=524901&lang=kr&appid=4344b0c5d63fb946ca403d0675a37478
print(weather_url)

response = requests.get(weather_url)
print(response)

weather_info = response.json()
print(type(weather_info))
print(weather_info)
print(json.dumps(weather_info,indent='\t'))

print(weather_info["weather"])
print(weather_info["weather"][0]["main"])
print(weather_info["weather"][0]["description"])
print(weather_info["sys"])
print(weather_info["sys"]["sunrise"])
print(weather_info["main"]["humidity"],'%')

print("-"*30)
print(weather_info["coord"]["lon"])
print(weather_info["coord"]["lat"])
print(weather_info["sys"]["country"])
print(weather_info["main"]["temp"])
print(weather_info["main"]["humidity"])
print(weather_info["wind"]["speed"])
print(weather_info["weather"][0]["icon"])
print(weather_info["name"])
print(weather_info["weather"][0]["description"])


win = Tk()

