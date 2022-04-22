from gc import set_debug
from tkinter import*
from tkinter.font import BOLD



root = Tk()
# title 
root.title("Hospital Management System")
# windwos size
root.geometry("1340x800+0+0")
titlelbl = Label(root,bd=15,relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",fg='green',bg='white',font=("times new roman",30,BOLD))
titlelbl.pack(side=TOP,fill="x")



# ==========================================================================================
dataframe = Frame(root,bd=20,relief=RIDGE)
dataframe.place(x=0,y=130,width=1340,height=400)


dataframeleft = LabelFrame(dataframe,bd=10,padx=20,relief=RIDGE,font=("times new roman",15),text='Patient Information')
dataframeleft.place(x=0,y=5,width=900,height=350)

dataframeright = LabelFrame(dataframe,bd=10,padx=20,relief=RIDGE,font=("times new roman",15),text='Prescription')
dataframeright.place(x=920,y=5,width=350,height=350)

# =============================Buttons Frame ===========================

Buttonframe = Frame(root,bd=20,relief=RIDGE)
Buttonframe.place(x=0,y=530,width=1340,height=80)

root.mainloop()