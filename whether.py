from tkinter import*
from tkinter import ttk
import requests

def data_get():
    

    city=cityname.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
    we1.config(text=data["weather"][0]["main"])
    wb1.config(text=data["weather"][0]["description"])
    tem1.config(text=(data["main"]["temp"]-273.15))
    p1.config(text=data["main"]["pressure"])

win=Tk()
win.title("weather casting")
win.config(bg="black")
win.geometry("500x500")



name_lable=Label(win,text="weather casting",font=("arial",35,"bold"))
name_lable.place(x=25,y=50,height=50,width=450)

list_name=[
    "Ambala", "Bhiwani", "Charkhi Dadri", "Faridabad", "Fatehabad",
    "Gurugram", "Hisar", "Jhajjar", "Jind", "Kaithal", "Karnal",
    "Kurukshetra", "Mahendragarh", "Nuh", "Palwal", "Panchkula",
    "Panipat", "Rewari", "Rohtak", "Sirsa", "Sonipat", "Yamunanagar","Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"

    "Bilaspur",
    "Chamba",
    "Hamirpur",
    "Kangra",
    "Kinnaur",
    "Kullu",
    "Lahaul and Spiti",
    "Mandi",
    "Shimla",
    "Sirmaur",
    "Solan",
    "Una","manali"
]


cityname=StringVar()
conb=ttk.Combobox(win,text="whether casting",values=list_name,font=("arial",14,"bold"),textvariable=cityname)
conb.place(x=75,y=120,height=30,width=350)





we=Label(win,text="Climate",font=("arial",14,"bold"))
we.place(x=25,y=260,height=40,width=200)
we1=Label(win,text="",font=("arial",12,"bold"))
we1.place(x=290,y=260,height=40,width=200)



wb=Label(win,text="Discription",font=("arial",14,"bold"))
wb.place(x=25,y=320,height=40,width=200)
wb1=Label(win,text="",font=("arial",12,"bold"))
wb1.place(x=290,y=320,height=40,width=200)



tem=Label(win,text="Temprature",font=("arial",14,"bold"))
tem.place(x=25,y=380,height=40,width=200) 
tem1=Label(win,text="",font=("arial",12,"bold"))
tem1.place(x=290,y=380,height=40,width=200)



p=Label(win,text="Pressure",font=("arial",14,"bold"))
p.place(x=25,y=440,height=40,width=200)
p1=Label(win,text="",font=("arial",12,"bold"))
p1.place(x=290,y=440,height=40,width=200)


but=Button(win,text="show",font=("arial",14,"bold"),command=data_get)
but.place(x=200,y=190,height=50,width=100)



mainloop()




