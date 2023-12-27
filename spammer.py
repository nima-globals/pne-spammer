import webbrowser , time , webbrowser
from random import randint
from tkinter import *
from tkinter import ttk, messagebox
from pyautogui import press,typewrite

def runspammer():
    try:
        sleeptime1_get = int(sleeptime1.get())
        sleeptime2_get = int(sleeptime2.get())
        tedad_get = int(tedad.get())
        ad_message = 0
        if spamtype == 1:
            text_get = text.get()
            ad_message = 0
        elif spamtype == 2:
            text_get = text.get()
            try:
                ad_message = int(text_get)
            except:
                messagebox.showerror(
                    "ورودی اشتباه", "لطفا مقدار شروع را درست وارد کنید")
            time.sleep(sleeptime1_get)
        for i in range(tedad_get):
            if spamtype == 2:
                typewrite(f"{ad_message}")
            elif spamtype == 3:
                typewrite(f"{randint(100,999)}")
            elif spamtype == 1:
                typewrite(f"{text_get}")
            press("enter")
            time.sleep(int(sleeptime2_get))
            ad_message += 1
    except:
        messagebox.showerror(
            "ورودی اشتباه", "لطفا مقادیر زمان و تعداد و حالت را درست وارد کنید")

window = Tk()
window.title("PNE SPAMMER")
window.resizable(0, 0)
window.geometry("400x500")
Label(window, text="PNE SPAMMER", font=("Arial", 22)).pack(pady=10)
Label(window, text="مقدار زمان صبر قبل از اجرا").pack()
sleeptime1 = Entry(window)
sleeptime1.pack()
Label(window, text="مقدار زمان صبر یعد از هر بار اجرا").pack()
sleeptime2 = Entry(window)
sleeptime2.pack()
Label(window, text="تعداد تکرار").pack()
tedad = Entry(window)
tedad.pack()
selected_spamtypebox = StringVar()
spamtypebox_cb = ttk.Combobox(
    window, textvariable=selected_spamtypebox, width=17,)
spamtypebox_cb['values'] = ["متن", "اعداد ترتیبی", "اعداد رندوم 3 رقمی"]
# spamtypebox_cb.set("انتخاب حالت")
spamtypebox_cb['state'] = 'readonly'
spamtypebox_cb.pack(padx=10, pady=5)

def spamtypebox_changed(event):
    global spamtype
    if selected_spamtypebox.get() == "متن":
        textlabel.config(text="متن برای تکرار")
        text.place(y=230, x=137)
        spamtype = 1
    elif selected_spamtypebox.get() == "اعداد ترتیبی":
        textlabel.config(text="شروع")
        text.place(y=230, x=137)
        spamtype = 2
    elif selected_spamtypebox.get() == "اعداد رندوم 3 رقمی":
        spamtype = 3
        textlabel.config(text="")
        text.place(y=42424)

spamtypebox_cb.bind('<<ComboboxSelected>>', spamtypebox_changed)
textlabel = Label(window, text="")
textlabel.pack()
text = Entry(window)
Button(window, text="start", command=runspammer).pack(pady=23)
Label(window, text="").pack(pady=25)
Label(window, text="راهنمایی:").pack()
Label(window, text="""بر روی ورودی متن یکی از پیام رسان های خود روید بعد برنامه روید
      و برنامه را اجرا کنید و دوباره برگردید به همان برنامه
      برنامه خودش حالت انتخاب شده را انجام میدهد و ارسال میکند.""").pack()
Label(window, text="").pack(pady=5)
copyright = Frame(window).pack(side=BOTTOM, fill=X)
Label(copyright, text="V1.0.0").pack(side=LEFT)
Label(copyright, text="copyright 2024 Nima.Globals").pack(side=LEFT, padx=80)
Button(copyright, text="GitHub", command=lambda: webbrowser.open(
    "https://github.com/nima-globals")).pack(side=LEFT)
window.mainloop()