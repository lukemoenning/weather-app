from cProfile import label
from tkinter import *
import tkinter as tk
import requests
from PIL import Image, ImageTk

#config stores the client side api key information
import config
        


#setup the window and canvas
win = Tk()
win.title("Weather App")
win.geometry('800x600+300+150')
win.config(bg="#87ceeb")
win.resizable(False,False)

canvas = Canvas(win, width="800", height="600", bg="#87ceeb")
canvas.pack()


#creates the searchbox
canvas.create_oval(150,25,650,75,fill="white")


#creates the textfield
textfield = Entry(
    win,
    justify="center",
    cursor="arrow",
    width=28,
    font=("Times New Roman", 24, "italic"),
    bg="white",
    fg="#87ceeb",
    bd=0,
    highlightthickness=0
)
textfield.place(x=225,y=34)
textfield.focus()


#creates the central label
central_label = Label(
    win, 
    text= "Search a city to see the weather.", 
    font= ("Times New Roman", 48, "italic"), 
    fg= "white", 
    bg= "#87ceeb"
)
central_label.place(relx=0.5, rely=0.5, anchor=CENTER)


# retrieves weather data from openweathermap.org
def getWeather():
    try:
        city_name = textfield.get()
        
        #api key
        api = (
            "https://api.openweathermap.org/data/2.5/weather?q="
            + city_name
            + "&appid=" +config.api_key
        )
        
        #requests weather data
        json_data = requests.get(api).json()
        description = json_data["weather"][0]["main"]
        humidity = json_data["main"]["humidity"]
        temperature = int(json_data["main"]["temp"] - 273.15)
        wind = json_data["wind"]["speed"]
        wind_degree = json_data["wind"]["deg"]

        
        #converts temperature to fahrenheit and rounds to nearest tenth
        temperature = temperature*(9/5) +32
        temperature = round(temperature, 1)
        
        #rounds humidity to nearest tenth
        humidity = round(humidity, 1)
        
        #converts wind degree to a cardinal direction and rounds to nearest tenth
        cardinal_directions = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N"]
        wind_direction = cardinal_directions[int(wind_degree%22.5)]
        wind = round(wind, 1)
        
        #creates the temperature label
        temperature_label = Label(
            win, 
            text= "TEMP",
            font= ("Times New Roman", 30, "bold"),
            fg= "black",
            bg= "#87ceeb"
        )
        temperature_label.place(relx=0.25, rely=0.75, anchor=CENTER)
    
        #displays the temperature
        retrieved_temperature_label = Label(
            win, 
            text= (str(temperature)+"°F"),
            font= ("Times New Roman", 30, "italic"),
            fg= "white",
            bg= "#87ceeb"
        )
        retrieved_temperature_label.place(relx=0.25, rely=0.82, anchor=CENTER)



        #creates the humidity label
        humidity_label = Label(
            win,
            text= "HUMIDITY",
            font= ("Times New Roman", 30, "bold"),
            fg= "black",
            bg= "#87ceeb"
    )
        humidity_label.place(relx=0.5, rely=0.75, anchor=CENTER)
    
        #displays the humidity
        retrieved_humidity_label = Label(
            win, 
            text= (str(humidity)+"%"),
            font= ("Times New Roman", 30, "italic"),
            fg= "white",
            bg= "#87ceeb"
        )
        retrieved_humidity_label.place(relx=0.5, rely=0.82, anchor=CENTER)



        #creates the wind label
        wind_label = Label(
            win,
            text= "WIND",
            font= ("Times New Roman", 30, "bold"),
            fg= "black",
            bg= "#87ceeb"
        )
        wind_label.place(relx=0.75, rely=0.75, anchor=CENTER)
    
        #displays the wind
        retrieved_wind_label = Label(
            win,
            text= str(wind)+" mph "+wind_direction,
            font= ("Times New Roman", 30, "italic"),
            fg= "white",
            bg= "#87ceeb"
        )
        retrieved_wind_label.place(relx=0.75, rely=0.82, anchor=CENTER)
        
        
        #removes all whitespaces from descpription to match file names
        
        """"
        match (description):
            
            #thunderstorm cases
            case "thunderstorm with light rain":
                description = "thunderstorm"
            case "thunderstorm with rain":
                description = "thunderstorm"
            case "thunderstorm with heavy rain":
                description = "thunderstorm"
            case "light thunderstorm":
                description = "thunderstorm"
            case "thunderstorm":
                description = "thunderstorm"
            case "heavy thunderstorm":
                description = "thunderstorm"
            case "ragged thunderstorm":
                description = "thunderstorm"
            case "thunderstorm with light drizzle":
                description = "thunderstorm"
            case "thunderstorm with drizzle":
                description = "thunderstorm"
            case "thunderstorm with heavy drizzle":
                description = "thunderstorm"
        """
        
        
        
        description = description.replace(" ","")
        print(description)
        image_path = "images/"+description+".gif"
                
                
        #displays the correct weather icon
        central_label.place_forget()
        img = Image.open(image_path)
        img_resized = img.resize((250,250))
        weather_icon = ImageTk.PhotoImage(img_resized)
        icon_label = Label(win, image=weather_icon)
        icon_label.image = weather_icon
        icon_label.config(bg = "#87ceeb")
        icon_label.place(relx=0.5, rely=0.45, anchor=CENTER)

                    
    except Exception as e:
        central_label.config(text="invalid input")
    

#creates the search button
search_button = Button(
    win,
    text="search",
    command= (lambda: getWeather()),
    justify="center",
    font= ("Times New Roman", 24, "italic"), 
    fg= "white", 
    highlightbackground="#87ceeb",
    bd=0,
    highlightthickness=0
)
search_button.place(x=670,y=34)



win.mainloop()