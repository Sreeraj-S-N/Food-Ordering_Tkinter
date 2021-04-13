from tkinter import *
from tkinter import messagebox
import sqlite3 as lite


def order():
    root = Tk()
    root.geometry("300x250")
    root.title("Order Page")
    Label(root,text="Food Details").grid(row=0,column=6)
    var1 = IntVar()
    Checkbutton(root, text="Dosa", variable= var1).grid(row=2,sticky=W)
    var2 = IntVar()
    Checkbutton(root, text="Roti", variable=var2).grid(row=3, sticky=W)
    var3 = IntVar()
    Checkbutton(root, text="Idli", variable=var3).grid(row=4, sticky=W)

    # def connection():
    #     con = lite.connect('food.db')
    #     with con:
    #         cur = con.cursor()
    #         cur.execute(
    #             "CREATE TABLE IF NOT EXISTS order(Name TEXT,Quantity INT,Price INT)")
    #         con.commit()

    def viewSelected():
        choice = var.get()
        if choice == 1:
            output = "Coffee"

        elif choice == 2:
            output = "Tea"

        elif choice == 3:
            output = "Milk"
        else:
            output = "Invalid selection"

        return messagebox.showinfo('PythonGuides', f'You Selected {output}.')

    var = IntVar()
    Radiobutton(root, text="Coffee", variable=var, value=1, command=viewSelected).grid(row=5)
    Radiobutton(root, text="Tea", variable=var, value=2, command=viewSelected).grid(row=6)
    Radiobutton(root, text="Milk", variable=var, value=3, command=viewSelected).grid(row=7)



    def insert_data():
        conn = lite.connect('students.db')
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO order(Name,Quantity,Price) VALUES(?,?,?)",(ientry.get(),ientry2.get(),ientry3.get(),ientry4.get(),ientry5.get(),ientry6.get(),ientry7.get()))
            conn.commit()
            messagebox.showinfo("SUCCESS","Data Successfully Inserted")

    root.mainloop()

order()