import admin_wind as aw
import tkinter as tk 
from tkinter import messagebox
    
def create_creup_wind(con,aid,operation,eid_org = 0,ename_org = '',accno_org = 0):
    cursor = con.cursor() 
    creup_window = tk.Tk()

    creup_window.geometry("600x564+417+80")
    creup_window.resizable(0,  0)
    # creup_window.title("Updating Raghu Verma")
    creup_window.configure(background="#e7eaf6")
    
    creup_window.iconbitmap(r'resources\icon.ico')

#------------------------Variables------------------------------ 
    eid = tk.StringVar()
    ename = tk.StringVar()
    dept = tk.StringVar()
    desig = tk.StringVar()
    phno = tk.StringVar()
    accno = tk.StringVar()
    basic = tk.StringVar()
    hra = tk.StringVar()
    ta = tk.StringVar()
    da = tk.StringVar()
    med = tk.StringVar()
    inc = tk.StringVar()
    
#------------------------Status Label------------------------------
    lab_status = tk.Label(creup_window)
    lab_status.place(relx=0.017, rely=0.94, height=21, width=584)
    lab_status.configure(background="#e7eaf6")
    lab_status.configure(font="-family {Arial} -size 10 -weight bold")
    lab_status.configure(foreground="red")
    
#------------------------Functions------------------------------       
    def exitt():
        creup_window.destroy()
        if operation == 'Updation':
            aw.create_admin_wind(con,aid,True)
        else:
            aw.create_admin_wind(con,aid)
        
    def operation_fatal_error():
        messagebox.showinfo(
                "Fatal Error",
                '''      
                Employee {} failed due to unknown reasons! Please try again later'''.format(operation))
        exitt()
                
    def clear():
        ename.set('')
        dept.set('')
        desig.set('')
        phno.set('')
        basic.set('')
        hra.set('')
        ta.set('')
        da.set('')
        med.set('')
        inc.set('')
        lab_status.configure(text = '---')
        
    def helpp():
        if operation == 'Creation':
            messagebox.showinfo(
                "How to Create an Employee",
                '''      
                Enter valid credentials of an
                employee and click Done.
                
                Note: 
                    Employee ID and Account Number are internally
                    generated and cannot be modified!''')
        else:
            messagebox.showinfo(
                "How to Update an Employee",
                '''      
                Modify the credentials of the
                employee and click Done.
                
                Note: 
                    Employee ID and Account Number
                    cannot be modified!''')
    
    def set_new_eid_accno():
        query = "select e_id,account_no from employee"
        cursor.execute(query)
        eid_accno_list = cursor.fetchall()
        eid_list = [tup[0] for tup in eid_accno_list]
        accno_list = [tup[1] for tup in eid_accno_list]
        if eid_accno_list:
            eid.set(max(eid_list) + 1)
            accno.set(max(accno_list) + 1)
        else:
            eid.set(1001)
            accno.set(100000000)
            
    def confirmation():
        title = 'Employee {} Confirmation'.format(operation)
        if operation == 'Creation':
            question = "Do you really want to {} Employee '{}' with ID '{}'?".format(operation[:5]+'e',ename.get(),eid.get())
        else:
            question = "Do you really want to {} Employee with ID '{}'?".format(operation[:5]+'e',eid_org)
        decision = messagebox.askquestion(title,question)
        return decision

    def text_field_verify(text):
        text = list(text)
        for char in text:
            if not (char.isspace() or char.isalpha()):
                return False
        return True
    
    def data_verify():
        ename.set(ename.get().strip())
        dept.set(dept.get().strip())
        desig.set(desig.get().strip())
        phno.set(phno.get().strip())
        basic.set(basic.get().strip())
        hra.set(hra.get().strip())
        ta.set(ta.get().strip())
        da.set(da.get().strip())
        med.set(med.get().strip())
        inc.set(inc.get().strip())
        
        if not all([ename.get(),dept.get(),desig.get(),phno.get(),basic.get(),hra.get(),ta.get(),da.get(),med.get(),inc.get()]):
            lab_status.configure(text = 'Enter all the credentials!!!') 
            return False  
        elif not text_field_verify(ename.get()):
            lab_status.configure(text = 'Enter a Valid Employee Name!!!') 
            return False
        elif not text_field_verify(dept.get()):
            lab_status.configure(text = 'Enter a Valid Department!!!') 
            return False
        elif not text_field_verify(desig.get()):
            lab_status.configure(text = 'Enter a Valid Designation!!!') 
            return False
        elif not (phno.get().isdigit() and 6000000000 <= int(phno.get()) <= 9999999999):
            lab_status.configure(text = 'Enter a Valid Phone Number!!!') 
            return False
        elif not (basic.get().isdigit() and int(basic.get()) >= 100): # no basic salary can be less than 100 rupees
            lab_status.configure(text = 'Enter a Valid Basic Pay which is at least 100 Rupees!!!') 
            return False
        elif not (hra.get().isdigit() and 0 <= int(hra.get()) < int(basic.get())):
            lab_status.configure(text = 'Enter a Valid HRA Amount which does not exceed the Basic Pay!!!') 
            return False
        elif not (ta.get().isdigit() and 0 <= int(ta.get()) < int(basic.get())):
            lab_status.configure(text = 'Enter a Valid TA Amount which does not exceed the Basic Pay!!!') 
            return False
        elif not (da.get().isdigit() and 0 <= int(da.get()) < int(basic.get())):
            lab_status.configure(text = 'Enter a Valid DA Amount which does not exceed the Basic Pay!!!') 
            return False
        elif not (med.get().isdigit() and 0 <= int(med.get()) < int(basic.get())):
            lab_status.configure(text = 'Enter a Valid Medical Allowance which does not exceed the Basic Pay!!!') 
            return False
        elif not (inc.get().isdigit() and 0 <= int(inc.get()) < int(basic.get())):
            lab_status.configure(text = 'Enter a Valid Incentive which does not exceed the Basic Pay!!!') 
            return False
        return True
    
    def create():
        if not data_verify():
            return None
        if confirmation() == 'no':
            lab_status.configure(text='Creation cancelled!')     
            return None
        lab_status.configure(text = 'Creating new employee...')  
        
        try:             
            query = "insert into employee values({},'{}','{}','{}',{},{},{})".format(eid.get(),ename.get(),dept.get(),desig.get(),phno.get(),accno.get(),aid)
            cursor.execute(query)
            query = "insert into salary values({},{},{},{},{},{},{},{})".format(accno.get(),basic.get(),med.get(),hra.get(),ta.get(),da.get(),inc.get(),aid)
            cursor.execute(query)
            query = "insert into username values({},'{}','{}')".format(eid.get(),accno.get(),'e')
            cursor.execute(query)
        except:
            operation_fatal_error()
        
        messagebox.showinfo(
                "Employee Created",
                '''      
                Successfully created New Employee '{}' with ID '{}'!!! '''.format(ename.get(),eid.get()))
        exitt()
    
    def update():
        if not data_verify():
            return None
        if confirmation() == 'no':
            lab_status.configure(text='Updation cancelled!')     
            return None
        lab_status.configure(text = 'Updating employee...')                

        try:
            query = "update employee set e_name = '{}' where e_id = {}".format(ename.get(),eid_org)
            cursor.execute(query)
            query = "update employee set department = '{}' where e_id = {}".format(dept.get(),eid_org)
            cursor.execute(query)
            query = "update employee set designation = '{}' where e_id = {}".format(desig.get(),eid_org)
            cursor.execute(query)
            query = "update employee set phone_no = {} where e_id = {}".format(phno.get(),eid_org)
            cursor.execute(query)
            query = "update salary set basic = {} where account_no = {}".format(basic.get(),accno_org)
            cursor.execute(query)        
            query = "update salary set med_allow = {} where account_no = {}".format(med.get(),accno_org)
            cursor.execute(query)        
            query = "update salary set hra = {} where account_no = {}".format(hra.get(),accno_org)
            cursor.execute(query)        
            query = "update salary set ta = {} where account_no = {}".format(ta.get(),accno_org)
            cursor.execute(query)        
            query = "update salary set da = {} where account_no = {}".format(da.get(),accno_org)
            cursor.execute(query)    
            query = "update salary set incentive = {} where account_no = {}".format(inc.get(),accno_org)
            cursor.execute(query)        
        except:
            operation_fatal_error()
        
        messagebox.showinfo(
                "Employee Updated",
                '''      
                Successfully Updated Employee with ID '{}' !!!'''.format(eid_org))
        exitt()
    
