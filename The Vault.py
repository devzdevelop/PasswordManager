from tkinter import *
from tkinter import font
import tkinter as ttk
import psycopg2
import random
import string

# regular functions

def random_password():
    ran_pass = str(''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12)))
    password_entry.delete(0, END)
    password_entry.insert(0, ran_pass)


# database functions

def create():
    conn = psycopg2.connect(dbname="password", user="postgres", password="Password", host="localhost", port="5432")
    curser = conn.cursor()

    curser.execute('''CREATE TABLE passwords(ID SERIAL, Platform Name text, Email text, Username text, Password text);''')
    print('Table created succe.')
    conn.commit()
    conn.close()

def add_data(platform_name, email, username, password):
    conn = psycopg2.connect(dbname="passworddb", user="postgres", password="Leonbrownz123", host="localhost", port="5432")
    curser = conn.cursor()

    query = '''
                INSERT INTO passwords(platform_name, email, username, password) VALUES (%s, %s, %s, %s);
            '''
    curser.execute(query, (platform_name, email, username, password))
    print('Data inserted successfully.')
    conn.commit()  
    conn.close()

def display_all(second_frame):
    conn = psycopg2.connect(dbname="passworddb", user="postgres", password="Leonbrownz123", host="localhost", port="5432")
    curser = conn.cursor()
    query = '''select * from passwords'''
    curser.execute(query)
    row = curser.fetchall()

    listbox = Listbox(second_frame, width=60, height=5)
    listbox.grid(row=2, column=3, sticky="ne")
    for x in row:
        listbox.insert(END, x)
        
    listbox.config(bg='#97114c')

def edit_passwords():
    platform_name = eplatform_name_entry.get()
    username = eusername_entry.get()
    new_password = enew_password_entry.get()

    conn = psycopg2.connect(dbname="passworddb", user="postgres", password="Leonbrownz123", host="localhost", port="5432")
    curser = conn.cursor()

    query = '''
               UPDATE passwords SET password = %s WHERE username = %s AND platform_name = %s;
            '''
    curser.execute(query, (new_password, username, platform_name))
    print('Password changed successfully.')
    conn.commit()  
    conn.close()

def delete_passwords():
    print("entered")
    platform_name = dplatform_name_entry.get()
    username = dusername_entry.get()
    password = dpassword_entry.get()

    conn = psycopg2.connect(dbname="passworddb", user="postgres", password="Leonbrownz123", host="localhost", port="5432")
    curser = conn.cursor()

    query = '''
               DELETE FROM passwords WHERE password = %s AND username = %s AND platform_name = %s;
            '''
    curser.execute(query, (password, username, platform_name))
    print('Password changed successfully.')
    conn.commit()  
    conn.close()

# windows

# view window
def view():
    # view window
    view_window = Toplevel()
    view_window.title("View Passwords")
    view_window.geometry("600x700")

    # main frame config
    main_frame = Frame(view_window, background="#241b20")
    main_frame.columnconfigure((0,1,2,3,4,5,6,), weight=1)
    main_frame.rowconfigure((0,1,2,3,4,5,6), weight=1)

    # second frame config
    second_frame = Frame(main_frame, background="#3e1a26")
    second_frame.columnconfigure((0,1,2,3,4,5,6,7), weight=1)
    second_frame.rowconfigure((0,1,2,3,4,5,6), weight=1)

    # main frame widgets
    main_label = Label(main_frame,text="The Valut - View Passwords", background="#241b20", foreground="#c23e78", font=bold_font)

    # second frame widgets
    instr_Msg = Label(second_frame, text="Your Passwords:", background="#611424", font=font.Font(family="Helvetica", size=12, weight="bold"))
   
    # main frame layout
    main_frame.pack(side="top", expand=True, fill="both")
    main_label.grid(column=3, row=0, sticky="wse", columnspan=1)
    second_frame.grid(row=2, column=2, sticky="nsew", columnspan=3, rowspan=4)

    # second main layout
    instr_Msg.grid(column=3,row=0, sticky="news")
    display_all(second_frame)
    
