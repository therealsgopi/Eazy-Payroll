import show_wind as sw
import login_wind as lw
import creup_wind as cuw
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk


        
def create_admin_wind(con,aid,clear_emp_data = False):
    global emp_current_show_list,but_create,but_update,but_delete
    cursor = con.cursor()   
    admin_window = tk.Tk()

    admin_window.geometry("641x772+442+0")
    admin_window.resizable(0,  0)
    # admin_window.title("Welcome John")
    admin_window.configure(background="#e7eaf6")
    
    admin_img = tk.PhotoImage(file=r"resources\admin.png")
    admin_img_lab = tk.Label(admin_window,image = admin_img)
    admin_img_lab.place(relx=0.343, rely=0.088, height=205, width=205)
    admin_img_lab.configure(background="#e7eaf6")
    admin_window.iconbitmap(r'resources\icon.ico')
    
#------------------------Variables------------------------------  
    search = tk.StringVar()
    rad_search = tk.StringVar()
    combo_sel = tk.StringVar()
    emp_current_show_list = []

#------------------------Status Label------------------------------
    lab_status = tk.Label(admin_window)
    lab_status.place(relx=0.019, rely=0.96, height=22, width=618)
    lab_status.configure(background="#e7eaf6")
    lab_status.configure(font="-family {Arial} -size 10 -weight bold")
    lab_status.configure(foreground="red")
    lab_status.configure(text='''---''')

# ------------------------Combobox-------------------------    
    combo_results = ttk.Combobox(admin_window)
    combo_results.place(relx=0.322, rely=0.644, relheight=0.032, relwidth=0.372)
    combo_results.configure(foreground="#000000")
    combo_results.configure(font="-family {Arial} -size 10")
    combo_results.configure(background="#e7eaf6")
    combo_data()  
    combo_results.configure(textvariable = combo_sel)
    # combo_results.configure(postcommand = combo_update)
    combo_results.current(0)
    combo_results.bind("<<ComboboxSelected>>", combo_selection)
    combo_results['state'] = 'readonly'

#------------------------Menu------------------------------   
    menubar = tk.Menu(admin_window)
    admin_window.configure(menu = menubar)
    menubar.add_command(label="Help",command = helpp)

#------------------------Labels------------------------------ 
    label_0 = tk.Label(admin_window)
    label_0.place(relx=0.062, rely=0.01, height=48, width=568)
    label_0.configure(background="#e7eaf6")
    label_0.configure(font="-family {Arial} -size 24 -weight bold")
    label_0.configure(foreground="#000000")
    label_0.configure(text='''Admin : Raghu Prasad''')

    lab_comp = tk.Label(admin_window)
    lab_comp.place(relx=0.078, rely=0.404, height=22, width=109)
    lab_comp.configure(background="#e7eaf6")
    lab_comp.configure(font="-family {Arial} -size 12 -weight bold")
    lab_comp.configure(foreground="#000000")
    lab_comp.configure(text='''Company :''')

    lab_branch = tk.Label(admin_window)
    lab_branch.place(relx=0.516, rely=0.404, height=22, width=109)
    lab_branch.configure(background="#e7eaf6")
    lab_branch.configure(font="-family {Arial} -size 12 -weight bold")
    lab_branch.configure(foreground="#000000")
    lab_branch.configure(text='''Branch :''')

    lab_aid = tk.Label(admin_window)
    lab_aid.place(relx=0.078, rely=0.455, height=22, width=109)
    lab_aid.configure(background="#e7eaf6")
    lab_aid.configure(font="-family {Arial} -size 12 -weight bold")
    lab_aid.configure(foreground="#000000")
    lab_aid.configure(text='''Admin ID :''')
    
    lab_ad_phno = tk.Label(admin_window)
    lab_ad_phno.place(relx=0.515, rely=0.455, height=22, width=109)
    lab_ad_phno.configure(background="#e7eaf6")
    lab_ad_phno.configure(font="-family {Arial} -size 12 -weight bold")
    lab_ad_phno.configure(foreground="#000000")
    lab_ad_phno.configure(text='''Phone No :''')

    lab_search = tk.Label(admin_window)
    lab_search.place(relx=0.125, rely=0.53, height=22, width=169)
    lab_search.configure(background="#e7eaf6")
    lab_search.configure(font="-family {Arial} -size 12 -weight bold")
    lab_search.configure(foreground="#000000")
    lab_search.configure(text='''Employee ID/Name :''')

    lab_eid_name = tk.Label(admin_window)
    lab_eid_name.place(relx=0.055, rely=0.707, height=21, width=155)
    lab_eid_name.configure(background="#e7eaf6")
    lab_eid_name.configure(font="-family {Arial} -size 12 -weight bold")
    lab_eid_name.configure(foreground="#000000")
    lab_eid_name.configure(anchor = 'e')
    lab_eid_name.configure(text='''Employee ID :''')
    
    lab_dept = tk.Label(admin_window)
    lab_dept.place(relx=0.12, rely=0.745, height=23, width=120)
    lab_dept.configure(background="#e7eaf6")
    lab_dept.configure(font="-family {Arial} -size 12 -weight bold")
    lab_dept.configure(foreground="#000000")
    lab_dept.configure(text='''Department :''')

    lab_desig = tk.Label(admin_window)
    lab_desig.place(relx=0.119, rely=0.782, height=22, width=118)
    lab_desig.configure(background="#e7eaf6")
    lab_desig.configure(font="-family {Arial} -size 12 -weight bold")
    lab_desig.configure(foreground="#000000")
    lab_desig.configure(text='''Designation :''')

    lab_phno = tk.Label(admin_window)
    lab_phno.place(relx=0.577, rely=0.707, height=21, width=109)
    lab_phno.configure(background="#e7eaf6")
    lab_phno.configure(font="-family {Arial} -size 12 -weight bold")
    lab_phno.configure(foreground="#000000")
    lab_phno.configure(text='''Phone No :''')
    
    lab_accno = tk.Label(admin_window)
    lab_accno.place(relx=0.568, rely=0.745, height=23, width=109)
    lab_accno.configure(background="#e7eaf6")
    lab_accno.configure(font="-family {Arial} -size 12 -weight bold")
    lab_accno.configure(foreground="#000000")
    lab_accno.configure(text='''Account No :''')
    
    lab_basic = tk.Label(admin_window)
    lab_basic.place(relx=0.63, rely=0.782, height=22, width=77)
    lab_basic.configure(background="#e7eaf6")
    lab_basic.configure(font="-family {Arial} -size 12 -weight bold")
    lab_basic.configure(foreground="#000000")
    lab_basic.configure(text='''Basic :''')
    
