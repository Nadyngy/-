import requests
import json
from tkinter import *
from tkinter import messagebox as mb

def exchange()

window = Tk()
window.title ("Курсы обмена валют")# заголовок
window.geometry ("360X80")

Label (text ="Введите код валюты").pack (padx = 10, pady = 10)

entry = Entry ()# поле ввода для чисел
entry.pack (padx = 10, pady = 10)

Button (text = 'Получить курс обмена к доллару', command=exchange).pack (padx = 10, pady = 10)

window.mainloop ()