# add window
def add():
    # add window
    add_window = Toplevel()
    add_window.title("Add Password")
    add_window.geometry("600x700")

    # main frame config
    amain_frame = Frame(add_window, background="#241b20")
    amain_frame.columnconfigure((0,1,2,3,4,5,6,), weight=1)
    amain_frame.rowconfigure((0,1,2,3,4,5,6), weight=1)

    # second frame config
    asub_frame1 = Frame(amain_frame, background="#3e1a26")
    asub_frame1.columnconfigure((0,1,2,3,4,5,6,7), weight=1)
    asub_frame1.rowconfigure((0,1,2,3,4,5,6), weight=1)

    # main frame widgets
    main_label = Label(amain_frame,text="The Valut - Add Password", background="#241b20", foreground="#c23e78", font=bold_font)

    # second frame widgets
    instr_Msg = Label(asub_frame1, text="Enter the information you want to add:", background="#611424", foreground="#000000", font=font.Font(family="Helvetica", size=12, weight="bold"))
    platform_name = Label(asub_frame1, text="Platform Name: ", background="#3e1a26", foreground="#c23e78", font=font.Font(family="Helvetica", size=12, weight="bold"))
    platform_name_entry = Entry(asub_frame1)

    email = Label(asub_frame1, text="Email: ", background="#3e1a26", foreground="#c23e78", font=font.Font(family="Helvetica", size=12, weight="bold"))
    email_entry = Entry(asub_frame1)

    username = Label(asub_frame1, text="Username: ", background="#3e1a26", foreground="#c23e78", font=font.Font(family="Helvetica", size=12, weight="bold"))
    username_entry = Entry(asub_frame1)

    password = Label(asub_frame1, text="Password:", background="#3e1a26", foreground="#c23e78", font=font.Font(family="Helvetica", size=12, weight="bold"))
    global password_entry 
    password_entry= Entry(asub_frame1)
    
    generate_password = Button(asub_frame1, text="Generate Password", command=lambda: random_password(), background="#97114c", foreground="#241b20", font=font.Font(family="Helvetica", size=12, weight="bold"))

    add_info = Button(asub_frame1, text="Add Info", command=lambda: add_data(platform_name_entry.get(), email_entry.get(), username_entry.get(), password_entry.get()), background="#97114c", foreground="#241b20", font=font.Font(family="Helvetica", size=12, weight="bold"))

    # main frame layout
    amain_frame.pack(side="top", expand=True, fill="both")
    main_label.grid(column=3, row=0, sticky="wse", columnspan=1)
    asub_frame1.grid(row=2, column=2, sticky="nsew", columnspan=3, rowspan=4)

    # second main layout
    instr_Msg.grid(column=4,row=0, sticky="news")
    platform_name.grid(row=2, column=3, sticky="ne")
    platform_name_entry.grid(row=2, column=4, sticky="nw", padx=20)

    email.grid(row=3, column=3, sticky="ne")
    email_entry.grid(row=3, column=4, sticky="nw", padx=20)

    username.grid(row=4, column=3, sticky="ne")
    username_entry.grid(row=4, column=4, sticky="nw", padx=20)

    password.grid(row=5, column=3, sticky="ne")
    password_entry.grid(row=5, column=4, sticky="nw", padx=20)
    generate_password.grid(row=5, column=4, sticky="wn", padx=180)

    add_info.grid(row=6, column=4, sticky="n")


