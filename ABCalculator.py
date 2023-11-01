import tkinter as tk
from tkinter import messagebox as mb
import os
import math

# Создание главного окна
root = tk.Tk()
root.title("A/B калькулятор")
root.geometry("280x300")
root.resizable(False, False)

helvetica = ("Helvetica", 10, "bold")


# Функция закрытия программы
def do_close():
    root.destroy()


# Функция форматирования процентов
def num_percent(num):
    return "{:.2f}".format(num * 100).rjust(10) + "%"


def do_proccessing():
    # Считывание данных из полей вводе
    n1 = int(ent_visitors_1.get())
    c1 = int(ent_conversions_1.get())
    n2 = int(ent_visitors_2.get())
    c2 = int(ent_conversions_2.get())

    # Проверка данных из полей ввода
    if n1 <= 0 or n2 <= 0:
        mb.showerror(title="Ошибка", message="Неверное количество посетителей")
        return

    # Открытия окна результатов
    popup_window(n1, c1, n2, c2)


# Функция вызова окна результатов
def popup_window(n1, c1, n2, c2):
    window = tk.Toplevel()
    window.geometry("500x500")
    window.title("A/B Результат")
    window.resizable(False, False)

    # Добавление окна вывода текста
    txt_output = tk.Text(window, font=("Courier New", 10, "bold"))
    txt_output.place(x=15, y=115, width=470, height=300)

    txt_output.insert(
        tk.END, "                              Контрольная     Тестовая" + os.linesep
    )
    txt_output.insert(
        tk.END, "                               группа          группа" + os.linesep
    )
    txt_output.insert(
        tk.END,
        "----------------------------------------------------------" + os.linesep,
    )

    # Добавление вывода конверсии и стандартного отклонения
    p1 = c1 / n1
    p2 = c2 / n2
    txt_output.insert(
        tk.END,
        "Конверсия                   "
        + num_percent(p1)
        + "    "
        + num_percent(p2)
        + os.linesep,
    )

    sigma_1 = math.sqrt(p1 * (1 - p1) / n1)
    sigma_2 = math.sqrt(p2 * (1 - p2) / n2)
    txt_output.insert(
        tk.END,
        "Стандартный отклонение     "
        + num_percent(sigma_1)
        + "     "
        + num_percent(sigma_2)
        + os.linesep,
    )
    txt_output.insert(
        tk.END,
        "----------------------------------------------------------" + os.linesep,
    )

    # Добавление кнопки закрытия окна
    btn_close_popup = tk.Button(
        window, text="Закрыть", font=helvetica, command=window.destroy
    )
    btn_close_popup.place(x=190, y=450, width=90, height=30)

    # Перевод фокуса на созданное окно
    window.focus_force()


# Добавление метки заголовка
lbl_title = tk.Label(
    text="A/B калькулятор", font=("Helvetica", 16, "bold"), fg="#0000cc"
)
lbl_title.place(x=55, y=20)


# Добавление метки заголовка контрольной группы
lbl_subtitle = tk.Label(
    text="Контрольная группа", font=("Helvetica", 12, "bold"), fg="#0066ff"
)
lbl_subtitle.place(x=25, y=55)

# Добавление полей ввода контрольной группы
lbl_visitors_1 = tk.Label(text="Посетители:", font=helvetica)
lbl_visitors_1.place(x=25, y=85)

ent_visitors_1 = tk.Entry(font=helvetica, justify="center")
ent_visitors_1.place(x=115, y=85, width=90, height=20)
ent_visitors_1.insert(tk.END, "255")

lbl_conversions_1 = tk.Label(text="Конверсии:", font=helvetica)
lbl_conversions_1.place(x=25, y=115)

ent_conversions_1 = tk.Entry(font=helvetica, justify="center")
ent_conversions_1.place(x=115, y=115, width=90, height=20)
ent_conversions_1.insert(tk.END, "26")


# Добавление метки заголовка тестовой группы
lbl_subtitle_2 = tk.Label(
    text="Тестовая группа", font=("Helvetica", 12, "bold"), fg="#008800"
)
lbl_subtitle_2.place(x=25, y=145)

# Добавление полей ввода тестовой группы
lbl_visitors_2 = tk.Label(text="Посетители:", font=helvetica)
lbl_visitors_2.place(x=25, y=175)

ent_visitors_2 = tk.Entry(font=helvetica, justify="center")
ent_visitors_2.place(x=115, y=175, width=90, height=20)
ent_visitors_2.insert(tk.END, "235")

lbl_conversions_2 = tk.Label(text="Конверсии:", font=helvetica)
lbl_conversions_2.place(x=25, y=205)

ent_conversions_2 = tk.Entry(font=helvetica, justify="center")
ent_conversions_2.place(x=115, y=205, width=90, height=20)
ent_conversions_2.insert(tk.END, "18")


# Добавление кнопки "Рассчитать"
btn_calculate = tk.Button(
    root, text="Рассчитать", font=helvetica, command=do_proccessing
)
btn_calculate.place(x=25, y=250, width=90, height=30)

# Добавление кнопки "Закрытия"
btn_close = tk.Button(root, text="Закрыть", font=helvetica, command=do_close)
btn_close.place(x=160, y=250, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()
