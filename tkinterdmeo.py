try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

main_window = tkinter.Tk()

main_window.title("FUck you")
main_window.geometry("640x640")
main_window.mainloop()