#------------------------Labels (show)------------------------------ 
    lab_comp_show = tk.Label(admin_window)
    lab_comp_show.place(relx=0.25, rely=0.404, height=22, width=155)
    lab_comp_show.configure(background="white")
    lab_comp_show.configure(font="-family {Arial} -size 12")
    lab_comp_show.configure(foreground="#000000")
    # lab_comp_show.configure(text='''id''')

    lab_branch_show = tk.Label(admin_window)
    lab_branch_show.place(relx=0.671, rely=0.404, height=22, width=155)
    lab_branch_show.configure(background="white")
    lab_branch_show.configure(font="-family {Arial} -size 12")
    lab_branch_show.configure(foreground="#000000")
    # lab_branch_show.configure(text='''id''')

    lab_aid_show = tk.Label(admin_window)
    lab_aid_show.place(relx=0.25, rely=0.455, height=23, width=158)
    lab_aid_show.configure(background="white")
    lab_aid_show.configure(font="-family {Arial} -size 12")
    lab_aid_show.configure(foreground="#000000")
    # lab_aid_show.configure(text='''id''')

    lab_ad_phno_show = tk.Label(admin_window)
    lab_ad_phno_show.place(relx=0.671, rely=0.455, height=23, width=158)
    lab_ad_phno_show.configure(background="white")
    lab_ad_phno_show.configure(font="-family {Arial} -size 12")
    lab_ad_phno_show.configure(foreground="#000000")
    # lab_ad_phno_show.configure(text='''id''')
    
    lab_eid_name_show = tk.Label(admin_window)
    lab_eid_name_show.place(relx=0.312, rely=0.707, height=21, width=128)
    lab_eid_name_show.configure(background="white")
    lab_eid_name_show.configure(font="-family {Arial} -size 12")
    lab_eid_name_show.configure(foreground="#000000")
    
    lab_dept_show = tk.Label(admin_window)
    lab_dept_show.place(relx=0.312, rely=0.745, height=22, width=128)
    lab_dept_show.configure(background="white")
    lab_dept_show.configure(font="-family {Arial} -size 12")
    lab_dept_show.configure(foreground="#000000")

    lab_desig_show = tk.Label(admin_window)
    lab_desig_show.place(relx=0.312, rely=0.782, height=22, width=128)
    lab_desig_show.configure(background="white")
    lab_desig_show.configure(font="-family {Arial} -size 12")
    lab_desig_show.configure(foreground="#000000")

    lab_phno_show = tk.Label(admin_window)
    lab_phno_show.place(relx=0.749, rely=0.707, height=21, width=128)
    lab_phno_show.configure(background="white")
    lab_phno_show.configure(font="-family {Arial} -size 12")
    lab_phno_show.configure(foreground="#000000")

    lab_accno_show = tk.Label(admin_window)
    lab_accno_show.place(relx=0.749, rely=0.745, height=23, width=128)
    lab_accno_show.configure(background="white")
    lab_accno_show.configure(font="-family {Arial} -size 12")
    lab_accno_show.configure(foreground="#000000")

    lab_basic_show = tk.Label(admin_window)
    lab_basic_show.place(relx=0.749, rely=0.782, height=22, width=128)
    lab_basic_show.configure(background="white")
    lab_basic_show.configure(font="-family {Arial} -size 12")
    lab_basic_show.configure(foreground="#000000")

