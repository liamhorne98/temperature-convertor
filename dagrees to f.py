from tkinter import *
from tkinter import messagebox
from functools import partial
#delclaration of global variable
temp_Val = "Celsius"
#drop down value
def store_temp(set_temp):
    global temp_Val
    temp_Val = set_temp
#clear function
def clear():
    input_entry.configure(text="")
    result_label.configure(text="")
#The conversion of temp
def call_convert(rlabel1, inputn):
    temp = inputn.get()
#celsius to fahrenheight
    if temp_Val == 'Celsius':
        f = float((float(temp) * 9 / 5) + 32)
        rlabel1.config(text="%.1f Fahrenheit" % f)
        messagebox.showinfo("Temperature Converter",
                            "Successfully converted to Fahrenheit ", )
#fahrenheit to temperature
    if temp_Val == 'Fahrenheit':
        c = float((float(temp) - 32) * 5 / 9)
        rlabel1.config(text="%.1f Celsius" % c)
        messagebox.showinfo("Temperature Converter",
                            "Successfully converted to Celsius ")
    return
#tk is the window
root =Tk()
#size of window
root.geometry('500x350')
#title name
root.title('Temperature Converter')
#Lay out of widgets
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)
root.configure(background="grey")
inputNumber =StringVar()
var =StringVar()
#label and entry
input_label =Label(root, text="Enter temperature in :")
input_entry =Entry(root, textvariable=inputNumber)
input_label.grid(row=1)
input_entry.grid(row=1, column=1)
result_label =Label(root)
result_label.grid(row=2, columnspan=5)
#drop down setup
dropDownList = ["Celsius", "Fahrenheit"]
drop_down =OptionMenu(root, var, *dropDownList,
                          command=store_temp)
var.set(dropDownList[0])
drop_down.grid(row=1, column=2)
#button widget
call_convert = partial(call_convert, result_label,
                       inputNumber)
result_button =Button(root, text="Convert",
                          command=call_convert)
result_button.grid(row=2, column=2)
#rest of buttons exit and clear
b2=Button(root, text="Clear", command=clear)
b2.grid(row=2,column=4)
exit_b=Button(root,text="exit",command=root.destroy)
exit_b.grid(row=2, column=0)
#infinit loop set
root.mainloop()
