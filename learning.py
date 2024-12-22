import tkinter
import csv
from tkinter import Toplevel, ttk, Label, Text, Scrollbar, Entry

win = tkinter.Tk(className="Restaurant Booking System")
win.title("Restaurant Booking System")
win.resizable(width=True, height=True)

title = tkinter.Label(win, text="Restaurant Booking System")
title.pack()


def get_restaurants():
    with open("restaurants.csv", 'r') as file_restaurants:
        file_contents = list(csv.DictReader(file_restaurants))
        return file_contents


# Function for  Opening the new window
def openNewWindow():
    file_contents = get_restaurants()

    # Create a new window
    newWindow = Toplevel(win)
    newWindow.title("Restaurant List")
    newWindow.geometry("400x300")
    newWindow.resizable(width=True, height=True)

    title_1 = tkinter.Label(newWindow, text="Restaurant List")
    title_1.pack()

    def search_bar():
        search = Entry(openNewWindow, textvariable="Enter the Restaurant you wish to search")
        if search in file_contents:

    def select(event):
        selected_item = combo_box.get()

        filtered = [restaurant for restaurant in file_contents if restaurant['Cuisine'] == selected_item]

        result_display.delete("1.0", tkinter.END)

        if filtered:
            for restaurant in filtered:
                result_display.insert(tkinter.END, f"{restaurant['Name']} - {restaurant['Address']}\n")
        else:
            result_display.insert(tkinter.END, "No restaurants found for the selected cuisine.\n")

    combo_box = ttk.Combobox(newWindow, values=["Indian", "Italian", "Turkish", "Ethiopian"])
    combo_box.bind("<<ComboboxSelected>>", select)
    combo_box.pack(pady=5)

    result_frame = tkinter.Frame(newWindow)
    result_frame.pack(fill=tkinter.BOTH, expand=True)

    scrollbar = Scrollbar(result_frame)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    result_display = Text(result_frame, wrap="word", yscrollcommand=scrollbar.set)
    result_display.pack(fill=tkinter.BOTH, expand=True)
    scrollbar.config(command=result_display.yview)


button_for_restaurant_display = tkinter.Button(win, text="Restaurant List", command=openNewWindow)
button_for_restaurant_display.pack()

win.mainloop()