# Marvel API, tkinter, customtkinter ,public_key and private_key(imported from keys)
from marvel import Marvel
from keys import public_key, private_key
import tkinter
import customtkinter
from customtkinter import *

# API Objects
marvel = Marvel(PUBLIC_KEY=public_key, PRIVATE_KEY=private_key)
characters = marvel.characters
# tkinter/customtkinter Objects
window = CTk()
window.title("Random Idea")
window.eval('tk::PlaceWindow . center')
window.geometry("1350x300")


# Functions that uses the API
def character_search(name, limit):
    # Searches for characters whose names start with the given name and limits the results according to the
    # provided limit
    my_char = characters.all(nameStartsWith=name, limit=limit)["data"]["results"]
    result_label.configure(text=str(len(my_char)) + " Results")
    for char in my_char:

        result_listbox.insert(tkinter.END, str(char["id"]) + ": " + char["name"])

        if len(char["description"]) == 0:
            result_listbox.insert(tkinter.END, "-n/a")
        else:
            result_listbox.insert(tkinter.END, "-" + char["description"])


def character_comic_search(name, limit):
    # It searches the charactor to see if it's in the database.
    # If it exists it will get the comic book data and if not it will
    # Search for and character with the same name
    my_char = characters.all(name=name)["data"]["results"]
    x = 0
    if len(my_char) > 0:
        for char in my_char:
            x = char["id"]
            result_label.configure(text=str(len(my_char)) + "Results")
            comic_search(x, limit)
    else:
        my_char = characters.all(nameStartsWith=name, limit=limit)["data"]["results"]
        result_label.configure(text="0 Results, Do you mean these characters")
    for char in my_char:

        result_listbox.insert(tkinter.END, str(char["id"]) + ": " + char["name"])

        if len(char["description"]) == 0:
            result_listbox.insert(tkinter.END, "-n/a")
        else:
            result_listbox.insert(tkinter.END, "-" + char["description"])


def comic_search(id, limit):
    # Searches for comics related to a character
    my_char = characters.comics(id, limit=limit)["data"]["results"]
    for char in my_char:

        result_listbox.insert(tkinter.END, "." + char['title'])

        if len(char["description"]) == 0:
            result_listbox.insert(tkinter.END, "-n/a")
        else:
            result_listbox.insert(tkinter.END, "-" + char["description"])

# Function for the button
def btn_action():
    # The click event with the search btn.
    # Checks if there's a public key or private and if the fields are filled
    if len(public_key) != 0 and len(private_key) != 0:

        if result_listbox.size() > 0:
            result_listbox.delete(0, tkinter.END)
        if select_menu.get() == "Comic" and limit_menu.get() != "-limit-" and len(textbox.get("1.0", "end-1c")) != 0:
            character_comic_search(textbox.get("1.0", "end-1c"), limit_menu.get())
        elif select_menu.get() == "Character" and limit_menu.get() != "-limit-" and len(
                textbox.get("1.0", "end-1c")) != 0:
            character_search(textbox.get("1.0", "end-1c"), limit_menu.get())
        else:
            print("error")

# Main Body
if __name__ == '__main__':
    # Setting the string for the dropbox
    select = customtkinter.StringVar()
    limit = customtkinter.StringVar()
    select.set("-select-")
    limit.set("-limit-")
    option_limit = ['5', '10', '15', '20', '25', '50', '55', '65', '70', '75', '80', '85', '90', '95', '100']

    # Widgets
    set_appearance_mode("Dark")
    textbox = CTkTextbox(window, width=320, height=20, font=('consolas', 20))
    select_menu = CTkOptionMenu(window, variable=select, values=["Character", "Comic"], width=35, height=39)
    select_menu.configure(font=('consolas', 15))
    limit_menu = CTkOptionMenu(window, variable=limit, values=option_limit, width=40, height=39)
    search = CTkButton(window, text="Search", font=('consolas', 25), width=35, height=30, command=btn_action)
    result_label = CTkLabel(window, text="Results", font=('consolas', 25))
    result_listbox = tkinter.Listbox(window, bg="#262626", fg="white", width=100, height=6, font=('consolas', 13))

    # Grid
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    window.columnconfigure(3, weight=1)
    window.columnconfigure(4, weight=1)
    window.columnconfigure(5, weight=1)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)
    select_menu.grid(row=0, column=0, padx=10)
    textbox.grid(row=0, column=2)
    limit_menu.grid(row=0, column=4)
    search.grid(row=0, column=5)
    result_label.grid(row=1, column=2)
    result_listbox.grid(row=2, column=2)
    window.mainloop()

    # 1011347 Spider-Ham (Larval Earth)
