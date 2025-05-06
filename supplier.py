from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Ramakant Plywood & Hardware | Designer by Ramakant")
        self.root.config(bg="#FFE4B5")
        self.root.focus_force()
        #=========================
        #  All variables======
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_desc=StringVar()
       
        
        
    
        
        
     
        
      
       
        #=====title===
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg="#B00857",fg="#E6E6FA",bd=3,relief=RIDGE).place(x=50,y=10,width=1000,height=40)
        
        
        #=====conetent======
        #====row1=====
        lbl_supplier_invoice=Label(self.root,text="Invoice No",font=("goudy old style",15),bg="#FFE4B5").place(x=50,y=80)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=180,y=80,width=180)
       
        #=======row 2=======
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="#FFE4B5").place(x=50,y=120)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=120,width=180)
       
        #=======row 3 =======
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="#FFE4B5").place(x=50,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=180,y=160,width=180)
       
        
         #=======row 4 =======
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="#FFE4B5").place(x=50,y=220)
        txt_desc=Entry(self.root,textvariable=self.var_desc,font=("goudy old style",15),bg="lightyellow").place(x=180,y=220,width=450,height=90)
       
        #===buttons===
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)
        
        #===Employee Details===
        
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,width=380,height=350)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("invoice",text="Invoice")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("desc",text="Description")

        self.supplierTable["show"]="headings"
        
        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=100)
        
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
     #==========================================================================================================================   
    
    def add(self): 
      con=sqlite3.connect(database=r'rpah.db')
      cur=con.cursor()
      try:
          if self.var_sup_invoice.get()=="":
            messagebox.showerror("Error","Invoice Must be required",parent=self.root)
          else:
            cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
            row=cur.fetchone()
            if row!=None:
              messagebox.showerror("Error","Invoice no. already assigned,try different",parent=self.root)
            else:
                cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                                    self.var_sup_invoice.get(),
                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.var_desc.get(),
                ))                    
                con.commit()
                messagebox.showinfo("Success","Supplier Addedd Successfully",parent=self.root)
                self.show()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  
         
         
    def show(self):
      con=sqlite3.connect(database=r'rpah.db')
      cur=con.cursor()
      try:
        cur.execute("select * from supplier")
        rows=cur.fetchall()
        self.supplierTable.delete(*self.supplierTable.get_children())
        for row in rows:
          self.supplierTable.insert('',END,values=row)
        
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values'] 
          
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.var_desc.set(row[3])
       
           
    def update(self): 
      con=sqlite3.connect(database=r'rpah.db')
      cur=con.cursor()
      try:
          if self.var_sup_invoice.get()=="":
            messagebox.showerror("Error","Invoice no. Must be required",parent=self.root)
          else:
            cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
            row=cur.fetchone()
            if row==None:
              messagebox.showerror("Error","Invalide invoice No.",parent=self.root)
            else:
                cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                    
                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.var_desc.get(),
                                    self.var_sup_invoice.get(),
                ))  
                con.commit()
                messagebox.showinfo("Success","supplier updated Successfully",parent=self.root)
                self.show()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  
         
    
    def delete(self):
      con=sqlite3.connect(database=r'rpah.db')
      cur=con.cursor()
      try:
          if self.var_sup_invoice.get()=="":
            messagebox.showerror("Error","Invoice No. Must be required",parent=self.root)
          else:
            cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
            row=cur.fetchone()
            if row==None:
              messagebox.showerror("Error","Invalide Invoice No.",parent=self.root)
            else:
                op=messagebox.askyesno("Confirim","Do you really want to delete?",parent=self.root)
                if op==True:
                   cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                   con.commit()
                   messagebox.showinfo("Delete","supplier Delete successfully",parent=self.root)
                   self.clear()
        
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  
    
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_desc.set("")
        self.var_searchtxt.set("")
        
        self.show()
    
    def search(self):
        con=sqlite3.connect(database=r'rpah.db')
        cur=con.cursor()
        try:
         
          if self.var_searchtxt.get()=="":  
           messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
          else:
              cur.execute("select * from invoice Where invoice=? "(self.var_searchtxt.get(),))
              row=cur.fetchone()
              if row!=None:
                 self.supplierTable.delete(*self.supplierTable.get_children())
                 self.supplierTable.insert('',END,values=row)
              else:
                messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
              
        
        
if __name__=="__main__":
    
   root=Tk()
   obj=supplierClass(root)
   root.mainloop()    