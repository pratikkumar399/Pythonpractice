from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label3.config(text=float(new_text)*1.609)

kilometer = 0

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=20)

# label
my_label = Label()
my_label.config(text="Miles")
my_label.grid(column=3, row=1)
# my_label.config(padx=50, pady=50)

my_label2 = Label()
my_label2.config(text="is equal to")
my_label2.grid(column=1,row=2)

my_label3 = Label()
my_label3.config(text="0")
my_label3.grid(column=2,row=2)

my_label4 = Label()
my_label4.config(text="km")
my_label4.grid(column=3,row=2)



# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=2, row=1)


window.mainloop()
