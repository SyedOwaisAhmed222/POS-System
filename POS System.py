
import time
from tkinter import *
import tkinter
window=tkinter.Tk()
window.title('SUBWAY POS')
tkinter.Label(window,text='Menu',font=("Times", 30, "bold")).grid(row=0,column=0)
tkinter.Label(window,text='Price',font=("Times", 30, "bold")).grid(row=0,column=1)
tkinter.Label(window,text='Quantity',font=("Times", 30, "bold")).grid(row=0,column=2,padx=10)
tkinter.Label(window,text='Info',font=("Times", 35, "bold")).grid(row=0,column=4,sticky="W",padx=100)
tkinter.Label(window,text="Broast",font=("Times", 20)).grid(row=1,column=0,padx = 10)
tkinter.Label(window,text="Pizza",font=("Times", 20)).grid(row=2,column=0,padx = 10)
tkinter.Label(window,text="Chawmen",font=("Times", 20)).grid(row=3,column=0,padx = 10)
tkinter.Label(window,text="Zinger",font=("Times", 20)).grid(row=4,column=0)
tkinter.Label(window,text="Chinese Rise",font=("Times", 20)).grid(row=5,column=0)
tkinter.Label(window,text="Cold Drink",font=("Times", 20)).grid(row=6,column=0)
tkinter.Label(window,text="Falooda",font=("Times", 20)).grid(row=7,column=0)
tkinter.Label(window,text="Tea",font=("Times", 20)).grid(row=8,column=0)

broast_price=220
pizza_price=600
chaomin_price=450
zinger_price=290
chineaserise_price=300
colddrink_price=30
faloda_price=120
tea_price=25

tkinter.Label(window,text=broast_price,font=("Times", 20)).grid(row=1,column=1,padx = 10)
tkinter.Label(window,text=pizza_price,font=("Times", 20)).grid(row=2,column=1,padx = 10)
tkinter.Label(window,text=chaomin_price,font=("Times", 20)).grid(row=3,column=1,padx = 10)
tkinter.Label(window,text=zinger_price,font=("Times", 20)).grid(row=4,column=1,padx = 10)
tkinter.Label(window,text=chineaserise_price,font=("Times", 20)).grid(row=5,column=1,padx = 10)
tkinter.Label(window,text=colddrink_price,font=("Times", 20)).grid(row=6,column=1,padx = 10)
tkinter.Label(window,text=faloda_price,font=("Times", 20)).grid(row=7,column=1,padx = 10)
tkinter.Label(window,text=tea_price,font=("Times", 20)).grid(row=8,column=1,padx = 10)

q1=tkinter.Entry(window,font=("Times", 20),width=5)
q1.grid(row=1,column=2)

q2=tkinter.Entry(window,font=("Times", 20),width=5)
q2.grid(row=2,column=2)

q3=tkinter.Entry(window,font=("Times", 20),width=5)
q3.grid(row=3,column=2)

q4=tkinter.Entry(window,font=("Times", 20),width=5)
q4.grid(row=4,column=2)

q5=tkinter.Entry(window,font=("Times", 20),width=5)
q5.grid(row=5,column=2)

q6=tkinter.Entry(window,font=("Times", 20),width=5)
q6.grid(row=6,column=2)

q7=tkinter.Entry(window,font=("Times", 20),width=5)
q7.grid(row=7,column=2)

q8=tkinter.Entry(window,font=("Times", 20),width=5)
q8.grid(row=8,column=2)

tkinter.Label(window,text='User Name:',font=("Times", 20)).grid(row=1,column=4)
e1=tkinter.Entry(window,font=("Times", 30))
e1.grid(row=1,column=5,pady=5)
tkinter.Label(window,text='Order No:',font=("Times", 20)).grid(row=2,column=4)
e2=tkinter.Entry(window,font=("Times", 30))
e2.grid(row=2,column=5,pady=5)

def Sub_total():
    global s_total
    s_total=0
    s_total+=int(q1.get())*broast_price
    s_total+=int(q2.get())*pizza_price
    s_total+=int(q3.get())*chaomin_price
    s_total+=int(q4.get())*zinger_price
    s_total+=int(q5.get())*chineaserise_price
    s_total+=int(q6.get())*colddrink_price
    s_total+=int(q7.get())*faloda_price
    s_total+=int(q8.get())*tea_price
    S1="Sub Total: Rs:",s_total,"/-"
    mylabel=tkinter.Label(window,text=S1,font=("Times", 20))
    mylabel.grid(row=4,column=4)

B1=tkinter.Button(window,text='Sub total!',font=("Times",20),bg="#d6d6c2",
                  relief=SUNKEN,command=Sub_total)
B1.grid(row=3,column=5)

def Generate_Receipt():
    s1_total=0
    s1_total+=int(q1.get())*broast_price
    s1_total+=int(q2.get())*pizza_price
    s1_total+=int(q3.get())*chaomin_price
    s1_total+=int(q4.get())*zinger_price
    s1_total+=int(q5.get())*chineaserise_price
    s1_total+=int(q6.get())*colddrink_price
    s1_total+=int(q7.get())*faloda_price
    s1_total+=int(q8.get())*tea_price
    

    l1a=tkinter.Label(window,text="Receipt",font=("Times", 30,"bold"))
    l1a.grid(row=7,column=5)
    
    
    l1v="Customer Name: ",e1.get()
    l1=tkinter.Label(window,text=l1v,font=("Times", 20))
    l1.grid(row=8,column=5)
    
    l2v="Order Number: ",e2.get()
    l2=tkinter.Label(window,text=l2v,font=("Times", 20))
    l2.grid(row=9,column=5)
    
    
    l3v="GST: Rs",(s1_total*13)/100,'/-'
    l3=tkinter.Label(window,text=l3v,font=("Times", 20))
    l3.grid(row=10,column=5)

   
    
    l4v="Total: ",s1_total+(s1_total*13)/100,"/-"
    l4=tkinter.Label(window,text=l4v,font=("Times", 20))
    l4.grid(row=11,column=5)
    
    l5v=time.strftime('%I:%M %p on %m/%d/%Y', time.localtime())
    l5=tkinter.Label(window,text=l5v,font=("Times", 20))
    l5.grid(row=12,column=5)

B2=tkinter.Button(window,text='Generate_Receipt',font=("Times",20),bg="#c6d9eb",
                  relief=SUNKEN,command=Generate_Receipt)
B2.grid(row=4,column=5,pady=5)
window.mainloop()


