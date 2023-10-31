import tkinter as tk
from tkinter import messagebox as mb

# Создание главного окна
root = tk.Tk()
root.title("A/B калькулятор")
root.geometry("280x300")
root.resizable(False, False)

helvetica = ("Helvetica", 10, "bold")


# Функция закрытия программы
def do_close():
    root.destroy()


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
    window.geometry("280x300")
    window.title("A/B Результат")
    window.resizable(False, False)

    # Добавление кнопки закрытия окна
    btn_close_popup = tk.Button(
        window, text="Закрыть", font=helvetica, command=window.destroy
    )
    btn_close_popup.place(x=160, y=250, width=90, height=30)

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
ent_visitors_1.insert(tk.END, "0")

lbl_conversions_1 = tk.Label(text="Конверсии:", font=helvetica)
lbl_conversions_1.place(x=25, y=115)

ent_conversions_1 = tk.Entry(font=helvetica, justify="center")
ent_conversions_1.place(x=115, y=115, width=90, height=20)
ent_conversions_1.insert(tk.END, "0")


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
ent_visitors_2.insert(tk.END, "0")

lbl_conversions_2 = tk.Label(text="Конверсии:", font=helvetica)
lbl_conversions_2.place(x=25, y=205)

ent_conversions_2 = tk.Entry(font=helvetica, justify="center")
ent_conversions_2.place(x=115, y=205, width=90, height=20)
ent_conversions_2.insert(tk.END, "0")


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