# edit window
def edit():
    # edit window
    edit_window = Toplevel()
    edit_window.title("Add Password")
    edit_window.geometry("600x700")

    # main frame config
    emain_frame = Frame(edit_window, background="#241b20")
    emain_frame.columnconfigure((0,1,2,3,4,5,6,), weight=1)
    emain_frame.rowconfigure((0,1,2,3,4,5,6), weight=1)

    # second frame config
    esub_frame1 = Frame(emain_frame, background="#3e1a26")
    esub_frame1.columnconfigure((0,1,2,3,4,5,6,7), weight=1)
    esub_frame1.rowconfigure((0,1,2,3,4,5,6), weight=1)

    # main frame widgets
    main_label = Label(emain_frame,text="The Valut - Edit Password", background="#241b20", foreground="#c23e78", font=bold_font)

    # second frame widgets
    instr_Msg = Label(esub_frame1, text="Change your password here:", background="#611424", foreground="#000000", font=font.Font(family="Helvetica", size=12, weight="bold"))
    global eplatform_name
    eplatform_name = Label(esub_frame1, text="Platform Name: ", background="#3e1a26", foreground="#c23e78", font=font.Font(family="Helvetica", size=12, weight="bold"))
    global eplatform_name_entry
    eplatform_name_entry = Entry(esub_frame1)

    global eusername 
    eusername = Label(esub_frame1, text="Username: ", background="#3e1a26", foreground="#c23e78", font=font.Font(family="Helvetica", size=12, weight="bold"))
    global eusername_entry 
    eusername_entry = Entry(esub_frame1)
    
    global enew_password 
    enew_password = Label(esub_frame1, text="New Password: ", background="#3e1a26", foreground="#c23e78", font=font.Font(family="Helvetica", size=12, weight="bold"))
    global enew_password_entry 
    enew_password_entry = Entry(esub_frame1)
    
    modify_info = Button(esub_frame1, text="Change Password", command= edit_passwords, background="#97114c", foreground="#241b20", font=font.Font(family="Helvetica", size=12, weight="bold"))


    # main frame layout
    emain_frame.pack(side="top", expand=True, fill="both")
    main_label.grid(column=3, row=0, sticky="wse", columnspan=1)
    esub_frame1.grid(row=2, column=2, sticky="nsew", columnspan=3, rowspan=4)

    # second main layout
    instr_Msg.grid(column=4,row=0, sticky="news")
    eplatform_name.grid(row=2, column=3, sticky="ne")
    eplatform_name_entry.grid(row=2, column=4, sticky="nw", padx=20)

    eusername.grid(row=3, column=3, sticky="ne")
    eusername_entry.grid(row=3, column=4, sticky="nw", padx=20)

    enew_password.grid(row=4, column=3, sticky="ne")
    enew_password_entry.grid(row=4, column=4, sticky="nw", padx=20)

    modify_info.grid(row=6, column=4, sticky="n")