#------------------------Entry------------------------------ 
    entry_search = tk.Entry(admin_window)
    entry_search.place(relx=0.406, rely=0.53, height=20, relwidth=0.24)
    entry_search.configure(background="white")
    entry_search.configure(foreground="#000000")
    entry_search.configure(textvariable = search)
    
#------------------------Radio Button------------------------------  
    rad_eid = tk.Radiobutton(admin_window)
    rad_eid.place(relx=0.203, rely=0.582, relheight=0.031, relwidth=0.22)
    rad_eid.configure(background="#e7eaf6")
    rad_eid.configure(font="-family {Arial} -size 12 -weight bold")
    rad_eid.configure(foreground="#000000")
    rad_eid.configure(justify='left')
    rad_eid.configure(text='''ID''')
    rad_eid.configure(variable = rad_search)
    rad_eid.configure(value = 'ID')

    rad_ename = tk.Radiobutton(admin_window)
    rad_ename.place(relx=0.468, rely=0.582, relheight=0.031, relwidth=0.172)
    rad_ename.configure(background="#e7eaf6")
    rad_ename.configure(font="-family {Arial} -size 12 -weight bold")
    rad_ename.configure(foreground="#000000")
    rad_ename.configure(justify='left')
    rad_ename.configure(text='''Name''')
    rad_ename.configure(variable = rad_search)
    rad_ename.configure(value = 'Name')
    
#------------------------Button------------------------------ 
    but_search = tk.Button(admin_window)
    but_search.place(relx=0.733, rely=0.556, height=36, width=97)
    but_search.configure(background="#1089ff")
    but_search.configure(font="-family {Arial} -size 12 -weight bold")
    but_search.configure(foreground="white")
    but_search.configure(text='''Search''')
    but_search.configure(command = search_but)
    
    but_create = tk.Button(admin_window)
    but_create.place(relx=0.187, rely=0.833, height=36, width=107)
    but_create.configure(background="#1089ff")
    but_create.configure(font="-family {Arial} -size 12 -weight bold")
    but_create.configure(foreground="white")
    but_create.configure(text='''Create''')
    but_create.configure(command = create)
    
    but_update = tk.Button(admin_window)
    but_update.place(relx=0.421, rely=0.833, height=36, width=107)
    but_update.configure(background="#1089ff")
    but_update.configure(font="-family {Arial} -size 12 -weight bold")
    but_update.configure(foreground="white")
    but_update.configure(text='''Update''')
    but_update.configure(command = update)
    
    but_delete = tk.Button(admin_window)
    but_delete.place(relx=0.655, rely=0.833, height=36, width=107)
    but_delete.configure(background="#1089ff")
    but_delete.configure(font="-family {Arial} -size 12 -weight bold")
    but_delete.configure(foreground="white")
    but_delete.configure(text='''Delete''')
    but_delete.configure(command = delete)

    but_clear = tk.Button(admin_window)
    but_clear.place(relx=0.187, rely=0.896, height=36, width=107)
    but_clear.configure(background="#1089ff")
    but_clear.configure(font="-family {Arial} -size 12 -weight bold")
    but_clear.configure(foreground="white")
    but_clear.configure(text='''Clear''')
    but_clear.configure(command = clear)
    
    but_show = tk.Button(admin_window)
    but_show.place(relx=0.421, rely=0.896, height=36, width=107)
    but_show.configure(background="#1089ff")
    but_show.configure(font="-family {Arial} -size 12 -weight bold")
    but_show.configure(foreground="white")
    but_show.configure(text='''Show''')
    but_show.configure(command = show)
    
    but_logout = tk.Button(admin_window)
    but_logout.place(relx=0.655, rely=0.896, height=36, width=107)
    but_logout.configure(background="#1089ff")
    but_logout.configure(font="-family {Arial} -size 12 -weight bold")
    but_logout.configure(foreground="white")
    but_logout.configure(text='''Logout''') 
    but_logout.configure(command = logout)
    


    admin_window.mainloop()
    cursor.close()  
    return None

# if __name__ == '__main__':
#     create_admin_wind()





