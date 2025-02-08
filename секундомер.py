from datetime import datetime
from tkinter import *

temp = 0
after_id = ''

def tick():
    global temp, after_id
    after_id = window.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    label1.configure(text=str(f_temp))
    temp += 1


def start_tick():
    Start.pack_forget()
    Stop.pack()
    tick()

def stop_tick():
    Stop.pack_forget()
    Continue.pack()
    Restart.pack()
    window.after_cancel(after_id)

def continue_tick():
    Continue.pack_forget()
    Restart.pack_forget()
    Stop.pack()
    tick()

def restart_tick():
    global temp
    temp = 0
    label1.configure(text='00:00')
    Continue.pack_forget()
    Restart.pack_forget()
    Start.pack()


window = Tk()
window.title("cекундомер")
window.resizable(width=False, height=False)
window.geometry('300x200')
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry("+%d+%d" % (x, y))

label1 = Label(window, width=10, font=('Comic Sans MS', 30), text='00:00')
label1.pack()

Start = Button(window, text='Cтарт', font=('Comic Sans MS', 20,),bg ="Green", fg="White", width=15, command=start_tick)
Stop = Button(window, text='Cтоп', font=('Comic Sans MS', 20), bg="Red",fg="White", width=15, command=stop_tick)
Restart = Button(window, text='Cброс', font=('Comic Sans MS', 20), bg="Orange",fg="White", width=15, command=restart_tick)
Continue = Button(window, text='Продолжить', font=('Comic Sans MS', 20),bg="Blue",fg="White", width=15, command=continue_tick)
Start.pack()


window.mainloop()
