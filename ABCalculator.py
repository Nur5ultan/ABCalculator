import tkinter as tk

# Создание главного окна
root = tk.Tk()
root.title("A/B калькулятор")
root.geometry("280x300")

helvetica = ("Helvetica", 10, "bold")


# Функция закрытия программы
def do_close():
    root.destroy()


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

ent_visitors_1 = tk.Entry(font=helvetica)
ent_visitors_1.place(x=115, y=85, width=90, height=20)

lbl_conversions_1 = tk.Label(text="Конверсии:", font=helvetica)
lbl_conversions_1.place(x=25, y=115)

ent_conversions_1 = tk.Entry(font=helvetica)
ent_conversions_1.place(x=115, y=115, width=90, height=20)


# Добавление метки заголовка тестовой группы
lbl_subtitle_2 = tk.Label(
    text="Тестовая группа", font=("Helvetica", 12, "bold"), fg="#008800"
)
lbl_subtitle_2.place(x=25, y=145)

# Добавление полей ввода тестовой группы
lbl_visitors_2 = tk.Label(text="Посетители:", font=helvetica)
lbl_visitors_2.place(x=25, y=175)

ent_visitors_2 = tk.Entry(font=helvetica)
ent_visitors_2.place(x=115, y=175, width=90, height=20)

lbl_conversions_2 = tk.Label(text="Конверсии:", font=helvetica)
lbl_conversions_2.place(x=25, y=205)

ent_conversions_2 = tk.Entry(font=helvetica)
ent_conversions_2.place(x=115, y=205, width=90, height=20)


# Добавление кнопки "Рассчитать"
btn_calculate = tk.Button(root, text="Рассчитать", font=helvetica)
btn_calculate.place(x=25, y=250, width=90, height=30)

# Добавление кнопки "Закрытия"
btn_close = tk.Button(root, text="Закрыть", font=helvetica, command=do_close)
btn_close.place(x=160, y=250, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()
