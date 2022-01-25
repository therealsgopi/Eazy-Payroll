'''
Eazy Payroll 1.0

This is GUI based based application used to document
and manage employee's payroll, actually this only 
documents, maybe next version can manage as well
'''

import tkinter as tk
from tkinter import messagebox
import cx_Oracle as o

# ----------------Establishing DB Connection-------------------
def connect_database():
    try:
        con = o.connect('C##dbms/project@localhost')
        # username: C##dbms 
        # password: project 
    except:
        db_error_window = tk.Tk()
        messagebox.showinfo(
                'Oracle DB Error',
        '''         Oracle DB not installed or 
        Used Oracle DB Username or Password is wrong!
              Contact developers for Support.''')
        db_error_window.destroy()
        return None
    
    con.autocommit = True
    cursor = con.cursor()

if __name__ == '__main__':
    connect_database()
    