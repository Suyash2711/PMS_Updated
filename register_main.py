from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
import pymysql
import sqlite3

class Register:

    def __init__(self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg = "white")

        # Bg Image
        self.bg=ImageTk.PhotoImage(file="C:\\Users\\Admin\\Desktop\\practice payroll\\payroll.png")
        bg=Label(self.root,image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Registration Frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100, width=700, height=500)


        title=Label(frame1, text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)


        #------------ROW_1

        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=50, y=100)
        self.txt_fname=Entry(frame1, font=("times new roman",15),bg="lightgrey")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_lname.place(x=370, y=130, width=250)

        #------------ROW_2
        contact = Label(frame1, text="Contact Number", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_email.place(x=370, y=200, width=250)

        # -----------ROW_3
        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white",fg="grey").place(x=50, y=240)
        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=370,y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_answer.place(x=370, y=270, width=250)

        # ------------ROW_4
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white",fg="grey").place(x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_password.place(x=50, y=340, width=250)

        c_password = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=370,y=310)
        self.txt_c_password = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_c_password.place(x=370, y=340, width=250)
        #--------------Terms
        # self.var_chk=IntVar()
        # chk=Checkbutton(frame1,text="I Agree the Terms & Conditions",onvalue=1,variable=self.var_chk, offvalue=0, bg="white",font=("times new roman",12)).place(x=50,y=380)

        #-----------Button
        btn_register=Button(frame1,text="Register Now",font=("times new roman",17), cursor="hand2",command= self.database).place(x=270,y=420)
        btn_display = Button(frame1, text="record", font=("times new roman", 17), cursor="hand2",command=self.disp).place(x=170, y=420)
        btn_delete = Button(frame1, text="Delete", font=("times new roman", 17), cursor="hand2",command=self.dele).place(x=440, y=420)

        btn_login = Button(self.root, text="Sign In", font=("times new roman", 20), bd=0, cursor="hand2").place(x=200, y=415, width=180)
        #self.check()

    def disp(self):
        conn = sqlite3.connect('record_2.db')
        with conn:
            cursor = conn.cursor()
            my_w = Tk()
            my_w.geometry("800x250")

            r_set = cursor.execute('''SELECT * from Table_2 ''');
            i = 0  # row value inside the loop
            for Table_2 in r_set:
                for j in range(len(Table_2)):
                    e = Entry(my_w, width=30, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, Table_2[j])
                i = i + 1

    def dele(self):
        conn = sqlite3.connect('record_2.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM Table_2')
            msg = messagebox.showinfo("Delete Record", "All Row Deleted")

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.txt_contact.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_c_password.get()=="":
              messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!= self.txt_c_password.get():
              messagebox.showerror("Error", "Password not Matching", parent=self.root)
        else:
            messagebox.showinfo("Success", "Registration Successful", parent=self.root)

        # elif self.var_chk.get()==0:
        #     messagebox.showerror("Error", "Please Agree our Terms and Condition", parent=self.root)


    def database(self):
        self.register_data()
        f_name = self.txt_fname.get()
        l_name = self.txt_lname.get()
        contact = self.txt_contact.get()
        email = self.txt_email.get()
        quest = self.cmb_quest.get()
        answer= self.txt_answer.get()
        password = self.txt_password.get()
        conn = sqlite3.connect('record_2.db')
        with conn:
            cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS Table_2 (f_name TEXT,l_name TEXT,contact INTEGER,email VARCHAR,quest TEXT, answer TEXT, password VARCHAR)')
        cursor.execute('INSERT INTO Table_2 (f_name,l_name,contact,email,quest,answer,password) VALUES(?,?,?,?,?,?,?)',
                       (f_name, l_name, contact, email, quest,answer,password))
        conn.commit()
        #msg = messagebox.showinfo("DB Demo", "Registration Successful")

root = Tk()
obj = Register(root)
root.mainloop()