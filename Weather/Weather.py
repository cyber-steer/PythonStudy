import json
import urllib.request
from tkinter import *
import requests
from datetime import datetime

iconBackgroudColor = "lightgray" # 아이콘 배경색
backgroudColor = 'white' # 윈도우 배경색
api_key = '4344b0c5d63fb946ca403d0675a37478'

def search():
    city_name = cityE.get()
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?&q='+city_name+'&lang=kr&appid='+api_key
    response = requests.get(weather_url)

    code = str(response)[11:14]
    if code == "200":
        weather_info = response.json()
        iconTmp = weather_info["weather"][0]["icon"]
        icon_url = "https://openweathermap.org/img/wn/"+iconTmp+"@2x.png"
        urllib.request.urlretrieve(icon_url, "tmp.png")

        now = datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")

        iconTmp = PhotoImage(file="tmp.png")
        lon = weather_info["coord"]["lon"]
        lat = weather_info["coord"]["lat"]
        country = weather_info["sys"]["country"]
        temp = str(round(int(weather_info["main"]["temp"])-273.15,1))+"도"
        humidity = str(weather_info["main"]["humidity"])+"%"
        speed = str(weather_info["wind"]["speed"])+"m/s"
        city = weather_info["name"]
        weather = weather_info["weather"][0]["description"]

        lonV.configure(text=str(lon))
        latV.configure(text=str(lat))
        countryV.configure(text=str(country))
        tempV.configure(text=str(temp))
        humidityV.configure(text=str(humidity))
        windSpeedV.configure(text=str(speed))
        cityV.configure(text=city)
        iconL.configure(image=iconTmp)
        iconL.image = iconTmp
        timeV.configure(text=now)
        weatherV.configure(text=str(weather))
    else:
        reset()
        weatherV.configure(text="잘못입력했습니다")
def reset():
    img = PhotoImage(file="icon.png")
    now = datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")

    cityE.delete(0,END)

    iconL.configure(image=img)
    iconL.image = img
    lonV.configure(text="")
    latV.configure(text="")
    countryV.configure(text="")
    tempV.configure(text="")
    humidityV.configure(text="")
    windSpeedV.configure(text="")
    cityV.configure(text="")
    timeV.configure(text=now)
    weatherV.configure(text="")



window = Tk()
window.title("Weather")
window.configure(background="white")
github = "https://github.com/cyber-steer"

icon = PhotoImage(file="icon.png")

cityE = Entry(window, background=backgroudColor)
searchB = Button(window, text="검색", command=search, background=backgroudColor)
resetB = Button(window, text="초기화", command=reset, background=backgroudColor)

lonL = Label(window, text="경도", background=backgroudColor)
lonV = Label(window, text="", background=backgroudColor)
latL = Label(window, text="위도", background=backgroudColor)
latV = Label(window, text="", background=backgroudColor)
iconL = Label(window,image=icon,background=iconBackgroudColor)
weatherL = Label(window, text="날씨", background=backgroudColor)
weatherV = Label(window, text="", background=backgroudColor)

countryL = Label(window, text="국가", background=backgroudColor)
countryV = Label(window, text="", background=backgroudColor)
cityL = Label(window, text="도시", background=backgroudColor)
cityV = Label(window, text="", background=backgroudColor)
tempL = Label(window, text="온도", background=backgroudColor)
tempV = Label(window, text="", background=backgroudColor)
humidityL = Label(window, text="습도", background=backgroudColor)
humidityV = Label(window, text="", background=backgroudColor)
windSpeedL = Label(window, text="풍속", background=backgroudColor)
windSpeedV = Label(window, text="", background=backgroudColor)

timeL = Label(window, text="현재시간", background=backgroudColor)
now = datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")
timeV = Label(window, text=now, background=backgroudColor)
userV = Label(window, text="장성익", background=backgroudColor)
githubL = Label(window, text=github, background=backgroudColor)

cityE.grid(row=0, column=0, columnspan=2)
searchB.grid(row=0, column=2)
resetB.grid(row=0, column=3)
latL.grid(row=1, column=0)
lonL.grid(row=1, column=1)
latV.grid(row=2, column=0)
lonV.grid(row=2, column=1)
weatherL.grid(row=3, column=0)
weatherV.grid(row=3, column=1)
iconL.grid(row=4,column=0,rowspan=2,columnspan=2)
countryL.grid(row=1, column=2)
countryV.grid(row=1, column=3)
cityL.grid(row=2, column=2)
cityV.grid(row=2, column=3)
tempL.grid(row=3, column=2)
tempV.grid(row=3, column=3)
humidityL.grid(row=4, column=2)
humidityV.grid(row=4, column=3)
windSpeedL.grid(row=5, column=2)
windSpeedV.grid(row=5, column=3)

timeL.grid(row=6,column=0)
timeV.grid(row=6,column=1)
userV.grid(row=7, column=0)
githubL.grid(row=7, column=1)

window.mainloop()