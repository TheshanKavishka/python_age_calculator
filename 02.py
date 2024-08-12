from tkinter import *
from datetime import date


def calculate():
    today = date.today()
    birthdate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    # age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    year = today.year - birthdate.year
    month = today.month - birthdate.month
    day = today.day - birthdate.day

    if day < 0:
        month -= 1
        day += (today.replace(day=1) - date(today.year, today.month - 1, 1)).days

    if month < 0:
        year -= 1
        month += 12
    
    Label(text=f"{nameValue.get()}. Your age is {year} Years, {month} Months and {day} Days",font=30).place(x=200, y=500)

root = Tk()
root.geometry("800x600")
root.resizable(False,False)
root.title("Age Calculator Python")

photo = PhotoImage(file="Logo.png")
myImage = Label(image=photo)
myImage.pack(padx=15, pady=15)

Label(text="Name", font=23).place(x=200, y=250)
Label(text="Year", font=23).place(x=200, y=300)
Label(text="Month", font=23).place(x=200, y=350)
Label(text="Day", font=23).place(x=200, y=400)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue, width=30, bd=3, font=20)
nameEntry.place(x=300,y=250)

yearEntry = Entry(root, textvariable=yearValue, width=30, bd=3, font=20)
yearEntry.place(x=300,y=300)

monthEntry = Entry(root, textvariable=monthValue, width=30, bd=3, font=20)
monthEntry.place(x=300,y=350)

dayEntry = Entry(root, textvariable=dayValue, width=30, bd=3, font=20)
dayEntry.place(x=300,y=400)

Button(text="Calculate", font=20, bg="black",fg="white", width=11, height=2, command=calculate).place(x=300, y=450)

root.mainloop()