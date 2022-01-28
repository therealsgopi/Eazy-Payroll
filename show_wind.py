import tkinter as tk
from tkinter import messagebox
import admin_wind as aw
import emp_wind as ew

def create_show_wind(parent_window,con,eid,ename,accno,aid,emp_win = ''):
    global comp
    cursor = con.cursor()   
    show_window = tk.Toplevel(parent_window)    
    
    show_window.geometry("577x792+476+0")
    show_window.resizable(0,  0)
    show_window.title("Employee Salary Details")
    show_window.configure(background="#e7eaf6")
    
    show_img = tk.PhotoImage(file=r"resources\show.png")
    show_img_lab = tk.Label(show_window,image = show_img)
    show_img_lab.place(relx=0.312, rely=0.09, height=219, width=202) 
    show_img_lab.configure(background="#e7eaf6")
    show_window.iconbitmap(r'resources\icon.ico')
    
#------------------------Functions------------------------------       
    def exitt():
        show_window.destroy()
        if emp_win:
            ew.enable_but()
        else:
            aw.update_emp_current_show_list(eid)
            aw.enable_emp_modification()
    
    def helpp():
        messagebox.showinfo(
                "For Any Queries",
                '''      
                Contact your:
                        Admin
                        Branch
                        Company''')
    
    
    # def disable_forced_exit():
        '''just an empty function like this will also disable 
        the window close button on top right corner'''
    #     pass

    def disable_forced_exit():
        messagebox.showinfo(
                "Window Close Button Disabled",
                '''      
                Please click on Close !!!''') 

#------------------------Menu------------------------------   
    menubar = tk.Menu(show_window)
    show_window.configure(menu = menubar)
    menubar.add_command(label = 'Help',command = helpp)

#------------------------Labels------------------------------ 
    label_0 = tk.Label(show_window)
    label_0.place(relx=0.104, rely=0.013, height=50, width=448)
    label_0.configure(background="#e7eaf6")
    label_0.configure(font="-family {Arial} -size 24 -weight bold")
    label_0.configure(foreground="#000000")
    label_0.configure(text='''Raghu Verma''')
    label_0.configure(relief = 'solid')

    lab_comp = tk.Label(show_window)
    lab_comp.place(relx=0.26, rely=0.391, height=21, width=118)
    lab_comp.configure(background="#e7eaf6")
    lab_comp.configure(font="-family {Arial} -size 12 -weight bold")
    lab_comp.configure(foreground="#000000")
    lab_comp.configure(text='''Company :''')

    lab_branch = tk.Label(show_window)
    lab_branch.place(relx=0.243, rely=0.442, height=21, width=157)
    lab_branch.configure(background="#e7eaf6")
    lab_branch.configure(font="-family {Arial} -size 12 -weight bold")
    lab_branch.configure(highlightcolor="black")
    lab_branch.configure(text='''Branch :''')

    lab_eid = tk.Label(show_window)
    lab_eid.place(relx=0.243, rely=0.492, height=21, width=119)
    lab_eid.configure(background="#e7eaf6")
    lab_eid.configure(font="-family {Arial} -size 12 -weight bold")
    lab_eid.configure(foreground="#000000")
    lab_eid.configure(text='''Employee ID :''')
    
    lab_accno = tk.Label(show_window)
    lab_accno.place(relx=0.26, rely=0.543, height=22, width=109)
    lab_accno.configure(background="#e7eaf6")
    lab_accno.configure(font="-family {Arial} -size 12 -weight bold")
    lab_accno.configure(foreground="#000000")
    lab_accno.configure(text='''Account No :''')
    
    lab_basic = tk.Label(show_window)
    lab_basic.place(relx=0.329, rely=0.593, height=21, width=69)
    lab_basic.configure(background="#e7eaf6")
    lab_basic.configure(font="-family {Arial} -size 12 -weight bold")
    lab_basic.configure(foreground="#000000")
    lab_basic.configure(text='''Basic :''')

    lab_hra = tk.Label(show_window)
    lab_hra.place(relx=0.34, rely=0.644, height=22, width=68)
    lab_hra.configure(background="#e7eaf6")
    lab_hra.configure(font="-family {Arial} -size 12 -weight bold")
    lab_hra.configure(foreground="#000000")
    lab_hra.configure(text='''HRA :''')

    lab_ta = tk.Label(show_window)
    lab_ta.place(relx=0.357, rely=0.694, height=22, width=59)
    lab_ta.configure(background="#e7eaf6")
    lab_ta.configure(font="-family {Arial} -size 12 -weight bold")
    lab_ta.configure(foreground="#000000")
    lab_ta.configure(text='''TA :''')

    lab_da = tk.Label(show_window)
    lab_da.place(relx=0.366, rely=0.745, height=22, width=48)
    lab_da.configure(background="#e7eaf6")
    lab_da.configure(font="-family {Arial} -size 12 -weight bold")
    lab_da.configure(foreground="#000000")
    lab_da.configure(text='''DA :''')
    
    lab_med = tk.Label(show_window)
    lab_med.place(relx=0.3, rely=0.795, height=22, width=89)
    lab_med.configure(background="#e7eaf6")
    lab_med.configure(font="-family {Arial} -size 12 -weight bold")
    lab_med.configure(foreground="#000000")
    lab_med.configure(text='''Medical :''')

    lab_inc = tk.Label(show_window)
    lab_inc.place(relx=0.282, rely=0.846, height=22, width=99)
    lab_inc.configure(background="#e7eaf6")
    lab_inc.configure(font="-family {Arial} -size 12 -weight bold")
    lab_inc.configure(foreground="#000000")
    lab_inc.configure(text='''Incentive :''')

