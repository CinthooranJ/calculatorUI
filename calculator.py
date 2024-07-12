import tkinter as tk

def make_display_read_only(text_widget):
    text_widget.config(state='normal')
    text_widget.insert(tk.END, "")  # Initial text
    text_widget.config(state='disabled')

def number_btn_click(number):
    return

window = tk.Tk()
window.title("Calculator")
window.geometry('350x480')

#Numbers
one = tk.Button(window, text='1', width = 6, height = 3, command = lambda: number_btn_click(1)).place(x = 20, y = 340)
two = tk.Button(window, text='2', width = 6, height = 3, command = lambda: number_btn_click(2)).place(x = 80, y = 340)
three = tk.Button(window, text='3', width = 6, height = 3, command = lambda: number_btn_click(3)).place(x = 140, y = 340)
four = tk.Button(window, text='4', width = 6, height = 3, command = lambda: number_btn_click(4)).place(x = 20, y = 280)
five = tk.Button(window, text='5', width = 6, height = 3, command = lambda: number_btn_click(5)).place(x = 80, y = 280)
six = tk.Button(window, text='6', width = 6, height = 3, command = lambda: number_btn_click(6)).place(x = 140, y = 280)
seven = tk.Button(window, text='7', width = 6, height = 3, command = lambda: number_btn_click(7)).place(x = 20, y = 220)
eight = tk.Button(window, text='8', width = 6, height = 3, command = lambda: number_btn_click(8)).place(x = 80, y = 220)
nine = tk.Button(window, text='9', width = 6, height = 3, command = lambda: number_btn_click(9)).place(x = 140, y = 220)
zero = tk.Button(window, text='0', width = 6, height = 3, command = lambda: number_btn_click(9)).place(x = 20, y = 400)
#Operators
plus = tk.Button(window, text='+', width = 4, height = 3, command =  window).place(x = 240, y = 280)
subtract = tk.Button(window, text='-', width = 4, height = 3, command =  window).place(x = 290, y = 280)
multiply = tk.Button(window, text='x', width = 4, height = 3, command =  window).place(x = 240, y = 340)
divide = tk.Button(window, text='÷', width = 4, height = 3, command =  window).place(x = 290, y = 340)
factorial = tk.Button(window, text='!', width = 4, height = 3, command =  window).place(x = 240, y = 400)
signchange = tk.Button(window, text='+/-', width = 4, height = 3, command =  window).place(x = 290, y = 400)
equal = tk.Button(window, text='=', width = 6, height = 3, command =  window).place(x = 140, y = 400)
dcpoint = tk.Button(window, text='.', width = 6, height = 3, command =  window).place(x = 80, y = 400)
#Functions
memoryplus = tk.Button(window, text='M+', width = 6, height = 2, command = lambda: number_btn_click(1)).place(x = 30, y = 110)
memorysub = tk.Button(window, text='M-', width = 6, height = 2, command = lambda: number_btn_click(1)).place(x = 90, y = 110)
memorycall = tk.Button(window, text='MC', width = 6, height = 2, command = lambda: number_btn_click(1)).place(x = 150, y = 110)
squareroot = tk.Button(window, text='√', width = 6, height = 2, command = lambda: number_btn_click(1)).place(x = 210, y = 110)
exponent = tk.Button(window, text='^', width = 6, height = 2, command = lambda: number_btn_click(1)).place(x = 270, y = 110)
sin = tk.Button(window, text='sin', width = 6, height = 2, command = lambda: number_btn_click(1)).place(x = 150, y = 160)
cos = tk.Button(window, text='cos', width = 6, height = 2, command = lambda: number_btn_click(1)).place(x = 210, y = 160)
tan = tk.Button(window, text='tan', width = 6, height = 2, command = lambda: number_btn_click(1)).place(x = 270, y = 160)
log = tk.Button(window, text='log', width = 6, height = 2, command = lambda: number_btn_click(1)).place(x = 30, y = 160)
percentage = tk.Button(window, text='%', width = 6, height = 2, command = lambda: number_btn_click(1)).place(x = 90, y = 160)

clear = tk.Button(window, text='C', width = 4, height = 3, command = lambda: number_btn_click(1)).place(x = 290, y = 220)
delete = tk.Button(window, text='DEL', width = 4, height = 3, command = lambda: number_btn_click(1)).place(x = 240, y = 220)

dis = tk.Text(window, width = 38, height = 5, wrap = 'none')
dis.place(x = 20, y = 10)
make_display_read_only(dis)


window.mainloop()




