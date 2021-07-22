from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="db")
cur=con.cursor()
booksTable="books"
def view():
    root=Tk()
    root.title("Library")
    root.minsize(width=400,height=600)
    root.geometry("600x500")

    canvas1=Canvas(root)
    canvas1.config(bg="blue")
    canvas1.pack(expand=True,fill=BOTH)

    headingFrame1=Frame(root,bg="yellow",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel=Label(headingFrame1,text="View Books",bg="black",fg="white",font=('Courier',15))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    labelFrame=Frame(root,bg="black")
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    Label(labelFrame,text="%-10s%-40s%-30s%-20s"%("BID","Title","Author","Status"),bg='black',fg="white").place(relx=0.07,rely=0.1)
    
    Label(labelFrame, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    quitBtn=Button(root,text="quit",bg="aqua",fg="black",command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9,relwidth=0.18,relheight=0.08)

    getBooks="select * from "+booksTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame,text="%-10s%-40s%-30s%-30s"%(i[0],i[1],i[2],i[3]),bg="black",fg="white").place(relx=0.07,rely=y)
            y+=0.1
    except:
        messagebox.showinfo("failed to fetch files from database")

        quitBtn=Button(root,text="quit",bg="aqua",fg="black",command=root.destroy)
        quitBtn.place(relx=0.4,rely=0.9,relwidth=0.18,relheight=0.08)
    
        root.mainloop()