#------------------------Labels (Show)------------------------------     
    lab_comp_show = tk.Label(show_window)
    lab_comp_show.place(relx=0.485, rely=0.391, height=22, width=138)
    lab_comp_show.configure(background="white")
    lab_comp_show.configure(font="-family {Arial} -size 12")
    lab_comp_show.configure(foreground="#000000")
    # lab_comp_show.configure(text='''id''')

    lab_branch_show = tk.Label(show_window)
    lab_branch_show.place(relx=0.485, rely=0.442, height=22, width=138)
    lab_branch_show.configure(background="white")
    lab_branch_show.configure(font="-family {Arial} -size 12")
    lab_branch_show.configure(foreground="#000000")
    # lab_branch_show.configure(text='''id''')

    lab_eid_show = tk.Label(show_window)
    lab_eid_show.place(relx=0.485, rely=0.492, height=22, width=138)
    lab_eid_show.configure(background="white")
    lab_eid_show.configure(font="-family {Arial} -size 12")
    lab_eid_show.configure(foreground="#000000")
    # lab_eid_show.configure(text='''id''')

    lab_accno_show = tk.Label(show_window)
    lab_accno_show.place(relx=0.485, rely=0.543, height=22, width=138)
    lab_accno_show.configure(background="white")
    lab_accno_show.configure(font="-family {Arial} -size 12")
    lab_accno_show.configure(foreground="#000000")
    # lab_accno_show.configure(text='''id''')

    lab_basic_show = tk.Label(show_window)
    lab_basic_show.place(relx=0.485, rely=0.593, height=22, width=138)
    lab_basic_show.configure(background="white")
    lab_basic_show.configure(font="-family {Arial} -size 12")
    lab_basic_show.configure(foreground="#000000")
    # lab_basic_show.configure(text='''id''')

    lab_hra_show = tk.Label(show_window)
    lab_hra_show.place(relx=0.485, rely=0.644, height=22, width=138)
    lab_hra_show.configure(background="white")
    lab_hra_show.configure(font="-family {Arial} -size 12")
    lab_hra_show.configure(foreground="#000000")
    # lab_hra_show.configure(text='''id''')

    lab_ta_show = tk.Label(show_window)
    lab_ta_show.place(relx=0.485, rely=0.694, height=22, width=138)
    lab_ta_show.configure(background="white")
    lab_ta_show.configure(font="-family {Arial} -size 12")
    lab_ta_show.configure(foreground="#000000")
    # lab_ta_show.configure(text='''id''')

    lab_da_show = tk.Label(show_window)
    lab_da_show.place(relx=0.485, rely=0.745, height=21, width=138)
    lab_da_show.configure(background="white")
    lab_da_show.configure(font="-family {Arial} -size 12")
    lab_da_show.configure(foreground="#000000")
    # lab_da_show.configure(text='''id''')

    lab_med_show = tk.Label(show_window)
    lab_med_show.place(relx=0.485, rely=0.795, height=22, width=138)
    lab_med_show.configure(background="white")
    lab_med_show.configure(font="-family {Arial} -size 12")
    lab_med_show.configure(foreground="#000000")
    # lab_med_show.configure(text='''id''')

    lab_inc_show = tk.Label(show_window)
    lab_inc_show.place(relx=0.485, rely=0.846, height=22, width=138)
    lab_inc_show.configure(background="white")
    lab_inc_show.configure(font="-family {Arial} -size 12")
    lab_inc_show.configure(foreground="#000000")
    # lab_inc_show.configure(text='''id''')
    