# delete window
def delete():
    # delete window
    delete_window = Toplevel()
    delete_window.title("Delete Password")
    delete_window.geometry("600x700")

    # main frame config
    dmain_frame = Frame(delete_window, background="#241b20")
    dmain_frame.columnconfigure((0,1,2,3,4,5,6,), weight=1)
    dmain_frame.rowconfigure((0,1,2,3,4,5,6), weight=1)

    # second frame config
    dsub_frame1 = Frame(dmain_frame, background="#3e1a26")
    dsub_frame1.columnconfigure((0,1,2,3,4,5,6,7), weight=1)
    dsub_frame1.rowconfigure((0,1,2,3,4,5,6), weight=1)

    # main frame widgets
    main_label = Label(dmain_frame,text="The Valut - Delete Password", background="#241b20", foreground="#c23e78", font=bold_font)

    # second frame widgets
    instr_Msg = Label(dsub_frame1, text="Delete your password here:", background="#611424", foreground="#000000", font=font.Font(family="Helvetica", size=12, weight="bold"))
    global dplatform_name
    dplatform_name = Label(dsub_frame1, text="Platform Name: ", background="#3e1a26", foreground="#c23e78", font=font.Font(family="Helvetica", size=12, weight="bold"))
    global dplatform_name_entry
    dplatform_name_entry = Entry(dsub_frame1)

    global dusername 
    dusername = Label(dsub_frame1, text="Username: ", background="#3e1a26", foreground="#c23e78", font=font.Font(family="Helvetica", size=12, weight="bold"))
    global dusername_entry 
    dusername_entry = Entry(dsub_frame1)
    
    global dpassword 
    dpassword = Label(dsub_frame1, text="Password: ", background="#3e1a26", foreground="#c23e78", font=font.Font(family="Helvetica", size=12, weight="bold"))
    global dpassword_entry 
    dpassword_entry = Entry(dsub_frame1)
    
    delete_info = Button(dsub_frame1, text="Delete Password", command= delete_passwords, background="#97114c", foreground="#241b20", font=font.Font(family="Helvetica", size=12, weight="bold"))


    # main frame layout
    dmain_frame.pack(side="top", expand=True, fill="both")
    main_label.grid(column=3, row=0, sticky="wse", columnspan=1)
    dsub_frame1.grid(row=2, column=2, sticky="nsew", columnspan=3, rowspan=4)

    # second main layout
    instr_Msg.grid(column=4,row=0, sticky="news")
    dplatform_name.grid(row=2, column=3, sticky="ne")
    dplatform_name_entry.grid(row=2, column=4, sticky="nw", padx=20)

    dusername.grid(row=3, column=3, sticky="ne")
    dusername_entry.grid(row=3, column=4, sticky="nw", padx=20)

    dpassword.grid(row=4, column=3, sticky="ne")
    dpassword_entry.grid(row=4, column=4, sticky="nw", padx=20)

    delete_info.grid(row=6, column=4, sticky="n")


#run
# main window
root = Tk()
root.title("The Vault")
root.geometry("600x700")

# Create a bold font
bold_font = font.Font(family="Helvetica", size=18, weight="bold")


# main frame config
main_frame = Frame(root, background="#241b20")
main_frame.columnconfigure((0,1,2,3,4,5,6,), weight=1)
main_frame.rowconfigure((0,1,2,3,4,5,6), weight=1)


# main frame widgets
welcome_label = Label(main_frame,text="The Vault - Where All Your Passwords Are Stored 🔒", background="#241b20", foreground="#c23e78", font=bold_font)

# sub frame config
sub_frame1 = Frame(main_frame, background="#3e1a26")
sub_frame1.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)
sub_frame1.rowconfigure((0,1,2,3,4,5,6,7), weight=1)

# sub frame widgets
instr_Msg = Label(sub_frame1, text="Select the appopriate option: ", background="#611424", foreground="#000000", font=font.Font(family="Helvetica", size=12, weight="bold"))
view_passwords = Button(sub_frame1, text="1. View Passwords", command=view, background="#97114c", foreground="#241b20", font=font.Font(family="Helvetica", size=12, weight="bold"))
add_password = Button(sub_frame1, text="2. Add Password", command=add, background="#97114c", foreground="#241b20", font=font.Font(family="Helvetica", size=12, weight="bold"))
edit_password = Button(sub_frame1, text="3. Edit Password", command=edit, background="#97114c", foreground="#241b20", font=font.Font(family="Helvetica", size=12, weight="bold"))
delete_password = Button(sub_frame1, text="4. Delete Password", command=delete, background="#97114c", foreground="#241b20", font=font.Font(family="Helvetica", size=12, weight="bold"))

# main layout
main_frame.pack(side="top", expand=True, fill="both")
welcome_label.grid(column=3, row=0, sticky="wse", columnspan=1)
sub_frame1.grid(column=1, row=2, sticky="nswe", columnspan=5, rowspan=4)

# sub frame layout
instr_Msg.grid(column=4,row=0, columnspan=1, sticky="news")
view_passwords.grid(column=4,row=2, columnspan=1, sticky="news")
add_password.grid(column=4,row=3, columnspan=1, sticky="news")
edit_password.grid(column=4,row=4, columnspan=1, sticky="news")
delete_password.grid(column=4,row=5, columnspan=1, sticky="news")

# run
root.mainloop()


