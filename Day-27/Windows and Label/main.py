import tkinter

window = tkinter.Tk()

window.title("My Window Example")
window.minsize(width=500, height=300)

# label

my_label = tkinter.Label(text="Sample label", font=("Arial", 24, "bold"))
my_label.pack()  # this makes text show up on the window


window.mainloop()
