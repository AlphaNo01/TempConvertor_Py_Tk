#Created by: Revat Tailor
#Created on: 2024-11-15

from tkinter import *
from tkinter import ttk

# Basic setup
conv = Tk()
conv.geometry("800x800")
conv.title("Temperature Converter")
conv["bg"] = "light grey"

Title = Label(text="Temperature Converter", font=("Helvetica", 30), background="light grey")
Title.pack(anchor="center")

# Global variables for widgets
fent_temp = fahren_lbl = f_convert = celc = cent_temp = celc_lbl = c_convert = fahren = None

enter = Entry(width=20, borderwidth=4)
enter.pack()

# Hide function
def hide():
    global fent_temp, fahren_lbl, f_convert, celc, cent_temp, celc_lbl, c_convert, fahren
    for widget in [fent_temp, fahren_lbl, f_convert, celc, cent_temp, celc_lbl, c_convert, fahren]:
        if widget:
            widget.destroy()

# Converting functions
def converter():
    global fent_temp, fahren_lbl, f_convert, celc, cent_temp, celc_lbl, c_convert, fahren
    
    hide()  # Hide previous widgets
    enter_get = enter.get()
    if enter.get().strip() == "":
        result = "Please enter a value."
    else:
        if dropdown.get() == "Fahrenheit to Celsius":
            ok_btn.config(bg="light pink")

            try:
                fahrenheit = float(enter.get())
                celsius = (5/9) * (fahrenheit - 32)
                result = f"{round(celsius, 2)} °C"
            except ValueError:
                result = "Invalid input."

            #fahren_lbl = Label(text="°F", background="light green", font=("Helvetica", 20))
            #fahren_lbl.pack(anchor="center")

            #celc = Label(text=result, font=("Helvetica", 20))
            #celc.pack(anchor="center")

        elif dropdown.get() == "Celsius To Fahrenheit":
            ok_btn.config(bg="light blue")

            try:
                celsius = float(enter.get())
                fahrenheit = (9/5) * celsius + 32
                result = f"{round(fahrenheit, 2)} °F"
            except ValueError:
                result = "Invalid Input!"

        else:
            result = "Please select a option"
            #celc_lbl = Label(text="°C", background="light green", font=("Helvetica", 20))
            #celc_lbl.pack()

    fahren = Label(text=result, font=("Helvetica", 20))
    fahren.pack(anchor="center")

# Dropdown
dropdown = ttk.Combobox(conv, values=["Fahrenheit to Celsius", "Celsius To Fahrenheit"], state="readonly")
dropdown.pack(pady=10)
dropdown.set("Select")

# Convert button
ok_btn = Button(text="Convert", command=converter, width=20, height=2)
ok_btn.pack(pady=10)

conv.mainloop()