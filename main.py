'''
Eazy Payroll 1.0
DBMS Project Sem 2 by:
    S Gopi
    Kaushik

This is GUI based based application used to document
and manage employee's payroll, actually this only 
documents, maybe next version can manage as well
'''

import login_wind as lw
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
    
    table_list = [('COMPANY'),('BRANCH'),('ADMINISTRATOR'),('EMPLOYEE'),('SALARY'),('USERNAME')]
    
    cursor.execute('select table_name from user_tables')
    exist_table_list = cursor.fetchall()
    exist_table_list = [table_name[0] for table_name in exist_table_list]
    
    if exist_table_list != table_list:
        table_set = [table_name for table_name in table_list if table_name not in exist_table_list]
        table_creation = {'COMPANY':'''create table company (
                                  c_id int primary key,
                                  c_name varchar(15) not null)''',
                      'BRANCH':'''create table branch (
                                  b_id int primary key,
                                  b_name varchar(15) not null,
                                  c_id int not null,
                                  constraint fk_c_id foreign key(c_id) 
                                  references company(c_id) on delete cascade)''', 
                      'ADMINISTRATOR':'''create table administrator (
                                  a_id int primary key,
                                  a_name varchar(15) not null,
                                  phone_no int not null,
                                  b_id int not null,
                                  account_no int not null,
                                  constraint f_b_id foreign key(b_id) 
                                  references branch(b_id) on delete cascade)''', 
                      'EMPLOYEE':'''create table employee (
                                  e_id int primary key,
                                  e_name varchar(15) not null,
                                  department varchar(15) not null,
                                  designation varchar(15) not null,
                                  phone_no int not null,
                                  account_no int not null,
                                  a_id int not null,
                                  constraint f_a_id foreign key(a_id) 
                                  references administrator(a_id) on delete cascade)''', 
                      'SALARY':'''create table salary (
                                  account_no int primary key,
                                  basic int not null,
                                  med_allow int not null,
                                  hra int not null,
                                  ta int not null,
                                  da int not null,
                                  incentive int not null,
                                  a_id int not null,
                                  constraint fk_a_id1 foreign key(a_id) 
                                  references administrator(a_id) on delete cascade)''', 
                      'USERNAME':'''create table username (
                                  id int not null,
                                  password varchar(25) not null,
                                  user_role char(1) not null)'''}
            
        ''' "on delete cascade" is used so that when a record in parent table is deleted 
        all the related/corressponding records in the child table is deleted automatically 
        without separate queries for them, but in this case in wont be useful bcoz when an 
        employee is deleted, there is no reference from employee table at all and 
        we need to delete the records from employee table only. Here, its used only 
        for learning purpose only.'''
        
        for table_name in table_set:
            cursor.execute(table_creation[table_name])
            if table_name == 'COMPANY':
                cursor.execute("insert into company values (1,'Admin Company')")
            elif table_name == 'BRANCH':
                cursor.execute("insert into branch values (1,'Admin Branch',1)")
            elif table_name == 'ADMINISTRATOR':
                cursor.execute("insert into administrator values (1,'Admin',1112223334,1,123)")
            elif table_name == 'USERNAME':
                cursor.execute("insert into username values (1,'123','a')")
            # print('Table created:',table_name)
            
    cursor.close()    
    if con:
        lw.create_login_wind(con)
        con.close()

if __name__ == '__main__':
    connect_database()  