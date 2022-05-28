from cProfile import label
import json
from multiprocessing import Condition
from re import I, M, S
from sys import api_version
import tkinter as tk
from typing import final
import requests
import time


def getWeather(canvas):
    city = textfield.get()
    api = (
        "https://api.openweathermap.org/data/2.5/weather?q= "
        + city
        + " &appid=5520dc89c2d541c9153a18873eb8960d"
    )

    json_data = requests.get(api).json()
    Condition = json_data["weather"][0]["main"]
    temp = int(json_data["main"]["temp"] - 273.15)
    min_temp = int(json_data["main"]["temp_min"] - 273.15)
    max_temp = int(json_data["main"]["temp_max"] - 273.15)
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind = json_data["wind"]["speed"]
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data["sys"]["sunrise"] + 7200))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data["sys"]["sunset"] + 7200))

    final_info = Condition + "\n" + str(temp) + "°c"
    final_data = (
        "\n"
        + "max Temp: "
        + str(max_temp)
        + "\n"
        + "min Temp: "
        + str(min_temp)
        + "\n"
        + "pressure: "
        + str(pressure)
        + "\n"
        + "Humidity: "
        + str(humidity)
        + "\n"
        + "wind Speed: "
        + str(wind)
        + "\n"
        + "Sunrise: "
        + sunrise
        + "\n"
        + "Sunset: "
        + sunset
    )
    label1.config(text=final_info)
    label2.config(text=final_data)


Canvas = tk.Tk()
Canvas.geometry("720x579")
Canvas.title("Weather App | By Hashem")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(Canvas, justify="center", font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind("<Return>", getWeather)

label1 = tk.Label(Canvas, font=t)
label1.pack()
label2 = tk.Label(Canvas, font=f)
label2.pack()


Canvas.mainloop()
