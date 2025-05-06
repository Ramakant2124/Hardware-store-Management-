from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from dashboard import RPAH
import os
class loginclass:
    def __init__(self,root):
        self.root=root
        self.root.title("login Window")
        self.root.geometry("1520x750+0+0")
        self.root.title("Ramakant Plywood & Hardware| Designer by Ramakant")
        self.root.config(bg="lightyellow")
        
        
         #=====login from=======
        login_frame=Frame(self.root,bg="#FFE4B5",bd=40)
        login_frame.place(x=380,y=100,height=500,width=700)
    
         
    
        title=Label(login_frame,text=" Login Here",font=("time new roman",20,"bold"),bg="#B00857",fg="#E6E6FA",bd=3,relief=RIDGE).place(x=8,y=0,width=600,height=60)
        
        
        email=Label(login_frame,text="Username :",font=("time new roman",25,"bold"),bg="#FFE4B5",fg="#B00857").place(x=220,y=100)
        self.txt_email=Entry(login_frame,font=("time new roman",15),bg="lightgray")
        self.txt_email.place(x=190,y=150,width=250,height=40)
        
        password=Label(login_frame,text="Password :",font=("time new roman",25,"bold"),bg="#FFE4B5",fg="#B00857").place(x=220,y=200)
        self.txt_password=Entry(login_frame,font=("time new roman",15),bg="lightgray")
        self.txt_password.place(x=190,y=250,width=250,height=40)
        
        btn_login=Button(login_frame,text="Login",command=self.login,font=("time new roman",15,"bold"),fg="white",bg="#B00857").place(x=220,y=380,width=200,height=50)
        
    def login(self):
        if self.txt_email.get()=='ramakant' and self.txt_password.get()=='ramakant':
            self.root.destroy()
            os.system("python dashboard.py")
            #self.dashboard()
        elif self.txt_email.get()=='' and self.txt_password.get()=='':
            messagebox.showerror('Error',"All fields are required",parent=self.root)
        else:
            messagebox.showerror('Error',"Username or Password Incorrect",parent=self.root)

            
    #def dashboard(self):
    #    self.new_win=Toplevel(self.root)
    #    self.new_obj=RPAH(self.new_win)
        
root=Tk()
obj=loginclass(root)
root.mainloop()