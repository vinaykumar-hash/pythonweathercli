import requests
import json
from os import system, name
import datetime
import time
API_KEY = "f8ab625482b231795aa326ac377aaa6a"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
AOD = False
a = 0
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def weathershow(city):
    global a
    c_url = base_url + "appid=" + API_KEY + "&q=" + city
    response = requests.get(c_url)
    x = response.json()
    if x["cod"]!="404":
        clear()
        print(x["name"],",",x["sys"]["country"])
        print("Temperature : "+str(round(x["main"]["temp"]-273.17))+chr(176),end="")
        print(" ~ "+str(round(x["main"]["feels_like"]-273.17))+chr(176))
        print(x["weather"][0]["main"],"-",x["weather"][0]["description"],"\n")
        print("WIND"+"-"*6)
        print("  speed : "+str(round(x["wind"]["speed"])),"Km/h")
        print("\n"+"-"*10)
        print("Pressure : "+str(round(x["main"]["pressure"])),"mb")
        print("Humidity : "+str(round(x["main"]["humidity"])),"%")
        print("-"*10)
        print("Sunrise : "+str(datetime.datetime.utcfromtimestamp(x["sys"]["sunrise"]+ 5 * 3600 + 30 * 60)))
        print("Sunset : "+str(datetime.datetime.utcfromtimestamp(x["sys"]["sunset"]+ 5 * 3600 + 30 * 60)))
        # datetime.datetime.utcfromtimestamp(x["sys"]["sunrise"])
        a+=1
        print(f"[UPDATED] : {a}")
        if not AOD:
            user()
    else:
        print("[NOT FOUND]")
        user()
def user():
    global AOD
    print(f"\n\n[AOD] : {AOD}")
    userr = input("[*]-> : ")
    if userr=="AOD" or userr=="aod":
        AOD= not AOD
        user()
    else:
        weathershow(userr)
        if AOD:
            while AOD:
                time.sleep(3)
                weathershow(userr)
print("\n\n[USAGE] : Enter City or aod/AOD to refresh data every 3sec ")
user()