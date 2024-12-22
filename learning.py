import tkinter
import csv
from tkinter import Toplevel, ttk, Label, Text, Scrollbar, Entry
from tkinter import *


#All the different classes i might need
class user:
    user_id = ""
    name = ""
    email = ""
    phone_number = ""
    current_bookings = ""
#Main Frontend Page
win = tkinter.Tk(className="Restaurants")
win.title("Restaurants")
win.resizable(width=True, height=True)

title = tkinter.Label(win, text="Restaurant Booking System")
title.pack()

#Handaling the data
def get_restaurants():
    with open("restaurants.csv", 'r') as file_restaurants:
        restaurant_contents = csv.DictReader(file_restaurants)
        return restaurant_contents
def get_user_data():
    with open("users.csv", 'r') as user_data:
        user_contents = csv.DictReader(user_data)
        return user_contents


# Function for  Opening the new window(For the searching bit
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
            print(file_contents[search])


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
# Function for opening the window for the booking thing
def bookings():
    bookings = Toplevel(win)
    bookings.title("Restaurant List")
    bookings.geometry("400x300")
    bookings.resizable(width=True, height=True)

    title_1 = tkinter.Label(bookings, text="Restaurant Booking System")
    title_1.pack()
    method_for_date_selection = Spinbox(bookings, from_=1, to=31)
    method_for_month_selection = Spinbox(bookings, from_=1, to=12)
    Label(bookings, text="Please enter the party number")
    method_for_party_size_input = Entry(bookings)
    #Put the table selection thing here ig




    #Packing everything inside this function
    method_for_date_selection.pack()
    method_for_month_selection.pack()
    method_for_party_size_input.pack()
def login_page(user_contents):
    login_page = Toplevel(win)
    login_page.title("User Information")
    login_page.geometry("400x300")
    login_page.resizable(width=True, height=True)
    Label(login_page, text="User ID").grid(row = 0)
    Label(login_page, text="Email ID").grid(row = 1)
    e1 = Entry(login_page)
    e2 = Entry(login_page)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    if e1 and e2 in user_contents:
        #Add a new page that opens here showing all the different bookings and all
    else:
        #Prompt the user to create an account of sorts

button_for_restaurant_display = tkinter.Button(win, text="Restaurant List", command=openNewWindow)
button_for_booking_selection = tkinter.Button(win, text="Booking a reservation", command=bookings)
button_for_logging_in = tkinter.Button(win, text="Login", command=login_page)


#Packing Everything
button_for_restaurant_display.pack()
button_for_booking_selection.pack()
button_for_logging_in.pack()

win.mainloop()