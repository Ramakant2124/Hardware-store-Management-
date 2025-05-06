from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import os
class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Ramakant Plywood & Hardware | Designer by Ramakant")
        self.root.config(bg="#FFE4B5")
        self.root.focus_force()
        
        self.bill_list=[]
        self.var_invoice=StringVar()
        
    #==========title====
        lbl_title=Label(self.root,text=" View Customer Bills",font=("goudyold style",30),bg="#B00857",fg="#E6E6FA",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_invoice=Label(self.root,text=" Invoice No.",font=("time new roman",15),bg="white").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("time new roman",15),bg="lightyellow").place(x=160,y=100,width=180,height=28)
        
        btn_search=Button(self.root,text="search",command=self.search,font=("time new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=360,y=100,width=120,height=28)
        btn_clear=Button(self.root,text="clear",command=self.clear,font=("time new roman",15,"bold"),bg="lightgray",fg="black",cursor="hand2").place(x=490,y=100,width=120,height=28)
        
    #======bill list
        sales_Frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_Frame.place(x=50,y=140,width=300,height=330)
        
        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.sales_list=Listbox(sales_Frame,font=(" goudy old style",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill="y")
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)
        
        #==========bill area
        bill_Frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_Frame.place(x=380,y=140,width=410,height=330)
        
        lbl_title2=Label(bill_Frame,text="Customer Bill Area",font=("goudyold style",20),bg="orange").pack(side=TOP,fill=X)

        
        scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
        self.bill_area=Text(bill_Frame,bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill="y")
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        
        self.show()
    #===================================================================================================================================
    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
                
                
    def get_data(self,ev):
            index_=self.sales_list.curselection()  
            file_name=self.sales_list.get(index_)  
            #print(file_name)
            self.bill_area.delete('1.0',END)
            fp=open(f'bill/{file_name}','r') 
            for i in fp:
                self.bill_area.insert(END,i)
            fp.close() 
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","invoice no, should be requiered",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:  
               fp=open(f'bill/{self.var_invoice.get()}.txt','r') 
               self.bill_area.delete('1.0',END)
               for i in fp:
                self.bill_area.insert(END,i)
               fp.close()
            else:
              messagebox.showerror("Error"," Invalid invoice no.",parent=self.root)
          
    def clear(self):
     self.show()
     self.bill_area.delete('1.0',END)       
                
        
if __name__=="__main__":       
     root=Tk()
     obj=salesClass(root)
     root.mainloop()