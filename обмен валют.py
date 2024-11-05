import requests
import json
from tkinter import *
from tkinter import messagebox as mb

def exchange():
    cod = entry.get ()

    if cod:
        try:
            respons = requests.get(https://open.er-api.com/v6/latest/USD)
            respons.raise_for_status()
            data =  respons.json()
            if cod in data ['rates']:
                exchange_rates = data ['rates'] [cod]
                mb.showinfo("Курс обмена", f"Курс {exchange_rates} {cod} за один доллар")
            else:
                mb.showerror("Ошибка", f"Валюта {cod} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты")




window = Tk()
window.title ("Курсы обмена валют")# заголовок
window.geometry ("360X80")

Label (text ="Введите код валюты").pack (padx = 10, pady = 10)

entry = Entry ()# поле ввода для чисел
entry.pack (padx = 10, pady = 10)

Button (text = 'Получить курс обмена к доллару', command=exchange).pack (padx = 10, pady = 10)

window.mainloop ()
