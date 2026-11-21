import tkinter as tk
from tkinter import messagebox


def convert():
    text = input_box.get()
    if not text or any(digit not in '01234567' for digit in text):
        messagebox.showwarning('Warning', 'Please enter a valid octal number (0-7).')
        return

    decimal = int(text, 8)
    binary = bin(decimal)[2:]
    output_var.set(binary)


def clear():
    input_box.delete(0, tk.END)
    output_var.set('')


window = tk.Tk()
window.title('Automata - Octal to Binary')
window.geometry('540x350')
window.configure(bg='#f2f4f8')
window.resizable(False, False)

tk.Label(window, text='Octal to Binary Converter', font=('Arial', 20, 'bold'),
         bg='#f2f4f8', fg='#263445').pack(pady=(27, 4))
tk.Label(window, text='Program 4  |  Automata Programming',
         font=('Arial', 10), bg='#f2f4f8', fg='#667085').pack()

tk.Label(window, text='Enter an octal number', font=('Arial', 11, 'bold'),
         bg='#f2f4f8').pack(pady=(25, 6))
input_box = tk.Entry(window, width=35, font=('Arial', 13),
                     relief='solid', bd=1, justify='center')
input_box.pack(ipady=8)

buttons = tk.Frame(window, bg='#f2f4f8')
buttons.pack(pady=18)
tk.Button(buttons, text='Convert', command=convert,
          bg='#4169ad', fg='white', font=('Arial', 10, 'bold'),
          padx=18, pady=7).pack(side='left', padx=6)
tk.Button(buttons, text='Clear', command=clear,
          font=('Arial', 10), padx=18, pady=7).pack(side='left', padx=6)

tk.Label(window, text='Binary Output', font=('Arial', 11, 'bold'),
         bg='#f2f4f8').pack(pady=(0, 6))
output_var = tk.StringVar()
output_box = tk.Entry(window, width=40, font=('Arial', 13),
                      textvariable=output_var, justify='center',
                      state='readonly', readonlybackground='white',
                      relief='solid', bd=1)
output_box.pack(ipady=8)

window.mainloop()
