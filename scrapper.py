import requests
from tkinter import *
import tkinter as tk
from bs4 import BeautifulSoup
import customtkinter


#url_to_parse = input("Enter a url: ")
#response = requests.get(url_to_parse)
#print(response.text)
#"1.0","end-1c"

#To parse the data
def scrapeData():
	parse_text.set("Parsing ...")
	url = textBox.get() #Get the url from the textbox
	response = requests.get(url)
	#print(response.text)
	#response = response.text
	soup = BeautifulSoup(response.text, "lxml")
	response = soup.find(variable.get())
	print("------------------------")
	print(response)
	print("-------------------------")
	
	#text box
	if response:

		text_box = Text(root, height=10, width=50, padx=15, pady=15)
		text_box.insert(1.0, response)
		text_box.pack()
		#print(requests.get(url))
		parse_text.set("Parse")
	
	else:
		print("Failed to fetch data")
		parse_text.set("Failed")



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Web Scraper")
canvas = customtkinter.CTkCanvas(master=root, width=600, height=300)


#Label
title_label = customtkinter.CTkLabel(master=root, text="Welcome to my Web Scraper", font=('Roboto',25))
#label.pack()
#title_abel.grid(column=1, row=0)

#Instructions
instructions = customtkinter.CTkLabel(master=root, text="Please enter a website url to parse and choose a element", font=('Roboto',15,'bold'))
#instructions.grid(columnspan=3, column=0, row=1)


#Text Box
textBox = customtkinter.CTkEntry(master=root, width=200,height=1,font=('Roboto',10,'bold'),border_width=2, placeholder_text="ex: https://youtube.com")
#textBox.grid(column=1, row=2)

#Drop Down Menu
OPTIONS = ["h1","h2","title","p","span","li","div"]
variable = StringVar(root)
variable.set(OPTIONS[0])

dropDownMenu = OptionMenu(root, variable, *OPTIONS)
dropDownMenu.place(x=180, y=200)

#Parse Button
parse_text = tk.StringVar()
parseButton = customtkinter.CTkButton(master=root,textvariable=parse_text, width=4, font=('Roboto',10,'bold'),command=scrapeData)
parse_text.set("Parse")
#parseButton.grid(column=1, row=3)

canvas = customtkinter.CTkCanvas(master=root, width=600, height=200)
#canvas.grid(columnspan=3)


title_label.pack(pady=20)
instructions.pack(pady=20)
textBox.pack(pady=20)
parseButton.pack(pady=40)



#Load the Window
root.mainloop()




    