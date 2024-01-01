from tkinter import *

window = Tk()

window.title("My Window Example")
window.minsize(width=500, height=300)

# label

my_label = Label(text="Sample label", font=("Arial", 24, "bold"))
my_label.pack()  # this makes text show up on the window


# button
def my_button():
    print("clicked")
    my_label.config(text="Clicked!")


button = Button(text="Click Me", command=my_button)
button.pack()


# entry
input = Entry(width=10)
input.pack()
print(input.get())


# Radio button, scale, checkbox, and more........




window.mainloop()