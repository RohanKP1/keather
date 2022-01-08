import requests
from bs4 import BeautifulSoup
from tkinter import Button, Entry, Label, PhotoImage, StringVar
from tkinter import Tk
from PIL import ImageTk,Image
from datetime import datetime
import os.path

def main():

    now = datetime.now()
    current_time = now.strftime("%H")
    open_url=open("assets/url.txt","r")
    url=open_url.read()
    master=Tk()
    master.title("Keather")
    master.config(bg="#202020")
    master.resizable(0,0)
    master.wait_visibility(master)
    master.wm_attributes('-alpha',0.95)
    img=Image.open("assets/keather.png")
    img=ImageTk.PhotoImage(img)
    master.iconphoto(False,img)

    def getweather():
        page=requests.get(url)
        soup=BeautifulSoup(page.content, "html.parser")

        full_location=soup.find("h1", class_="CurrentConditions--location--kyTeL").text.split(",")
        location=f"{full_location[0]}\n"
        locationlabel.config(text=location)

        temperature=soup.find("span",class_="CurrentConditions--tempValue--3a50n").text
        temperaturelabel.config(text=temperature+"C")

        condition=soup.find("div",class_="CurrentConditions--phraseValue--2Z18W").text
        weatcondlabel.config(text="\n"+condition)
    
        temperaturelabel.after(60000,getweather)
        master.update()

        return condition

    Label(master,text="",bg="#202020").grid(row=0,columnspan=2)

    locationlabel= Label(master,font=("Google sans",12),bg="#202020",fg="white")
    locationlabel.grid(row=1,columnspan=2,sticky="W",padx=30)

    temperaturelabel= Label(master,font=("Google sans bold",50),bg="#202020",fg="white")
    temperaturelabel.grid(row=2,column=0,sticky="W",padx=30)

    weatcondlabel= Label(master,font=("Google sans",15),bg="#202020",fg="white")
    weatcondlabel.grid(row=3,column=1,sticky="S",padx=25)

    getweather()

    if getweather() == "Clear" and (19 < int(current_time) or 5 > int(current_time)):
        assets=Image.open("assets/weather-clear-night-symbolic.png")

    elif getweather() == "Clear":
        assets=Image.open("assets/weather-clear-symbolic.png")

    elif getweather() == "Clear" and (19 < int(current_time) or 5 > int(current_time)):
        assets=Image.open("assets/weather-clear-night-symbolic.png")

    elif getweather() == "Partly Cloudy" and (19 < int(current_time) or 5 > int(current_time)):
        assets=Image.open("assets/weather-clear-night-symbolic.png")

    elif getweather() == "Partly Cloudy":
        assets=Image.open("assets/weather-few-clouds-symbolic.png")

    elif getweather()== "Fog":
        assets=Image.open("assets/weather-fog-symbolic.png")

    elif getweather()== "Sunny":
        assets=Image.open("assets/weather-clear-symbolic.png")

    elif getweather()== "Mostly Cloudy" and (19 < int(current_time) or 5 > int(current_time)):
        assets=Image.open("assets/weather-clouds-night-symbolic.png")
        
    elif getweather()== "Mostly Cloudy":
        assets=Image.open("assets/weather-clouds-symbolic.png")

    elif getweather()== "Haze":
        assets=Image.open("assets/weather-fog-symbolic.png")

    elif getweather()== "Smoke":
        assets=Image.open("assets/weather-fog-symbolic.png")

    elif getweather()== "Light Rain":
        assets=Image.open("assets/weather-showers-scattered-symbolic.png")

    elif getweather()== "Rain" or "Rain Shower":
        assets=Image.open("assets/weather-showers-symbolic.png")

    elif getweather()== "Heavy Rain":
        assets=Image.open("assets/weather-storm-symbolic.png")

    elif getweather()== "Fair":
        assets=Image.open("assets/weather-clouds-symbolic.png")
        
    elif getweather()== "Light Rain Shower":
    	assets=Image.open("assets/weather-showers-scattered-symbolic.png")

    else:    
        assets=Image.open("assets/weather-none-available-symbolic.png")

    assets.resize((1,1))
    assets=ImageTk.PhotoImage(assets)
    assetsLabel= Label(master,image=assets,bg="#202020").grid(row=2,column=1,padx=25)

    Label(master,text="",bg="#202020").grid(row=4,columnspan=2,padx=180)

    master.mainloop()


def location():

    senior=Tk()
    senior.title("Keather")
    senior.config(bg="#202020")
    senior.resizable(0,0)
    img=Image.open("assets/keather.png")
    img=ImageTk.PhotoImage(img)
    senior.iconphoto(False,img)
    senior.wait_visibility(senior)
    senior.wm_attributes('-alpha',0.95)

    Label(senior,font=("Google sans",12),text="\nKeather (Powered by weather.com)",bg="#202020",fg="white").grid(row=0,columnspan=2,sticky="N",padx=25)
    Label(senior,font=("Google sans",10),text="\nGo to 'weather.com' and search your location and paste 'the URL' under :",bg="#202020",fg="white").grid(row=1,columnspan=2,sticky="N",padx=25)
    Label(senior,bg="#202020").grid(row=2,columnspan=2)
    url_var=StringVar()
    Entry(senior,textvariable=url_var,background="#272727",foreground="white",font=("Google sans",10)).grid(row=3,columnspan=2,sticky="nsew",padx=25)
    def permanent_url():
        url=url_var.get()
        save_url=open("assets/url.txt","w")
        save_url.write(url)    
    Label(senior,bg="#202020").grid(row=6,columnspan=2)
    Button(senior,text="Submit",bg="#272727",fg="white",activebackground="#202020",activeforeground="white",font=("Google sans",10),command=lambda:[permanent_url(),senior.destroy(),main()]).grid(row=7,columnspan=2)
    Label(senior,bg="#202020").grid(row=8,columnspan=2)

    senior.mainloop()

if os.path.exists("assets/url.txt") == False:
    check=open("assets/url.txt","x")
    check=open("assets/url.txt","r")
else:
    check=open("assets/url.txt","r")

if check.read()!="":
    main()
else:
    location()    

