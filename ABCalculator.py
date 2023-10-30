import tkinter as tk

# Создание главного окна
root = tk.Tk()
root.title("A/B калькулятор")
root.geometry("280x300")

font_btn = ("Helvetica", 10, "bold")


# Функция закрытия программы
def do_close():
    root.destroy()


# Добавление метки заголовка
lbl_title = tk.Label(
    text="A/B калькулятор", font=("Helvetica", 16, "bold"), fg="#0000cc"
)
lbl_title.place(x=55, y=20)

# Добавление кнопки "Рассчитать"
btn_calculate = tk.Button(root, text="Рассчитать", font=font_btn)
btn_calculate.place(x=25, y=250, width=90, height=30)

# Добавление кнопки "Закрытия"
btn_close = tk.Button(root, text="Закрыть", font=font_btn, command=do_close)
btn_close.place(x=160, y=250, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()
