import tkinter

main_window = tkinter.Tk()

main_window.title("Calculator")
main_window.geometry("240x240")
main_window['padx'] = 8


label = tkinter.Entry(main_window)
label.grid(row = 0, column =0, columnspan = 3, sticky='nsew')

cbutton = tkinter.Button(main_window, text="C")
cebutton = tkinter.Button(main_window, text="CE")
cbutton.grid(row = 1, column =0, sticky=tkinter.E +tkinter.W)
cebutton.grid(row = 1, column =1, sticky=tkinter.E +tkinter.W)
buttons = ["7","8","9","+","4","5","6","-","1","2","3", "*", "0", "=", "/"]

row = 2
column = 0
for b in buttons:
    button = tkinter.Button(main_window, text=b)
    if b == '=':
        button.grid(row = row, column = column, sticky=tkinter.E +tkinter.W)
    else:
        button.grid(row = row, column = column, sticky=tkinter.E +tkinter.W)
    column += 1
    if column == 4:
        column = 0
        row +=1










main_window.mainloop()