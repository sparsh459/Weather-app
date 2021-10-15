import tkinter as tk # for gui
import requests # for json file
import time # to format some variables

# defining a function to get data from the api
def getweather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=71c6872d17e86e62c2594277bf48f749"
    
    # calling json data from api by requests
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    # temp given in kelvin so to convert it into celcius and tehn we get a float value we use int typecast
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    # the below time is converted from seconds format to 12 hr format, if you want it for 24 hr %I = %H
    sunrise_time = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 19800))
    sunset_time =  time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] + 19800))
    
    # defining two strings to carry the data
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind_speed) + "\n" + "Sunrise: " + sunrise_time + "\n" + "Sunset: " + sunset_time
    
    # attaching these final_info and final_data to teh labels we ahve created
    label1.config(text = final_info)
    label2.config(text = final_data)

# defining GUI
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
# ico file for teh icon in this
canvas.wm_iconbitmap(bitmap =r"C:\Users\Sony\PycharmProjects\pythonProject\Frameworks of python\tkinter_prijects\weatherapp\icon_for.ico")


# defining fonts here to be used in GUI
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold") 

# defining text field here to get city name from the user
textfield = tk.Entry(canvas, justify='center', width = 20, font = t)
textfield.pack(pady = 20)
# focus.() - so when the user enter thsi applicateion tehy can write city name directly without moving cursor
textfield.focus()
# binding enter button to textfield so taht whenever enter is pressed it calls teh getweather function and displays the weather fo that city
textfield.bind('<Return>', getweather)

# creating labels to show the data
label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()