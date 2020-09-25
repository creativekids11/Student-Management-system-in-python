from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Students Management System")
        self.root.wm_iconbitmap('icon.ico')
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Students Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="orange",fg="yellow")
        title.pack(side=TOP,fill=X)

        ############ All Variables ##########
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        self.abc=IntVar()
        self.abc=self.contact_var

        ############ Manage Frame ###########
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="orange")
        Manage_Frame.place(x=18,y=100,width=380,height=565)

        m_title=Label(Manage_Frame,text="Manage Students",bg="orange",fg="white",font=("times new roman",18,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        #============roll no.==============
        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="orange",fg="white",font=("times new roman",18,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        #=======name==========
        lbl_name=Label(Manage_Frame,text="Name",bg="orange",fg="white",font=("times new roman",18,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        #============email========
        lbl_email=Label(Manage_Frame,text="Email",bg="orange",fg="white",font=("times new roman",18,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        #==========Gender=============
        lbl_gen=Label(Manage_Frame,text="Gender",bg="orange",fg="white",font=("times new roman",18,"bold"))
        lbl_gen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        #==========cantact================
        lbl_con=Label(Manage_Frame,text="Contact",bg="orange",fg="white",font=("times new roman",18,"bold"))
        lbl_con.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_con=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_con.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        #=========D.O.B========
        lbl_dob=Label(Manage_Frame,text="Address",bg="orange",fg="white",font=("times new roman",18,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        #============Address===========
        lbl_address=Label(Manage_Frame,text="Reply",bg="orange",fg="white",font=("times new roman",18,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        #===========Button Frame==========
        btn_Frame = Frame(Manage_Frame, bd=0, relief=RIDGE, bg="orange")
        btn_Frame.place(x=15, y=500, width=350, height=50)

        addbtn=Button(btn_Frame,text="Add",width=8,command=self.add_students).grid(row=0,column=2,padx=10)
        updatebtn=Button(btn_Frame, text="Update", width=8, command=self.update_data).grid(row=0, column=3, padx=10)
        deletebtn=Button(btn_Frame, text="Delete", width=8, command=self.delete_data).grid(row=0, column=4, padx=10)
        clearbtn=Button(btn_Frame, text="Clear", width=8, command=self.clear_data).grid(row=0, column=5, padx=10)

        ############ Detail Frame ###########
        detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="orange")
        detail_Frame.place(x=407,y=102,width=605,height=563)

        lbl_search=Label(detail_Frame,text="Search By",bg="orange",fg="white",font=("times new roman",19,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13),state='readonly')
        combo_search['values']=("Roll_no","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_con=Entry(detail_Frame,textvariable=self.search_txt,width=10,font=("times new roman",15))
        txt_con.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        btn_search=Button(detail_Frame,text="Search",width=6,command=self.search_data).grid(row=0,column=3,padx=10)
        btn_Show_all=Button(detail_Frame,text="Show All",width=7,command=self.fetch_data).grid(row=0,column=4,padx=10)

        #=========Table Frame=========
        table_Frame = Frame(detail_Frame, bd=0, relief=RIDGE, bg="orange")
        table_Frame.place(x=10, y=50, width=577, height=497)

        scroll_x=Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_Frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(table_Frame,columns=("Roll No.","Name","email","gender","contact","Address","Reply"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Roll No.",text="Roll No.")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Reply", text="Reply")
        self.student_table['show']='headings'
        self.student_table.column("Roll No.", width=90)
        self.student_table.column("Name", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Reply", width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
            messagebox.showerror("Error","All fields are required!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_address.get('1.0',END)
                                                                            ))
            con.commit()
            self.fetch_data()
            self.clear_data()
            con.close()
            messagebox.showinfo("Success","Record has been added")

    def fetch_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear_data(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents_cur=self.student_table.item(cursor_row)
        row_c=contents_cur['values']
        self.Roll_No_var.set(row_c[0])
        self.name_var.set(row_c[1])
        self.email_var.set(row_c[2])
        self.gender_var.set(row_c[3])
        self.contact_var.set(row_c[4])
        self.dob_var.set(row_c[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row_c[6])
    def update_data(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
            messagebox.showerror("Error","All fields are required!!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                                                    self.name_var.get(),
                                                                                                    self.email_var.get(),
                                                                                                    self.gender_var.get(),
                                                                                                    self.contact_var.get(),
                                                                                                    self.dob_var.get(),
                                                                                                    self.txt_address.get('1.0', END),
                                                                                                    self.Roll_No_var.get()
                                                                                                    ))
            con.commit()
            self.fetch_data()
            self.clear_data()
            con.close()
            messagebox.showinfo("Success","Record Has Been Updated!!")

    def delete_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear_data()
        messagebox.showinfo("Success","Record has been deleted")


    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()
    

root=Tk()
ob=student(root)
root.mainloop()
