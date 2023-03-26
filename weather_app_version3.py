import tkinter as tk
import requests
import time
# my weather function
def getWeather(canvas):
    
    city = textField.get()
    #API
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f" + "&units=metric"
    # All  info about the place 
    json_data = requests.get(api).json()
    print(json_data)
    return_code = int(json_data['cod'])
    location_value = textField.get()  
    lbl_loc.config(text = location_value)     
    if return_code == 200:
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'])
        icon = json_data['weather'][0]['icon']
        minimum_temp = int(json_data['main']['temp_min'])
        maximum_temp = int(json_data['main']['temp_max'])
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        #final data
        final_info = condition + "\n" + str(temp) + "°C"
        final_data = "\n"+ "Min Temp: " + str(minimum_temp) + "°C" + "\n" + "Max Temp: " + str(maximum_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) 
        label1.config(text = final_info, font = big)
        label2.config(text = final_data, font = medium, pady = 10,)
        #city not found function
    elif return_code == 404:
        label1.config(text = 'City not found')
        label2.config(text = " ")
    textField.delete(0, tk.END)


    
# setting my canvas
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
#font sizes
small = ("poppins", 15, "bold")
big = ("poppins", 35, "bold")
medium = ("poppins", 25, "bold")
#header
lbl_title = tk.Label(canvas, text = 'Weather App', font = big)
lbl_name = tk.Label(canvas, text = '- Mit Patel Class 7', font = medium)
lbl_title.pack()
lbl_name.pack()

#textbox
textField = tk.Entry(canvas,justify='center', width = 20, font = big, bg = 'light blue' , fg = 'black')
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)


# Location name
lbl_loc= tk.Label(canvas, font = big)
lbl_loc.pack()
# the weather info font sizes and label
label1 = tk.Label(canvas, font=big, fg = 'blue' )
label1.pack()
label2 = tk.Label(canvas, font=small, fg = 'red')
label2.pack()

canvas.mainloop()

