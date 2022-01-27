import show_wind as sw
import login_wind as lw
import regex as r
import tkinter as tk
from tkinter import messagebox

def enable_but():
    but_show.configure(state = 'normal')
    
def create_emp_wind(con,eid):
    global but_show
    cursor = con.cursor()    
    emp_window = tk.Tk()

    emp_window.geometry("568x792+515+0")
    emp_window.resizable(0,  0)
    # emp_window.title("Welcome Raghu Verma")
    emp_window.configure(background="#e7eaf6")
    
    emp_img = tk.PhotoImage(file=r"resources\emp.png")
    emp_img_lab = tk.Label(emp_window,image = emp_img)
    emp_img_lab.place(relx=0.333, rely=0.075, height=200, width=204)
    emp_img_lab.configure(background="#e7eaf6")
    emp_window.iconbitmap(r'resources\icon.ico')
    
#------------------------Variables------------------------------  
    newpsw = tk.StringVar()
    conf_newpsw = tk.StringVar()
    
#------------------------Status Label------------------------------ 
    lab_status = tk.Label(emp_window)
    lab_status.place(relx=0.018, rely=0.95, height=22, width=558)
    lab_status.configure(background="#e7eaf6")
    lab_status.configure(font="-family {Arial} -size 10 -weight bold")
    lab_status.configure(foreground="red")
    lab_status.configure(text='''---''')
    
#------------------------Functions------------------------------       
    def exitt():
        emp_window.destroy()
        lw.create_login_wind(con)
    
    def clear():
        newpsw.set('')
        conf_newpsw.set('')
        lab_status.configure(text = '---')
        
    def helpp():
        messagebox.showinfo(
                "How to Update Password",
                '''      
                New password must contain (minimun):
                            8 characters
                            1 uppercase
                            1 lowercase
                            1 number
                            1 special character''')
        
    def show():
        but_show.configure(state = 'disabled')
        sw.create_show_wind(emp_window,con,eid,emp_data[0][1],emp_data[0][5],emp_data[0][6],'emp_wind')    
        # but_show.configure(state = 'normal')  
        # enable_but() #both these methods didnt work, dont know why!
    
    def update_psw():
        newpsw.set(newpsw.get().strip())
        conf_newpsw.set(conf_newpsw.get().strip())
        if newpsw.get() != conf_newpsw.get():
            lab_status.configure(text='Entered passwords do not match')
            return None            
        elif not (r.search('[a-z]+',newpsw.get()) and r.search('[A-Z]+',newpsw.get()) and r.search('[0-9]+',newpsw.get()) and r.search('[^a-zA-Z0-9]+',newpsw.get()) and len(newpsw.get()) >= 8):
            helpp()  
            clear()
            return None
        query = "update username set password = '{}' where id = {} and user_role = 'e'".format(newpsw.get(),emp_data[0][0])
        cursor.execute(query)
        clear()
        lab_status.configure(text='Password updated successfully!')
        return None
    
    # def disable_forced_exit():
        '''just an empty function like this will also disable 
        the window close button on top right corner'''
    #     pass

    def disable_forced_exit():
        messagebox.showinfo(
                "Window Close Button Disabled",
                '''      
                Please Logout properly for safety reasons !!!''') 
    
#------------------------Menu------------------------------   
    menubar = tk.Menu(emp_window)
    emp_window.configure(menu = menubar)
    menubar.add_command(label = 'Help',command = helpp)