#------------------------Menu------------------------------   
    menubar = tk.Menu(creup_window)
    creup_window.configure(menu = menubar)
    menubar.add_command(label = 'Help',command = helpp)
    
#------------------------Labels------------------------------  
    label_0 = tk.Label(creup_window)
    label_0.place(relx=0.01, rely=0.035, height=50, width=585)
    label_0.configure(background="#e7eaf6")
    label_0.configure(font="-family {Arial} -size 24 -weight bold")
    label_0.configure(foreground="#000000")
    # label_0.configure(text='Employee: ' + 'Raghu Verma')
    label_0.configure(relief = 'solid')

    lab_eid = tk.Label(creup_window)
    lab_eid.place(relx=0.075, rely=0.205, height=21, width=124)
    lab_eid.configure(background="#e7eaf6")
    lab_eid.configure(font="-family {Arial} -size 12 -weight bold")
    lab_eid.configure(foreground="#000000")
    lab_eid.configure(text='''Employee ID :''')

    lab_ename = tk.Label(creup_window)
    lab_ename.place(relx=0.0201, rely=0.304, height=21, width=164)
    lab_ename.configure(background="#e7eaf6")
    lab_ename.configure(font="-family {Arial} -size 12 -weight bold")
    lab_ename.configure(foreground="#000000")
    lab_ename.configure(text='''Employee Name :''')

    lab_dept = tk.Label(creup_window)
    lab_dept.place(relx=0.078, rely=0.392, height=21, width=124)
    lab_dept.configure(background="#e7eaf6")
    lab_dept.configure(font="-family {Arial} -size 12 -weight bold")
    lab_dept.configure(foreground="#000000")
    lab_dept.configure(text='''Department :''')

    lab_desig = tk.Label(creup_window)
    lab_desig.place(relx=0.078, rely=0.483, height=22, width=124)
    lab_desig.configure(background="#e7eaf6")
    lab_desig.configure(font="-family {Arial} -size 12 -weight bold")
    lab_desig.configure(foreground="#000000")
    lab_desig.configure(text='''Designation :''')

    lab_phno = tk.Label(creup_window)
    lab_phno.place(relx=0.096, rely=0.577, height=21, width=114)
    lab_phno.configure(background="#e7eaf6")
    lab_phno.configure(font="-family {Arial} -size 12 -weight bold")
    lab_phno.configure(foreground="#000000")
    lab_phno.configure(text='''Phone No :''')

    lab_accno = tk.Label(creup_window)
    lab_accno.place(relx=0.083, rely=0.665, height=22, width=114)
    lab_accno.configure(background="#e7eaf6")
    lab_accno.configure(font="-family {Arial} -size 12 -weight bold")
    lab_accno.configure(foreground="#000000")
    lab_accno.configure(text='''Account No :''')
    
    lab_basic = tk.Label(creup_window)
    lab_basic.place(relx=0.543, rely=0.205, height=21, width=124)
    lab_basic.configure(background="#e7eaf6")
    lab_basic.configure(font="-family {Arial} -size 12 -weight bold")
    lab_basic.configure(foreground="#000000")
    lab_basic.configure(text='''Basic :''')

    lab_hra = tk.Label(creup_window)
    lab_hra.place(relx=0.515, rely=0.304, height=21, width=164)
    lab_hra.configure(background="#e7eaf6")
    lab_hra.configure(font="-family {Arial} -size 12 -weight bold")
    lab_hra.configure(foreground="#000000")
    lab_hra.configure(text='''HRA :''')

    lab_ta = tk.Label(creup_window)
    lab_ta.place(relx=0.56, rely=0.392, height=21, width=124)
    lab_ta.configure(background="#e7eaf6")
    lab_ta.configure(font="-family {Arial} -size 12 -weight bold")
    lab_ta.configure(foreground="#000000")
    lab_ta.configure(text='''TA :''')

    lab_da = tk.Label(creup_window)
    lab_da.place(relx=0.56, rely=0.483, height=22, width=124)
    lab_da.configure(background="#e7eaf6")
    lab_da.configure(font="-family {Arial} -size 12 -weight bold")
    lab_da.configure(foreground="#000000")
    lab_da.configure(text='''DA :''')

    lab_med = tk.Label(creup_window)
    lab_med.place(relx=0.456, rely=0.577, height=21, width=214)
    lab_med.configure(background="#e7eaf6")
    lab_med.configure(font="-family {Arial} -size 12 -weight bold")
    lab_med.configure(foreground="#000000")
    lab_med.configure(text='''Medical :''')

    lab_inc = tk.Label(creup_window)
    lab_inc.place(relx=0.53, rely=0.665, height=22, width=114)
    lab_inc.configure(background="#e7eaf6")
    lab_inc.configure(font="-family {Arial} -size 12 -weight bold")
    lab_inc.configure(foreground="#000000")
    lab_inc.configure(text='''Incentive :''')

