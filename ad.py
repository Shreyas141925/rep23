import mysql.connector as mc
from tkinter import *
import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
from datetime import timedelta
from datetime import date
import mysql.connector as mc
con1=mc.connect(host="localhost",username="root",passwd="ashreyas@1419",database="Library")
cur=con1.cursor()
def main():
    root=Tk()
    app=Addbook(root)






class Addbook:
    def __init__(self,master):
        self.master=master
        self.master.title("Add book")
        self.master.geometry('600x450+0+0')
        self.master.config(bg="red")
        self.frame=Frame(self.master,bg="black")
        self.frame.place(x=50,y=50,width=500,height=350)
        self.frame2=Frame(self.frame,bg="pink")
        self.frame2.place(x=10,y=10,width=480,height=330)
        self.lbl1=Label(self.frame2,text='Book Id',bg='purple',font=(12)).place(x=40,y=30,width=90,height=30)
        
        self.Bookid=StringVar()
        
        self.ent1=Entry(self.frame2,font=(12),textvariable=self.Bookid).place(x=140,y=30,width=300,height=30)
        
        self.btn1=Button(self.frame2,text='Add',bg="Red",font=(12),command=self.addbook).place(x=20,y=270,width=140,height=30)
    def addbook(self):
        bi=self.Bookid.get()
        
        surety=mb.askyesno('adding...',"Are you aure you want to enter this data")
        if surety:
            sql="SELECT * FROM Book WHERE Book_id=%s"
            val=list(bi)
            cur.execute(sql,val)
            con1.commit()
            mb.showinfo("done","Successfully recorc added")
        





main()