#------------------------Labels (Title, show values, password)------------------------------ 
    label_0 = tk.Label(emp_window)
    label_0.place(relx=0.015, rely=0.0, height=50, width=548)
    label_0.configure(background="#e7eaf6")
    label_0.configure(font="-family {Arial} -size 24 -weight bold")
    label_0.configure(foreground="#000000")
    # label_0.configure(text='''Employee : Raghu Verma''')
    label_0.configure(relief = 'solid')

    lab_eid = tk.Label(emp_window)
    lab_eid.place(relx=0.264, rely=0.341, height=20, width=118)
    lab_eid.configure(background="#e7eaf6")
    lab_eid.configure(font="-family {Arial} -size 12 -weight bold")
    lab_eid.configure(foreground="#000000")
    lab_eid.configure(text='''Employee ID :''')

    lab_dept = tk.Label(emp_window)
    lab_dept.place(relx=0.234, rely=0.391, height=22, width=157)
    lab_dept.configure(background="#e7eaf6")
    lab_dept.configure(font="-family {Arial} -size 12 -weight bold")
    lab_dept.configure(foreground="#000000")
    lab_dept.configure(text='''Department :''')

    lab_desig = tk.Label(emp_window)
    lab_desig.place(relx=0.268, rely=0.442, height=22, width=120)
    lab_desig.configure(background="#e7eaf6")
    lab_desig.configure(font="-family {Arial} -size 12 -weight bold")
    lab_desig.configure(foreground="#000000")
    lab_desig.configure(text='''Designation :''')

    lab_phno = tk.Label(emp_window)
    lab_phno.place(relx=0.284, rely=0.492, height=22, width=119)
    lab_phno.configure(background="#e7eaf6")
    lab_phno.configure(font="-family {Arial} -size 12 -weight bold")
    lab_phno.configure(foreground="#000000")
    lab_phno.configure(text='''Phone No :''')

    lab_accno = tk.Label(emp_window)
    lab_accno.place(relx=0.28, rely=0.544, height=21, width=109)
    lab_accno.configure(background="#e7eaf6")
    lab_accno.configure(font="-family {Arial} -size 12 -weight bold")
    lab_accno.configure(foreground="#000000")
    lab_accno.configure(text='''Account No :''')

    lab_aid = tk.Label(emp_window)
    lab_aid.place(relx=0.296, rely=0.597, height=23, width=109)
    lab_aid.configure(background="#e7eaf6")
    lab_aid.configure(font="-family {Arial} -size 12 -weight bold")
    lab_aid.configure(foreground="#000000")
    lab_aid.configure(text='''Admin ID :''')

    lab_adname = tk.Label(emp_window)
    lab_adname.place(relx=0.273, rely=0.653, height=23, width=109)
    lab_adname.configure(background="#e7eaf6")
    lab_adname.configure(font="-family {Arial} -size 12 -weight bold")
    lab_adname.configure(foreground="#000000")
    lab_adname.configure(text='''Admin Name :''')

    lab_eid_show = tk.Label(emp_window)
    lab_eid_show.place(relx=0.511, rely=0.345, height=19, width=128)
    lab_eid_show.configure(background="white")
    lab_eid_show.configure(font="-family {Arial} -size 12")
    lab_eid_show.configure(foreground="#000000")
    # lab_eid_show.configure(text='''id''')

    lab_dept_show = tk.Label(emp_window)
    lab_dept_show.place(relx=0.511, rely=0.396, height=19, width=128)
    lab_dept_show.configure(background="white")
    lab_dept_show.configure(font="-family {Arial} -size 12")
    lab_dept_show.configure(foreground="#000000")
    # lab_dept_show.configure(text='''id''')

    lab_desig_show = tk.Label(emp_window)
    lab_desig_show.place(relx=0.511, rely=0.446, height=19, width=128)
    lab_desig_show.configure(background="white")
    lab_desig_show.configure(font="-family {Arial} -size 12")
    lab_desig_show.configure(foreground="#000000")
    # lab_desig_show.configure(text='''id''')

    lab_phno_show = tk.Label(emp_window)
    lab_phno_show.place(relx=0.511, rely=0.497, height=19, width=128)
    lab_phno_show.configure(background="white")
    lab_phno_show.configure(font="-family {Arial} -size 12")
    lab_phno_show.configure(foreground="#000000")
    # lab_phno_show.configure(text='''id''')

    lab_accno_show = tk.Label(emp_window)
    lab_accno_show.place(relx=0.511, rely=0.548, height=18, width=128)
    lab_accno_show.configure(background="white")
    lab_accno_show.configure(font="-family {Arial} -size 12")
    lab_accno_show.configure(foreground="#000000")
    # lab_accno_show.configure(text='''id''')
    
    lab_aid_show = tk.Label(emp_window)
    lab_aid_show.place(relx=0.511, rely=0.601, height=18, width=128)
    lab_aid_show.configure(background="white")
    lab_aid_show.configure(font="-family {Arial} -size 12")
    lab_aid_show.configure(foreground="#000000")
    # lab_aid_show.configure(text='''id''')

    lab_adname_show = tk.Label(emp_window)
    lab_adname_show.place(relx=0.511, rely=0.657, height=19, width=128)
    lab_adname_show.configure(background="white")
    lab_adname_show.configure(font="-family {Arial} -size 12")
    lab_adname_show.configure(foreground="#000000")
    
    lab_newpsw = tk.Label(emp_window)
    lab_newpsw.place(relx=0.123, rely=0.82, height=19, width=138)
    lab_newpsw.configure(background="#e7eaf6")
    lab_newpsw.configure(font="-family {Arial} -size 12 -weight bold")
    lab_newpsw.configure(foreground="#000000")
    lab_newpsw.configure(text='''New Password :''')

    lab_conf_newpsw = tk.Label(emp_window)
    lab_conf_newpsw.place(relx=0.012, rely=0.876, height=19, width=198)
    lab_conf_newpsw.configure(background="#e7eaf6")
    lab_conf_newpsw.configure(font="-family {Arial} -size 12 -weight bold")
    lab_conf_newpsw.configure(foreground="#000000")
    lab_conf_newpsw.configure(text='''Confirm New Password :''')

