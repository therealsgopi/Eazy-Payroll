import admin_wind as aw
import emp_wind as ew
import tkinter as tk
from tkinter import messagebox
import os
import sys
    
# ----------Defining path for resources when generating ONE exe file---------
def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
# -----------------OR------------------
'''
def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
'''

def create_login_wind(con):
    cursor = con.cursor()    
    login_window = tk.Tk()

    login_window.geometry("540x627+502+123")
    login_window.resizable(0, 0)
    login_window.title("Eazy Payroll 1.0")
    login_window.configure(background="#e7eaf6")
    
    login_img = tk.PhotoImage(file= resource_path(r"resources\login.png"))
    login_img_lab = tk.Label(login_window,image = login_img)
    login_img_lab.place(relx=0.333, rely=0.105, height=200, width=204)
    login_img_lab.configure(background="#e7eaf6")
    login_window.iconbitmap(resource_path(r'resources\icon.ico'))
    
#------------------------Variables------------------------------      
    username = tk.StringVar()
    password = tk.StringVar()
    rad_role = tk.StringVar()
    
#------------------------Status Label------------------------------ 
    lab_status = tk.Label(login_window)
    lab_status.place(relx=0.019, rely=0.933, height=31, width=524)
    lab_status.configure(background="#e7eaf6")
    lab_status.configure(font="-family {Arial} -size 10 -weight bold")
    lab_status.configure(foreground="red")
    lab_status.configure(text='''---''')
    
#------------------------Functions------------------------------  
    def exitt():
        login_window.destroy()
    
    def helpp():
        messagebox.showinfo(
                "How to Login",
                '''      
                Enter valid Admin ID or Employee ID 
                and correct password and click Login''')
                
    def about():
        messagebox.showinfo(
                'About','''
                    Easy Payroll
                    Version : 1.0
                    Last Update : 17/06/2021
                    Developers :-
                       S Gopi
                       Kaushik
                    Special Thanks : Dr. Nachiyappan Sir
                    
                    Support us by Donating!!!''')
    
    def clear():
        username.set(0)
        password.set('')
        lab_status.configure(text = '---')
        
    def login():
        username.set(username.get().strip())
        password.set(password.get().strip())
        if username.get() and rad_role.get():
            if not username.get().isdigit():
                lab_status.configure(text = 'Enter a Valid Username!')
                return None
            if rad_role.get() == 'a':
                query = "select password from username where id = {} and user_role = '{}'".format(username.get(),rad_role.get())
            else:
                query = "select password from username where id = {} and user_role = '{}'".format(username.get(),rad_role.get())
            cursor.execute(query)
            ret_pass = cursor.fetchall()
        else:
            lab_status.configure(text = 'Enter Username and select User Role!')
            return None
            
        if ret_pass:
            if password.get() == ret_pass[0][0]:
                exitt()
                if rad_role.get() == 'a':
                    aw.create_admin_wind(con,username.get())
                else:
                    ew.create_emp_wind(con,username.get())
            else:
                lab_status.configure(text = 'Incorrect password!')
        else:
            if rad_role.get() == 'a':
                lab_status.configure(text = 'Administrator not registered!')
            else:
                lab_status.configure(text = 'Employee not registered!')
            return None

#------------------------Menu------------------------------             
    menubar = tk.Menu(login_window)
    login_window.configure(menu = menubar)

    file = tk.Menu(menubar)
    file.add_command(label="Exit",command = exitt)
    menubar.add_cascade(menu=file,label="File")
    
    option = tk.Menu(menubar)
    option.add_command(label="About",command = about)
    option.add_command(label="Help",command = helpp)
    menubar.add_cascade(menu=option,label="Options")
    
#------------------------Labels------------------------------             
    label_0 = tk.Label(login_window)
    label_0.place(relx=0.13, rely=0.01, height=50, width=411)
    label_0.configure(background="#e7eaf6")
    label_0.configure(font="-family {Arial} -size 24 -weight bold -slant italic")
    label_0.configure(foreground="#1089ff")
    label_0.configure(text='''Welcome to Eazy Payroll''')
    label_0.configure(relief = 'solid')

    lab_user = tk.Label(login_window)
    lab_user.place(relx=0.278, rely=0.455, height=33, width=111)
    lab_user.configure(background="#e7eaf6")
    lab_user.configure(font="-family {Arial} -size 12 -weight bold")
    lab_user.configure(foreground="#000000")
    lab_user.configure(text='''Username :''')

    lab_pass = tk.Label(login_window)
    lab_pass.place(relx=0.296, rely=0.524, height=33, width=101)
    lab_pass.configure(background="#e7eaf6")
    lab_pass.configure(font="-family {Arial} -size 12 -weight bold")
    lab_pass.configure(foreground="#000000")
    lab_pass.configure(text='''Password :''')
    
#------------------------Entry------------------------------             
    entry_user = tk.Entry(login_window)
    entry_user.place(relx=0.519, rely=0.461, height=20, relwidth=0.23)
    entry_user.configure(background="white")
    entry_user.configure(foreground="#000000")
    entry_user.configure(textvariable=username)

    entry_pass = tk.Entry(login_window)
    entry_pass.place(relx=0.519, rely=0.54, height=20, relwidth=0.23)
    entry_pass.configure(background="white")
    entry_pass.configure(foreground="#000000")
    entry_pass.configure(textvariable=password)

#------------------------Radio Button------------------------------  
    rad_user = tk.Radiobutton(login_window)
    rad_user.place(relx=0.556, rely=0.606, relheight=0.061, relwidth=0.226)
    rad_user.configure(background="#e7eaf6")
    rad_user.configure(font="-family {Arial} -size 12 -weight bold")
    rad_user.configure(foreground="#000000")
    rad_user.configure(justify='left')
    rad_user.configure(text='''Employee''')
    rad_user.configure(variable = rad_role)
    rad_user.configure(value = 'e')

    rad_admin = tk.Radiobutton(login_window)
    rad_admin.place(relx=0.259, rely=0.606, relheight=0.061, relwidth=0.17)
    rad_admin.configure(background="#e7eaf6")
    rad_admin.configure(font="-family {Arial} -size 12 -weight bold")
    rad_admin.configure(foreground="#000000")
    rad_admin.configure(justify='left')
    rad_admin.configure(text='''Admin''')
    rad_admin.configure(variable = rad_role)
    rad_admin.configure(value = 'a')

#------------------------Button------------------------------  
    but_login = tk.Button(login_window)
    but_login.place(relx=0.389, rely=0.7, height=44, width=127)
    but_login.configure(background="#1089ff")
    but_login.configure(font="-family {Arial} -size 12 -weight bold")
    but_login.configure(foreground="white")
    but_login.configure(text='''Login''')
    but_login.configure(command = login)
    
    but_clear = tk.Button(login_window)
    but_clear.place(relx=0.389, rely=0.8, height=44, width=127)
    but_clear.configure(background="#1089ff")
    but_clear.configure(command = clear)
    but_clear.configure(font="-family {Arial} -size 12 -weight bold")
    but_clear.configure(foreground="white")
    but_clear.configure(text='''Clear''')
    
    login_window.mainloop()
    cursor.close()  
    return None

# if __name__ == '__main__':
#     create_login_wind()