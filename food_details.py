try:
    import Tkinter as tk
except:
    import tkinter as tk
import sqlite3 as lite
from tkinter import messagebox as msgbox


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
def connection():
        con = lite.connect('user.db')
        with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS user(Name TEXT,Addr TEXT,Phone INT,Username TEXT,Pass TEXT)")
                con.commit()


connection()
class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Login page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="").pack()
        tk.Label(self, text="Username").pack()
        username_entry = tk.Entry(self, textvariable="username")
        username_entry.pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="Password").pack()
        pwd_entry = tk.Entry(self, textvariable="password", show='*')
        pwd_entry.pack()
        tk.Label(self, text="").pack()
        def log():
            user = username_entry.get()
            upass = pwd_entry.get()
            conn = lite.connect('user.db')
            cursor = conn.execute("SELECT Pass from user WHERE Username = '" + user + "';")
            conn.commit()
            for row in cursor:
                    if upass==row[0]:
                        msgbox.showinfo("SUCCESS","Login Successfull")
                        conn.close()
                        master.switch_frame(FoodDetails)
            conn.close()           
            msgbox.showinfo("ERROR","Incorrect Credentials")
            
            
        tk.Button(self, text="Login",
                  command=lambda: log()).pack()
        tk.Button(self, text="Register",
                  command=lambda: master.switch_frame(RegPage)).pack()
        


class FoodDetails(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='blue')
        tk.Label(self, text="Welcome to homemade food shop", font=('', 13, 'bold')).grid(row=0, pady=5)
        tk.Label(self, text="Please select your choices", font=('', 9, 'bold')).grid(row=1, column=0, pady=5)
        tk.Label(self, text="Food items:-", font=('', 9, 'bold')).grid( row=2, column=0, pady=4)
        tk.Label(self, text="Drinks:-", font=('', 9, 'bold')).grid( row=6, column=0, pady=4)

        def cal():
            total_cost = 0
            food_lst = []
            costs = tk.Label(self, font=('', 8, 'bold'))
            costs.grid( row=11, column=0, pady=2)
            if (dosa_var.get() != 0):
                total_cost += dosa_var.get()
                food_lst.append('Dosa')
            if (chappathi_var.get() != 0):
                total_cost += chappathi_var.get()
                food_lst.append('Chappathi')
            if (porota_var.get() != 0):
                total_cost += porota_var.get()
                food_lst.append('Porota')
            choice = var.get()
            if choice == 1:
                total_cost += 10
                food_lst.append('Coffee')
            elif choice == 2:
                total_cost += 10
                food_lst.append('Tea')
            elif choice == 3:
                total_cost += 10
                food_lst.append('Slice')
            costs.config(text="")
            costs.configure(text="Total cost:-" + str(total_cost))
            tk.Label(self, text="Your orders:-", font=('', 9, 'bold')).grid(row=12, column=0, pady=4)
            Lb1 = tk.Listbox(self)
            for i, foods in enumerate(food_lst):
                Lb1.insert(i + 1, foods)
            Lb1.grid( row=13, column=0)
            # else:

        dosa_var = tk.IntVar()
        chappathi_var = tk.IntVar()
        porota_var = tk.IntVar()
        var = tk.IntVar()

        dosa_food = tk.Checkbutton(self, text="Dosa", variable=dosa_var, onvalue=35, offvalue=0).grid(row=3,column=0)
        chappathi_food = tk.Checkbutton(self, text="Chappathi", variable=chappathi_var, onvalue=45, offvalue=0).grid( row=4, column=0)
        porota_food = tk.Checkbutton(self, text="Porota", variable=porota_var, onvalue=50, offvalue=0).grid(row=5, column=0)

        tk.Radiobutton(self, text="Coffe", variable=var, value=1).grid( row=7, column=0)
        tk.Radiobutton(self, text="Tea", variable=var, value=2).grid( row=8, column=0)
        tk.Radiobutton(self, text="Slice", variable=var, value=3).grid( row=9, column=0)

        orders = tk.Label(self, text="").grid( row=11, column=0, pady=4)
        tk.Button(self, text="submit", width=8, command=cal).grid( row=10, column=1)

        tk.Button(self, text="Go back to Login Page",
                  command=lambda: master.switch_frame(LoginPage)).grid(row=11,column=0)


class RegPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red')

        tk.Label(self, text='Registration', font=('times', 20, 'bold')).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text='Full Name').grid(row=2, column=1, padx=5, pady=5)
        name_entry = tk.Entry(self, width=15)
        name_entry.grid(row=2, column=2, padx=5, pady=5)
        
        tk.Label(self, text='Address').grid(row=3, column=1, padx=5, pady=5)
        addr_entry = tk.Entry(self, width=15)
        addr_entry.grid(row=3, column=2, padx=5, pady=5)
        
        tk.Label(self, text='Ph no:').grid(row=4, column=1, padx=5, pady=5)
        phno_entry = tk.Entry(self, width=15)
        phno_entry.grid(row=4, column=2, padx=5, pady=5)
        
        tk.Label(self, text='Username').grid(row=5, column=1, padx=5, pady=5)
        user_entry = tk.Entry(self, width=15)
        user_entry.grid(row=5, column=2, padx=5, pady=5)
        
        tk.Label(self, text='password').grid(row=6, column=1, padx=5, pady=5)
        password_entry = tk.Entry(self, width=15)
        password_entry.grid(row=6, column=2, padx=5, pady=5)
        
        tk.Label(self, text='Already have an account?', fg='red').grid(row=9, column=2, padx=1, pady=5)
        tk.Button(self, text="Login",
                  command=lambda:master.switch_frame(LoginPage)).grid(row=9, column=3, padx=5, pady=8)

        def clear():
            name_entry.delete(0, 'end')
            addr_entry.delete(0, 'end')
            phno_entry.delete(0, 'end')
            user_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            # grade_entry.configure(text="")
        def reg():
            if(name_entry.get()!="" and addr_entry.get()!="" and name_entry.get()!="" and phno_entry.get()!="" and user_entry.get()!="" and password_entry.get()!=""):
                conn = lite.connect('user.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute("INSERT INTO user(Name,Addr,Phone,Username,Pass) VALUES(?,?,?,?,?)",(name_entry.get(),addr_entry.get(),phno_entry.get(),user_entry.get(),password_entry.get()))
                    conn.commit()
                msgbox.showinfo("SUCCESS","Data Successfully Inserted")
                master.switch_frame(LoginPage)
            else:
                msgbox.showinfo("ERROR","Enter Data")

        tk.Button(self, text="Reset", width=8, command=clear).grid(row=8, column=1, padx=5, pady=8)
        tk.Button(self, text="Submit",
                  command=lambda:reg()).grid(row=9, column=1, padx=5, pady=8)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
