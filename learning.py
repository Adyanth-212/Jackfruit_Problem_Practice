import tkinter
import csv
from tkinter import Toplevel, ttk, Label, Text, Scrollbar, Entry, messagebox
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

#Getting the user data in read mode
def get_user_data():
    with open("users.csv", 'r') as user_data:
        user_contents = csv.DictReader(user_data)
        return user_contents


#Function that basically stores all the booking data at once
def booking_data():
    with open("bookings.csv", 'r') as booking_data_as_file:
        booking_contents = csv.DictReader(booking_data_as_file)
        return booking_contents


# Function for  Opening the new window(For the searching bit)
def restaurant_list():
    file_contents = get_restaurants()

    newWindow = Toplevel(win)
    newWindow.title("Restaurant List")
    newWindow.geometry("400x300")
    newWindow.resizable(width=True, height=True)

    title_1 = tkinter.Label(newWindow, text="Restaurant List", font=("Times New Roman", 16))
    title_1.pack(pady=10)

    frame = tkinter.Frame(newWindow)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scrollbar = tkinter.Scrollbar(frame, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)

    restaurant_list_to_show = tkinter.Listbox(frame, yscrollcommand=scrollbar.set)
    restaurant_list_to_show.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar.config(command=restaurant_list_to_show.yview)

    for restaurant in file_contents:
        restaurant_list_to_show.insert(END, restaurant)

    #Function to add new Restaurants if needed
    def adding_restaraunt():
        restaurant_addition_window = Toplevel(newWindow)
        newWindow.destroy()
        """
        •	restaurant_id (unique identifier)
        •	name
        •	cuisine_type
        •	rating (out of 5)
        •	location
        •	total_tables
        •	table_configuration (e.g., 2-seater, 4-seater, etc.)
        •	opening_hours
        •	closing_hours
        """





    add_button = tkinter.Button(newWindow, text='Click Here to Add A restaurant', width = 200, command= adding_restaurants)

    def search_bar():
        search = Entry(restaurant_list, textvariable="Enter the Restaurant you wish to search")
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





    #Code to Open a page where we can ask the user if they wish to add the restuarant to the list

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

#Function for the login Page
def login_page(user_contents, booking_contents):
    login_page = Toplevel(win)
    login_page.title("User Information")
    login_page.geometry("400x300")
    login_page.resizable(width=True, height=True)
    Label(login_page, text="User ID").grid(row=0)
    Label(login_page, text="Email ID").grid(row=1)
    e1 = Entry(login_page)
    e2 = Entry(login_page)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    if e1 and e2 in user_contents:
        bookings_page = Toplevel(login_page)
        bookings_page.title('Bookings')
        bookings_page.resizable(height=True, width=False)
        scrollbar = Scrollbar(bookings_page)
        bookings_list = Listbox(login_page, yscrollcommand=scrollbar.set)
        for booking in booking_contents:
            bookings_list.insert(END, booking['Restaraunt Name'])
        bookings_list.pack()
    else:
        # Prompt the user to create an account
        response = messagebox.askyesno("Account Not Found", "User not found. Would you like to create an account?")
        if response:  # If the user agrees to create an account
            with open("users.csv", 'a', newline='') as user_data:
                writer = csv.writer(user_data)
                writer.writerow([e1.get(), e2.get()])
            messagebox.showinfo("Account Created", "Your account has been created successfully!")
        else:
            messagebox.showinfo("Cancelled", "Account creation cancelled.")



#Buttons for the main page
button_for_restaurant_display = tkinter.Button(win, text="Restaurant List", command=restaurant_list)
button_for_booking_selection = tkinter.Button(win, text="Booking a reservation", command=bookings)
button_for_logging_in = tkinter.Button(
    win, 
    text="Login", 
    command=lambda: login_page(user_contents, booking_contents)
)

#Packing Everything
button_for_restaurant_display.pack()
button_for_booking_selection.pack()
button_for_logging_in.pack()

win.mainloop()
