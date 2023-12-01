#-----------------------------
#Importing tkinter and creating a window
import tkinter as tk 
window = tk.Tk()
window.title("Binary-Hex-Denary Converter")
window.geometry("650x200")
#-----------------------------

#Function to convert
def convert():
    if (len(b_entry.get())) >= 1:
        b_num = (b_entry.get())
        d_eq = int(b_num,2)
        d_entry.delete(0,tk.END)
        d_entry.insert(0,str(d_eq))
        h_eq = hex(d_eq)
        h_entry.delete(0,tk.END)
        h_entry.insert(0,str(h_eq))
    elif (len(h_entry.get())) >= 1:
        h_num = (h_entry.get())
        d_eq = int(h_num,16)
        d_entry.delete(0,tk.END)
        d_entry.insert(0,str(d_eq))
        b_eq = bin(d_eq)
        b_eq = b_eq.replace("0b","")
        b_entry.delete(0,tk.END)
        b_entry.insert(0,str(b_eq))
    elif (len(d_entry.get())) >= 1:
        d_num = (d_entry.get())
        h_eq = hex(int(d_num))
        h_entry.delete(0,tk.END)
        h_entry.insert(0,str(h_eq))
        b_eq = bin(int(d_num))
        b_eq = b_eq.replace("0b","")
        b_entry.delete(0,tk.END)
        b_entry.insert(0,str(b_eq))


#Function to refresh all entries
def refresh():
    b_entry.delete(0,tk.END)
    h_entry.delete(0,tk.END)
    d_entry.delete(0,tk.END)

#Welcome Label
t_label = tk.Label(window,text="Binary-Hex-Denary Converter\n-----------------")
t_label.grid(row=1,column=1)

#Instructions label
i_lable = tk.Label(window,text="Instructions!\nEnter in the bin/hex/den you want to convert into the correct box and hit convert")
i_lable.grid(row=9,column=0)

#Creating the binary text box entry
b_label = tk.Label(window,text="Binary Number:")
b_label.grid(row=3,column=0)
b_entry = tk.Entry(window)
b_entry.grid(row=3,column=1)

#Creating a hex output box
h_label = tk.Label(window,text="Hexadecimal Equivalent")
h_label.grid(row=5,column=0)
h_entry = tk.Entry(window)
h_entry.grid(row=5,column=1)

#Creating a denary output box
d_label = tk.Label(window,text="Denary Equivalent")
d_label.grid(row=6,column=0)
d_entry = tk.Entry(window)
d_entry.grid(row=6,column=1)

#Converter button
convert_button = tk.Button(window,text="Convert",command=convert)
convert_button.grid(row=7,column=1)

#Quit button
quit_button = tk.Button(window,text="Quit",command=window.quit)
quit_button.grid(row=7,column=0)

#Clear all entries
clear_button = tk.Button(window,text="Refresh",command=refresh)
clear_button.grid(row=7,column=2)

#-----------------------------
window.mainloop()
#-----------------------------