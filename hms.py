from cgitb import text
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
 

root = Tk()
# title 
root.title("Hospital Management System")
# windwos size
root.geometry("1340x800+0+0")
titlelbl = Label(root,bd=15,relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",fg='green',bg='white',font=("times new roman",30,BOLD))
titlelbl.pack(side=TOP,fill="x")



# ======================================= Patient Frame ===================================================
dataframe = Frame(root,bd=20,relief=RIDGE)
dataframe.place(x=0,y=100,width=1340,height=400)


dataframeleft = LabelFrame(dataframe,bd=10,padx=10,relief=RIDGE,font=("times new roman",15),text='Patient Information')
dataframeleft.place(x=0,y=5,width=900,height=350)

dataframeright = LabelFrame(dataframe,bd=10,padx=20,relief=RIDGE,font=("times new roman",15),text='Prescription')
dataframeright.place(x=920,y=5,width=350,height=350)

# =============================Buttons Frame ===========================

Buttonframe = Frame(root,bd=20,relief=RIDGE)
Buttonframe.place(x=0,y=510,width=1340,height=70)


# =============================Details Frame ===========================
detailsFrame = Frame(root,bd=20,relief=RIDGE)
detailsFrame.place(x=0,y=580,width=1340,height=120)
# =============================Data Frame Left ===========================

lblnametablet = Label(dataframeleft,text="Name Of Tablets",font=('times new roman',12,BOLD),padx=2,pady=6)
lblnametablet.grid(row=0,column=0)

combonametablet = ttk.Combobox(dataframeleft,font=('times new roman',12,BOLD),width=33)
combonametablet["values"]=("Nice","Corona Vaccine","Acetaminophen","Adderall","Ativan")
combonametablet.grid(row=0,column=1)










root.mainloop()