try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

main_window = tkinter.Tk()

main_window.title("FUck you")
main_window.geometry("640x480")

label = tkinter.Label(main_window, text = "Hello World")
label.pack(side='top')

left_frame = tkinter.Frame(main_window)
left_frame.pack(side='left', anchor='n', fill=tkinter.Y, expand = False)


canvas = tkinter.Canvas(main_window, relief= 'raised', borderwidth=1)
canvas.pack(side='left', anchor = 'n')

right_frame = tkinter.Frame(main_window)
right_frame.pack(side='right', anchor='n', expand = True)
button1 = tkinter.Button(right_frame,  text = "button1")
button2 = tkinter.Button(right_frame,  text = "button2")
button3 = tkinter.Button(right_frame,  text = "button3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')
main_window.mainloop()