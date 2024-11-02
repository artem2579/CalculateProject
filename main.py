from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_base_label(event):
    # Получаем полное название базовой валюты из словаря и обновляем метку
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)

def update_base2_label(event):
    # Получаем полное название второй базовой валюты из словаря и обновляем метку
    code = base2_combobox.get()
    name = currencies[code]
    base2_label.config(text=name)

def update_target_label(event):
    # Получаем полное название целевой валюты из словаря и обновляем метку
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)

def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()
    base2_code = base2_combobox.get()

    if target_code and base_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()

            data = response.json()

            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base = currencies[base_code]
                base2 = currencies[base2_code]
                target = currencies[target_code]
                mb.showinfo("Курс обмена", f"Курс {exchange_rate:.1f} {target} за 1 {base} , {exchange_rate:.1f} {target} за 1 {base2}")
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")

# Словарь кодов валют и их полных названий
currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("360x360")

Label(text="Базовая валюта:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_base_label)

base_label = ttk.Label()
base_label.pack(padx=10, pady=10)

Label(text="Вторая базовая валюта:").pack(padx=10, pady=5)
base2_combobox = ttk.Combobox(values=list(currencies.keys()))
base2_combobox.pack(padx=10, pady=5)
base2_combobox.bind("<<ComboboxSelected>>", update_base2_label)

base2_label = ttk.Label()
base2_label.pack(padx=10, pady=10)

Label(text="Целевая валюта:").pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_target_label)

target_label = ttk.Label()
target_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()