#------------------------Entry------------------------------
    entry_newpsw = tk.Entry(emp_window)
    entry_newpsw.place(relx=0.387, rely=0.822, height=20, relwidth=0.289)
    entry_newpsw.configure(background="white")
    entry_newpsw.configure(foreground="#000000")
    entry_newpsw.configure(textvariable = newpsw)

    entry_conf_newpsw = tk.Entry(emp_window)
    entry_conf_newpsw.place(relx=0.387, rely=0.876, height=20, relwidth=0.289)
    entry_conf_newpsw.configure(background="white")
    entry_conf_newpsw.configure(foreground="#000000")
    entry_conf_newpsw.configure(highlightbackground="#d9d9d9")
    entry_conf_newpsw.configure(textvariable = conf_newpsw)

#------------------------Button------------------------------ 
    but_show = tk.Button(emp_window)
    but_show.place(relx=0.29, rely=0.72, height=44, width=97)
    but_show.configure(background="#1089ff")
    but_show.configure(command = show)
    but_show.configure(font="-family {Arial} -size 12 -weight bold")
    but_show.configure(foreground="white")
    but_show.configure(text='''Show''')

    but_logout = tk.Button(emp_window)
    but_logout.place(relx=0.55, rely=0.72, height=44, width=97)
    but_logout.configure(background="#1089ff")
    but_logout.configure(command = exitt)
    but_logout.configure(font="-family {Arial} -size 12 -weight bold")
    but_logout.configure(foreground="white")
    but_logout.configure(text='''Logout''')
    
    but_update_psw = tk.Button(emp_window)
    but_update_psw.place(relx=0.757, rely=0.802, height=40, width=107)
    but_update_psw.configure(background="#1089ff")
    but_update_psw.configure(command = update_psw)
    but_update_psw.configure(font="-family {Arial} -size 12 -weight bold")
    but_update_psw.configure(foreground="white")
    but_update_psw.configure(text='''Update''')

    but_clear = tk.Button(emp_window)
    but_clear.place(relx=0.757, rely=0.87, height=40, width=107)
    but_clear.configure(background="#1089ff")
    but_clear.configure(command = clear)
    but_clear.configure(font="-family {Arial} -size 12 -weight bold")
    but_clear.configure(foreground="white")
    but_clear.configure(text='''Clear''')
    
#------------------------Displaying Preliminary Data----------------------
    query = "select * from employee where e_id = {}".format(eid)
    cursor.execute(query)
    emp_data = cursor.fetchall()
    query = "select a_name from administrator where a_id = {}".format(emp_data[0][6])
    cursor.execute(query)
    admin_data = cursor.fetchall()
    
    emp_window.title('Welcome ' + emp_data[0][1])
    label_0.configure(text='Employee : ' + emp_data[0][1])
    lab_eid_show.configure(text=emp_data[0][0])
    lab_dept_show.configure(text=emp_data[0][2])
    lab_desig_show.configure(text=emp_data[0][3])
    lab_phno_show.configure(text=emp_data[0][4])
    lab_accno_show.configure(text=emp_data[0][5])
    lab_aid_show.configure(text=emp_data[0][6])
    lab_adname_show.configure(text=admin_data[0][0])
    
    '''to disable the window close button on top right corner so that 
    users use only the custom close options defined in the window'''
    emp_window.protocol("WM_DELETE_WINDOW", disable_forced_exit)
    
    '''or we can repurpose the window close button on top right corner and make it run the custom 
    exitt function defined whenever the window close button on top right corner is clicked'''
    # emp_window.protocol("WM_DELETE_WINDOW", exitt)
    
    '''or just use a empty/dummy inline function like this to achieve the same'''
    # emp_window.protocol("WM_DELETE_WINDOW", lambda: 'pass')
    
    '''or disable the complete title bar including icon, title, 
    minimize, maximize and close options'''
    # emp_window.overrideredirect(True)
    
    emp_window.mainloop()
    cursor.close()  
    return None

# if __name__ == '__main__':
#     create_emp_wind()