#------------------------Entry------------------------------
    lab_eid = tk.Label(creup_window)# Label to show Employee ID
    lab_eid.place(relx=0.280, rely=0.205, height=20, relwidth=0.223)
    lab_eid.configure(background="#e7eaf6")
    lab_eid.configure(font="-family {Arial} -size 12 -weight bold")
    lab_eid.configure(foreground="#000000")
    lab_eid.configure(textvariable = eid)
    
    entry_ename = tk.Entry(creup_window)
    entry_ename.place(relx=0.280, rely=0.304, height=20, relwidth=0.223)
    entry_ename.configure(background="white")
    entry_ename.configure(foreground="#000000")
    entry_ename.configure(textvariable = ename)

    entry_dept = tk.Entry(creup_window)
    entry_dept.place(relx=0.280, rely=0.397, height=20, relwidth=0.223)
    entry_dept.configure(background="white")
    entry_dept.configure(foreground="#000000")
    entry_dept.configure(textvariable = dept)

    entry_desig = tk.Entry(creup_window)
    entry_desig.place(relx=0.280, rely=0.483, height=20, relwidth=0.223)
    entry_desig.configure(background="white")
    entry_desig.configure(foreground="#000000")
    entry_desig.configure(textvariable = desig)

    entry_phno = tk.Entry(creup_window)
    entry_phno.place(relx=0.280, rely=0.575, height=20, relwidth=0.223)
    entry_phno.configure(background="white")
    entry_phno.configure(foreground="#000000")
    entry_phno.configure(textvariable = phno)
    
    lab_accno = tk.Label(creup_window)# Label to show Employee Account Number
    lab_accno.place(relx=0.280, rely=0.665, height=20, width=134)
    lab_accno.configure(background="#e7eaf6")
    lab_accno.configure(font="-family {Arial} -size 12 -weight bold")
    lab_accno.configure(foreground="#000000")
    lab_accno.configure(textvariable = accno)
    
    entry_basic = tk.Entry(creup_window)
    entry_basic.place(relx=0.704, rely=0.205, height=20, relwidth=0.223)
    entry_basic.configure(background="white")
    entry_basic.configure(foreground="#000000")
    entry_basic.configure(textvariable = basic)
    
    entry_hra = tk.Entry(creup_window)
    entry_hra.place(relx=0.704, rely=0.304, height=20, relwidth=0.223)
    entry_hra.configure(background="white")
    entry_hra.configure(foreground="#000000")
    entry_hra.configure(textvariable = hra)

    entry_ta = tk.Entry(creup_window)
    entry_ta.place(relx=0.704, rely=0.397, height=20, relwidth=0.223)
    entry_ta.configure(background="white")
    entry_ta.configure(foreground="#000000")
    entry_ta.configure(textvariable = ta)

    entry_da = tk.Entry(creup_window)
    entry_da.place(relx=0.704, rely=0.483, height=20, relwidth=0.223)
    entry_da.configure(background="white")
    entry_da.configure(foreground="#000000")
    entry_da.configure(textvariable = da)
    
    entry_med = tk.Entry(creup_window)
    entry_med.place(relx=0.704, rely=0.575, height=20, relwidth=0.223)
    entry_med.configure(background="white")
    entry_med.configure(foreground="#000000")
    entry_med.configure(textvariable = med)
    
    entry_inc = tk.Entry(creup_window)
    entry_inc.place(relx=0.704, rely=0.665, height=20, width=134)
    entry_inc.configure(background="white")
    entry_inc.configure(foreground="#000000")
    entry_inc.configure(textvariable = inc)
    
