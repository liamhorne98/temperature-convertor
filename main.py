from tkinter import *
from tkinter import messagebox

temp_Val = "Celsius"

def call_convert(rlabel1, inputn):
    temp = inputn.get()

    def store_temp(set_temp):
        global temp_Val
        temp_Val = set_temp

    if temp_Val == 'Celsius':
        # Conversion of celsius temperature to fahrenheit
        f = float((float(temp) * 9 / 5) + 32)
        rlabel1.config(text="%.1f Fahrenheit" % f)
        messagebox.showinfo("Temperature Converter",
                            "Successfully converted to Fahrenheit ", )

    if temp_Val == 'Fahrenheit':
        # Conversion of fahrenheit temperature
        # to celsius
        c = float((float(temp) - 32) * 5 / 9)
        rlabel1.config(text="%.1f Celsius" % c)
        messagebox.showinfo("Temperature Converter",
                            "Successfully converted to Celsius ")
    return

def clearfunc():
    e1.delete(0)
    e2.delete(0)
    store_temp.set("")


master = Tk()
myText = StringVar()
Label(master, text="Celcius").grid(row=0, sticky=W)
Label(master, text="Farenheight").grid(row=1, sticky=W)
Label(master, text="Result:").grid(row=3, sticky=W)
result = Label(master, text="", textvariable=myText).grid(row=3, column=1, sticky=W)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b = Button(master, text="Calculate", command=addNumbers)
b.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W, padx=5, pady=5)
b2=Button(master, text="Clear", command=clearfunc)
b2.grid(row=5,column=5)






master.mainloop()