from tkinter import*
import pymysql
from PIL import ImageTk
from tkinter import ttk, messagebox
from tkinter import messagebox
import sqlite3
#from register_main import Register
# from EMP import *

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        # self.root.resizable(False,False)
        #-------BG Image
        self.bg=ImageTk.PhotoImage(file="C:\\Users\\Admin\\Desktop\\practice payroll\\background.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #------Login Frame
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="dark blue",bg="white").place(x=110,y=30)
        desc = Label(Frame_login, text="Accountant Employee Login Area", font=("Goudy old style", 15, "bold"), fg="blue", bg="white").place(x=90,y=100)

        lbl_user = Label(Frame_login, text="Username", font=("Goody old style", 15, "bold"),fg="gray", bg="white").place(x=90, y=140)
        self.txt_user = Entry(Frame_login,font=("time new roman", 15), bg="light gray")
        self.txt_user.place(x=90, y=170, width=350, height=35)

        lbl_pass = Label(Frame_login, text="Password", font=("Goody old style", 15, "bold"), fg="gray",bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, font=("time new roman", 15), bg="light gray")
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        forget_button=Button(Frame_login,text="New User? Register Here",cursor="hand2",bg="white",fg="dark blue",bd=0,font=("times new roman",12)).place(x=90,y=280)
        login_button = Button(self.root,command=self.login_function,cursor="hand2", text="Login", fg="white", bg="dark blue",font=("times new roman", 20)).place(x=300, y=470,width=180,height=40)


    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All field are Required",parent=self.root)
        # elif self.txt_pass.get() != "12345" or self.txt_user.get() != "Suyash":
        #     messagebox.showerror("Error", "Invalid Username and Password", parent=self.root)
        else:
            conn = sqlite3.connect('record_2.db')
            conn.row_factory = lambda cursor, row: row[0]
            cursor_user = conn.cursor()
            cursor_user.execute("select email from Table_2")

            row_user=cursor_user.fetchall()
            print(row_user)

            cursor_password = conn.cursor()
            cursor_password.execute("select password from Table_2")
            row_password = cursor_password.fetchall()
            print(row_password)

            user_entry = self.txt_user.get()
            password_entry = self.txt_user.get()

            for i in row_user:
                if i == user_entry:
                    print("Username Found")
                # else:
                #     print("Username Not Found")


            # if user_entry in row_user:
            #     print("Username is correct")
            # #else:
            #     print("Invalid Username and Password")

            # if row==None:
            #     messagebox.showerror("Error", "Invalid Username and Password", parent=self.root)
            # else:
            #     messagebox.showinfo("Success", "Welcome", parent=self.root)

            # messagebox.showinfo("Welcome", f"Welcome {self.txt_user.get()}\n Your Password: {self.txt_pass.get()}", parent=self.root)
            # self.login()

    def login(self):
        print(self.txt_user.get(), self.txt_pass.get())



    def register(self,root):
        pass
        #Register()




#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
root=Tk()
obj=Login(root)
root.mainloop()