#------------------------Button------------------------------ 
    but_close = tk.Button(show_window)
    but_close.place(relx=0.433, rely=0.912, height=44, width=107)
    but_close.configure(background="#1089ff")
    but_close.configure(font="-family {Arial} -size 12 -weight bold")
    but_close.configure(foreground="white")
    but_close.configure(text='''Close''')
    but_close.configure(command = exitt)
    
#------------------------Displaying Preliminary Data----------------------
    query = "select * from salary where account_no = {}".format(accno)
    cursor.execute(query)
    sal_data = cursor.fetchall()
    
    query = '''select c_name from company c inner join branch b on c.c_id = b.c_id 
            inner join administrator a on b.b_id = a.b_id where a_id = {}'''.format(aid)
    cursor.execute(query)
    comp = cursor.fetchall()
    
    query = '''select b_name from branch b inner join administrator a 
            on b.b_id = a.b_id where a_id = {}'''.format(aid)
    cursor.execute(query)
    branch = cursor.fetchall()
    
    label_0.configure(text=ename)
    lab_comp_show.configure(text=comp[0][0])
    lab_branch_show.configure(text=branch[0][0])
    lab_eid_show.configure(text=eid)
    lab_accno_show.configure(text=accno)
    lab_basic_show.configure(text=sal_data[0][1])
    lab_hra_show.configure(text=sal_data[0][3])
    lab_ta_show.configure(text=sal_data[0][4])
    lab_da_show.configure(text=sal_data[0][5])
    lab_med_show.configure(text=sal_data[0][2])
    lab_inc_show.configure(text=sal_data[0][6])    
    
    '''to disable the window close button on top right corner so that 
    users use only the custom close options defined in the window'''
    show_window.protocol("WM_DELETE_WINDOW", disable_forced_exit)
    
    '''or we can repurpose the window close button on top right corner and make it run the custom 
    exitt function defined whenever the window close button on top right corner is clicked'''
    # show_window.protocol("WM_DELETE_WINDOW", exitt)
    
    '''or just use a empty/dummy inline function like this to achieve the same'''
    # show_window.protocol("WM_DELETE_WINDOW", lambda: 'pass')
    
    '''or disable the complete title bar including icon, title, 
    minimize, maximize and close options'''
    # show_window.overrideredirect(True)
    
    show_window.mainloop()
    cursor.close()  
    return None

# if __name__ == '__main__':
#     create_show_wind()