#------------------------Button------------------------------ 
    but_creup = tk.Button(creup_window)
    but_creup.place(relx=0.167, rely=0.798, height=44, width=107)
    but_creup.configure(background="#1089ff")
    # but_creup.configure(command = update)
    but_creup.configure(font="-family {Arial} -size 12 -weight bold")
    but_creup.configure(foreground="white")
    # but_creup.configure(text='''CreUp''')

    but_clear = tk.Button(creup_window)
    but_clear.place(relx=0.417, rely=0.798, height=44, width=107)
    but_clear.configure(background="#1089ff")
    but_clear.configure(command = clear)
    but_clear.configure(font="-family {Arial} -size 12 -weight bold")
    but_clear.configure(foreground="white")
    but_clear.configure(text='''Clear''')

    but_cancel = tk.Button(creup_window)
    but_cancel.place(relx=0.667, rely=0.798, height=44, width=97)
    but_cancel.configure(background="#1089ff")
    but_cancel.configure(command = exitt)
    but_cancel.configure(font="-family {Arial} -size 12 -weight bold")
    but_cancel.configure(foreground="white")
    but_cancel.configure(text='''Cancel''')
    
#-----------------Setting Window Function and Displaying Preliminary Data-----------------
    if operation == 'Creation':
        creup_window.title("Creating New Employee")
        label_0.configure(text='New Employee')
        but_creup.configure(text='Create')
        but_creup.configure(command = create)
        lab_status.configure(text='''Employee ID and Account Number are internally generated and cannot be modified''')
        set_new_eid_accno()
    else:
        creup_window.title("Updating " + ename_org)
        label_0.configure(text='Employee : ' + ename_org)
        but_creup.configure(text='Update')
        but_creup.configure(command = update)
        lab_status.configure(text='''Employee ID and Account Number cannot be modified''')
        
        query = "select department,designation,phone_no from employee where e_id = {}".format(eid_org)
        cursor.execute(query)
        emp_data = cursor.fetchall()
        
        query = "select * from salary where account_no = {}".format(accno_org)
        cursor.execute(query)
        emp_sal_data = cursor.fetchall()
        
        eid.set(eid_org)
        ename.set(ename_org)
        dept.set(emp_data[0][0])
        desig.set(emp_data[0][1])
        phno.set(emp_data[0][2])
        accno.set(accno_org)
        basic.set(emp_sal_data[0][1])
        med.set(emp_sal_data[0][2])
        hra.set(emp_sal_data[0][3])
        ta.set(emp_sal_data[0][4])
        da.set(emp_sal_data[0][5])
        inc.set(emp_sal_data[0][6])

    '''to disable the window close button on top right corner so that 
    users use only the custom close options defined in the window'''
    creup_window.protocol("WM_DELETE_WINDOW", disable_forced_exit)
    
    '''or we can repurpose the window close button on top right corner and make it run the custom 
    exitt function defined whenever the window close button on top right corner is clicked'''
    # creup_window.protocol("WM_DELETE_WINDOW", exitt)
    
    '''or just use a empty/dummy inline function like this to achieve the same'''
    # creup_window.protocol("WM_DELETE_WINDOW", lambda: 'pass')
    
    '''or disable the complete title bar including icon, title, 
    minimize, maximize and close options'''
    # creup_window.overrideredirect(True)
    
    creup_window.mainloop()
    cursor.close()  
    return None

# if __name__ == '__main__':
#     create_creup_wind()
