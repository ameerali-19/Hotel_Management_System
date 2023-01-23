import tkinter as tk
from tkinter import ttk
import mysql.connector
from datetime import datetime
from datetime import date
import ttkbootstrap as tb


#Substitute your credentials here
username = "root"
password = "password"

# MySQL connection code
my_db = mysql.connector.connect(
    host="localhost",
    user=username,
    passwd=password,
    database="hms"
)
my_conn = my_db.cursor()

# Create the main window
window = tb.Window(themename="darkly")
window.geometry("1366x768")
window.title("Hotel Management")
logo_path = "D:\Py\HMS\logo.ico"      #Give the absolute path of your logo.ico file here
window.iconbitmap(logo_path)
window.style.configure('my.Treeview', rowheight=25)

# Create the heading frame
heading_frame = tb.Frame(window,bootstyle='dark')
heading_frame.pack(side='top', fill='x')

# Create the heading label
heading_label = tb.Label(heading_frame, text='HOTEL MANAGEMENT SYSTEM', font=('Arial 24 bold underline'),bootstyle='inverse-dark')
heading_label.pack(padx=10, pady=10)

# Create the input frame
input_frame = tk.Frame(window)
input_frame.pack(fill='y', padx=50, pady=50)

# Create the input labels and entry fields
name_label = tb.Label(input_frame, text='Name:', font=('Helvetica', 11))
name_label.grid(row=1, column=1, padx=(200, 20),pady=(10, 10), ipadx=1, ipady=4)
name_entry = tk.Entry(input_frame, font=('Helvetica', 11))
name_entry.grid(row=1, column=2, padx=(20, 0), pady=(10, 10), ipadx=1, ipady=4)

proof_label = tk.Label(input_frame, text='Proof:', font=('Helvetica', 11))
proof_label.grid(row=2, column=1, padx=(200, 20),pady=(10, 10), ipadx=1, ipady=4)
proof_entry = tk.Entry(input_frame, font=('Helvetica', 11))
proof_entry.grid(row=2, column=2, padx=(20, 0),pady=(10, 10), ipadx=1, ipady=4)

checkin_label = tk.Label(input_frame, text='Checkin:', font=('Helvetica', 11))
checkin_label.grid(row=3, column=1, padx=(200, 20),pady=(10, 10), ipadx=1, ipady=4)
checkin_entry = tk.Entry(input_frame, font=('Helvetica', 11))
checkin_entry.grid(row=3, column=2, padx=(20, 0), pady=(10, 10), ipadx=1, ipady=4)
today = date.today()
checkin_entry.insert(0,today)

checkout_label = tk.Label(input_frame, text='Checkout:', font=('Helvetica', 11))
checkout_label.grid(row=4, column=1, padx=(200, 20),pady=(10, 10), ipadx=1, ipady=4)
checkout_entry = tk.Entry(input_frame, font=('Helvetica', 11))
checkout_entry.grid(row=4, column=2, padx=(20, 0), pady=(10, 10), ipadx=1, ipady=4)
checkout_entry.insert(0,today)

room_label = tk.Label(input_frame, text='Room: ', font=('Helvetica', 11))
room_label.grid(row=5, column=1, padx=(200, 20),pady=(10, 10), ipadx=1, ipady=4)
room_entry = tk.Entry(input_frame, font=('Helvetica', 11))
room_entry.grid(row=5, column=2, padx=(20, 0), pady=(10, 10), ipadx=1, ipady=4)

cost_label = tk.Label(input_frame, text='Cost: ', font=('Helvetica', 11))
cost_entry = tk.Entry(input_frame, font=('Helvetica', 11))

status_label = tk.Label(input_frame, text='Status: ', font=('Helvetica', 11))
status_var = tk.StringVar(value="Checked In")
status_entry = ttk.Combobox(input_frame,textvariable=status_var, values=["Checked In", "Checked Out"], font=('Helvetica', 11))

# Create the treeview frame
treeview_frame = tk.Frame(window)
treeview_frame.pack(fill='both')

# Create the treeview
treeview = tb.Treeview(treeview_frame, columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7','c8'], show='headings', bootstyle='dark', style='my.Treeview', height=7)
treeview.column("#1", anchor=tk.CENTER, width=150)
treeview.heading("#1", text="CID")
treeview.column("#2", anchor=tk.CENTER, width=150)
treeview.heading("#2", text="Name")
treeview.column("#3", anchor=tk.CENTER, width=150)
treeview.heading("#3", text="Proof")
treeview.column("#4", anchor=tk.CENTER, width=150)
treeview.heading("#4", text="Checkin")
treeview.column("#5", anchor=tk.CENTER, width=150)
treeview.heading("#5", text="Checkout")
treeview.column("#6", anchor=tk.CENTER, width=150)
treeview.heading("#6", text="Room")
treeview.column("#7", anchor=tk.CENTER, width=150)
treeview.heading("#7", text="Cost")
treeview.column("#8", anchor=tk.CENTER, width=150)
treeview.heading("#8", text="Status")
treeview.pack(padx=10, pady=10, ipadx=1, ipady=4)

# Function to show the customer details in the treeview
def custview():
    for item in treeview.get_children():
        treeview.delete(item)
    my_conn.execute("select * from customer")
    rows = my_conn.fetchall()
    for row in rows:
        treeview.insert("", 0, values=row)

# Function to add customer details
def addcust():
    name = name_entry.get()
    proof = proof_entry.get()
    checkin = checkin_entry.get()
    checkout = checkout_entry.get()
    room = room_entry.get()
    d1 = datetime.strptime(checkin, "%Y-%m-%d")
    d2 = datetime.strptime(checkout, "%Y-%m-%d")
    delta = d2 - d1


    r=[]
    r.append(room)
    value = (r)
    sql = 'select vacancy from room where rno=%s'
    my_conn.execute(sql, value)
    rm=[]
    for x in my_conn:
        rm.append(x)
    temp = rm[0]
    room_vacancy=''.join(temp)

    def room_vacant() :
        l = []
        l.append(name)
        l.append(proof)
        l.append(checkin)
        l.append(checkout)
        l.append(room)
        values = (l)
        sql = 'insert into customer (name,proof,checkin,checkout,room) values (%s,%s,%s,%s,%s)'
        my_conn.execute(sql, values)

        rslt = []
        sql = "select max(cid) from customer"
        my_conn.execute(sql)
        for x in my_conn:
            rslt.append(x)
        max = rslt[0]

        x = []
        x.append(delta.days)
        x.append(room)
        x.extend(max)
        value1 = (x)
        sql = 'update customer set cost=((%s+1)*(select price from room where rno=%s)) where cid=%s'
        my_conn.execute(sql, value1)

        l1 = []
        l1.append("Checked In")
        l1.extend(max)
        value1 = (l1)
        sql = 'update customer set status=%s where cid=%s'
        my_conn.execute(sql, value1)

        y = []
        y.append("Occuppied")
        y.append(room)
        values = (y)
        sql = "update room set vacancy=%s where rno =%s"
        my_conn.execute(sql, values)

        my_db.commit()
        custview()
        clear()
        checkin_entry.insert(0,today)
        checkout_entry.insert(0,today)

    def room_occupied():
        r = tk.Tk()
        r.title('Error')
        r.iconbitmap(logo_path)
        r.geometry('200x100+583+284')
        l = tk.Label(r, text='Room Occuppied')
        l.pack(padx=10, pady=10)
        button = tk.Button(r, text='Try Again', width=20, command=r.destroy)
        button.pack(padx=10, pady=10)
        r.mainloop()

    if room_vacancy == 'Vacant':
        room_vacant()
    else :
        room_occupied()
        return

# Function to clear the input fields
def clear():
    name_entry.delete(0, tk.END)
    proof_entry.delete(0, tk.END)
    checkin_entry.delete(0, tk.END)
    checkout_entry.delete(0, tk.END)
    room_entry.delete(0, tk.END)
    cost_entry.delete(0, tk.END)
    status_entry.delete(0,tk.END)

# Functions of rooms window

#Function to display the room details in the treeview 
def room_display():
    for item in roomtree.get_children():
        roomtree.delete(item)
    my_conn.execute("select * from room")
    rows = my_conn.fetchall()
    for row in rows:
        roomtree.insert("", tk.END, values=row)

#Function to add room details
def add_room():
    def add_room_conf():
        l=[]
        l.append(roomtype.get())
        l.append(roomprize.get())
        l.append("Vacant")
        values=(l)
        sql='insert into room (type,price,vacancy) values (%s,%s,%s)'
        my_conn.execute(sql,values)
        my_db.commit()
        room_display()
        win_addroom.destroy()
    
    win_addroom = tb.Window(title="Insert Room", themename="darkly")
    win_addroom.geometry('250x175+583+284')
    win_addroom.iconbitmap(logo_path)
    f = tk.Frame(win_addroom)
    f.pack()
    l = tk.Label(f, text="Room details", font='Arial 11 bold underline')
    l.grid(row=1, column=1,pady=(10,10))

    l =tk.Label(f, text="Type")
    l.grid(row=2, column=0,pady=(10,10))
    roomtype = tk.Entry(f)
    roomtype.grid(row=2, column=1,pady=(10,10))

    l = tk.Label(f, text="Prize")
    l.grid(row=3, column=0,pady=(10,10))
    roomprize = tk.Entry(f)
    roomprize.grid(row=3, column=1,pady=(10,10))

    bt = tk.Button(f, text="Confirm",command=add_room_conf)
    bt.grid(row=4, column=1, padx=(5, 5), pady=(8, 5))

    win_addroom.mainloop()

#Function to edit room details
def edit_room():
    def edit_room_conf():
        l=[]
        l.append(roomno.get())
        l.append(roomtype.get())
        l.append(roomprice.get())
        l.append(roomvacancy.get())
        l.append(selected_roomno)
        values=(l)
        sql='update room set rno=%s,type=%s,price=%s,vacancy=%s where rno=%s'
        my_conn.execute(sql,values)
        my_db.commit()
        room_display()
        win_editroom.destroy()

    win_editroom = tb.Window(title="Edit Room", themename="darkly")
    win_editroom.geometry('250x250+583+284')
    win_editroom.iconbitmap(logo_path)
    f = tk.Frame(win_editroom)
    f.pack()
    l = tk.Label(f, text="Room details", font='Arial 11 bold underline')
    l.grid(row=1, column=1,pady=(10,10))

    l =tk.Label(f, text="Room no : ")
    l.grid(row=2, column=0,pady=(10,10))
    roomno = tk.Entry(f)
    roomno.insert(0,selected_roomno)
    roomno.grid(row=2, column=1,pady=(10,10))

    l =tk.Label(f, text="Type: ")
    l.grid(row=3, column=0,pady=(10,10))
    roomtype = tk.Entry(f)
    roomtype.insert(0,selected_room_type)
    roomtype.grid(row=3, column=1,pady=(10,10))

    l = tk.Label(f, text="Prize: ")
    l.grid(row=4, column=0,pady=(10,10))
    roomprice = tk.Entry(f)
    roomprice.insert(0,selected_room_price)
    roomprice.grid(row=4, column=1,pady=(10,10))

    l = tk.Label(f, text="Vacancy : ")
    l.grid(row=5, column=0,pady=(10,10))
    roomvacancy = tk.Entry(f)
    roomvacancy.insert(0,selected_room_vacancy)
    roomvacancy.grid(row=5, column=1,pady=(10,10))

    bt = tk.Button(f, text="Confirm",command=edit_room_conf)
    bt.grid(row=6, column=1, padx=(5, 5), pady=(8, 5))

    win_editroom.mainloop()

#Function to delete a room 
def delete_room():
    def delete_room_confirm():
        win.destroy()
        l = []
        l.append(selected_roomno)
        values = (l)
        sql = "delete from room where rno=%s"
        my_conn.execute(sql, values)
        my_db.commit()
        room_display()
    win = tk.Tk()
    win.geometry('400x100+583+284')
    win.title('Delete Room')
    win.iconbitmap(logo_path)
    lab = tk.Label(win, text="Are you sure you want to delete the room ?")
    lab.grid(padx=(2, 0), pady=(10, 10), sticky='W')
    conf = tk.Button(win, text="Delete", width=15, command=delete_room_confirm)
    conf.grid(row=1, column=0, padx=(0, 0), pady=(10, 10))
    canc = tk.Button(win, text="Cancel", width=15, command=win.destroy)
    canc.grid(row=1, column=1, padx=(0, 0), pady=(10, 10))
    win.mainloop()

#Function to create the main room window ( opened when the Room button is clicked)
def roomview():
    roomwindow = tk.Tk()
    roomwindow.geometry('975x400')
    roomwindow.iconbitmap(logo_path)
    roomwindow.title('Rooms')

    main_frame = tk.Frame(roomwindow, bg='white', width=975, height=300)
    main_frame.pack()

    global roomtree
    roomtree = ttk.Treeview(main_frame, column=("c1", "c2", "c3", "c4"), show='headings')
    roomtree.column("#1", anchor=tk.CENTER)
    roomtree.heading("#1", text="Room No")
    roomtree.column("#2", anchor=tk.CENTER)
    roomtree.heading("#2", text="Type")
    roomtree.column("#3", anchor=tk.CENTER)
    roomtree.heading("#3", text="Price")
    roomtree.column("#4", anchor=tk.CENTER)
    roomtree.heading("#4", text="Vacancy")

    roomtree.place(x=90,y=40)

    
    roomtree.bind("<<TreeviewSelect>>", on_roomtree_select)

    room_display()

    footer_frame = tk.Frame(roomwindow, bg='lightgrey', width=975, height=100)
    footer_frame.pack(side='bottom')
    
    addroom = tk.Button(footer_frame, text="Add", width=20, command=add_room)
    addroom.grid(row=1, column=1, padx=(20, 20), pady=(30, 30))

    editroom = tk.Button(footer_frame, text="Edit", width=20, command=edit_room)
    editroom.grid(row=1, column=2, padx=(20, 20), pady=(30, 30))

    deleteroom = tk.Button(footer_frame, text="Delete", width=20, command=delete_room)
    deleteroom.grid(row=1, column=3, padx=(20, 20), pady=(30, 30))

#Function to get the details of the selected room
def on_roomtree_select(event):
    global selected_roomno
    global selected_room_type
    global selected_room_price
    global selected_room_vacancy
    selected_item = roomtree.item(roomtree.selection()[0])
    selected_item_values = selected_item["values"]
    selected_roomno = selected_item_values[0]
    selected_room_type = selected_item_values[1]
    selected_room_price = selected_item_values[2]
    selected_room_vacancy = selected_item_values[3]
    room_entry.delete(0, tk.END)
    room_entry.insert(0,selected_roomno)


# Function to get the details of the selected customer
def on_treeview_select(event):
    global selected_cid
    global selected_name
    global selected_proof
    global selected_checkin
    global selected_checkout
    global selected_rno
    global selected_cost
    global selected_status
    selected_item = treeview.item(treeview.selection()[0])
    selected_item_values = selected_item["values"]
    selected_cid = selected_item_values[0]
    selected_name = selected_item_values[1]
    selected_proof = selected_item_values[2]
    selected_checkin = selected_item_values[3]
    selected_checkout = selected_item_values[4]
    selected_rno = selected_item_values[5]
    selected_cost = selected_item_values[6]
    selected_status = selected_item_values[7]
treeview.bind("<<TreeviewSelect>>", on_treeview_select)

# Function to delete a customer
def delete():
    def delete_confirm():
        win.destroy()
        l = []
        l.append(selected_cid)
        values = (l)
        sql = "delete from customer where cid=%s"
        my_conn.execute(sql, values)
        my_db.commit()
        custview()
    win = tk.Tk()
    win.geometry('400x100+583+284')
    win.title('Delete')
    win.iconbitmap(logo_path)
    lab = tk.Label(win, text="Are you sure you want to delete the customer ?")
    lab.grid(padx=(2, 0), pady=(10, 10), sticky='W')
    conf = tk.Button(win, text="Delete", width=15, command=delete_confirm)
    conf.grid(row=1, column=0, padx=(0, 0), pady=(10, 10))
    canc = tk.Button(win, text="Cancel", width=15, command=win.destroy)
    canc.grid(row=1, column=1, padx=(0, 0), pady=(10, 10))
    win.mainloop()

# Function to checkout a customer
def checkout():
    def checkout_confirm():
        win.destroy()
        l = []
        l.append("Vacant")
        l.append(selected_rno)
        values = (l)
        sql = "update room set vacancy=%s where rno =%s"
        my_conn.execute(sql, values)
        my_db.commit()

        l1 = []
        l1.append("Checked Out")
        l1.append(selected_cid)
        value1 = (l1)
        sql = 'update customer set status=%s where cid=%s'
        my_conn.execute(sql, value1)
        custview()

    win = tk.Tk()
    win.geometry('300x100+583+284')
    win.title('Checkout')
    win.iconbitmap(logo_path)
    lab = tk.Label(win, text="Confirm Checkout ?")
    lab.grid(padx=(2, 0), pady=(10, 10), sticky='W')
    conf = tk.Button(win, text="Confirm", width=15, command=checkout_confirm)
    conf.grid(row=1, column=0, padx=(20, 0), pady=(10, 10))
    canc = tk.Button(win, text="Cancel", width=15, command=win.destroy)
    canc.grid(row=1, column=1, padx=(20, 20), pady=(10, 10))

#Function to edit a customer's details
def edit():
    def editconf():
        l=[]
        l.append(name_entry.get())
        l.append(proof_entry.get())
        l.append(checkin_entry.get())
        l.append(checkout_entry.get())
        l.append(room_entry.get())
        l.append(cost_entry.get())
        l.append(status_entry.get())
        l.append(selected_cid)
        values=(l)
        sql="update customer set name=%s,proof=%s,checkin=%s,checkout=%s,room=%s,cost=%s,status=%s where cid=%s"
        my_conn.execute(sql,values)
        my_db.commit()
        custview()
        clear()
        checkin_entry.insert(0,today)
        checkout_entry.insert(0,today)
        edit_button.configure(text="EDIT CUSTOMER",bootstyle="outline",command=edit)
        cancel_edit_button.grid_remove()
        delete_button.grid(row=5)
        cost_label.grid_remove()
        cost_entry.grid_remove()
        status_label.grid_remove()
        status_entry.grid_remove()
    clear()
    cost_label.grid(row=6, column=1, padx=(200, 20),pady=(10, 10), ipadx=1, ipady=4)
    cost_entry.grid(row=6, column=2, padx=(20, 0), pady=(10, 10), ipadx=1, ipady=4)
    status_label.grid(row=7, column=1, padx=(200, 20),pady=(10, 10), ipadx=1, ipady=4)
    status_entry.grid(row=7, column=2, padx=(20, 0), pady=(10, 10), ipadx=1, ipady=4)
    name_entry.insert(0,selected_name)
    proof_entry.insert(0,selected_proof)
    checkin_entry.insert(0,selected_checkin)
    checkout_entry.insert(0,selected_checkout)
    room_entry.insert(0,selected_rno)
    cost_entry.insert(0,selected_cost)
    status_entry.insert(0,selected_status)
    edit_button.configure(text="CONFIRM EDIT",bootstyle="info,outline",command=editconf)
    cancel_edit_button.grid(row=5, column=0, padx=(0, 0), pady=(10, 10), ipadx=1, ipady=4)
    delete_button.grid(row=6)


def cancel_edit():
    clear()
    checkin_entry.insert(0,today)
    checkout_entry.insert(0,today)
    edit_button.configure(text="EDIT CUSTOMER",bootstyle="outline",command=edit)
    cancel_edit_button.grid_remove()
    delete_button.grid(row=5)
    cost_label.grid_remove()
    cost_entry.grid_remove()
    status_label.grid_remove()
    status_entry.grid_remove()

    
# Create the buttons
checkin_button = tb.Button(input_frame, text='CHECKIN', width=20,bootstyle="success,outline", takefocus=False, command=addcust)
checkin_button.grid(row=1, column=0, padx=(0, 0), pady=(10, 10), ipadx=1, ipady=4)

checkout_button = tb.Button(input_frame, text='CHECKOUT', width=20,bootstyle="danger,outline", takefocus=False, command=checkout)
checkout_button.grid(row=2, column=0, padx=(0, 0), pady=(10, 10), ipadx=1, ipady=4)

rooms_button = tb.Button(input_frame, text='ROOMS', width=20,bootstyle="outline", takefocus=False, command=roomview)
rooms_button.grid(row=3, column=0, padx=(0, 0), pady=(10, 10), ipadx=1, ipady=4)

edit_button = tb.Button(input_frame, text='EDIT CUSTOMER', width=20,bootstyle="outline", takefocus=False, command=edit)
edit_button.grid(row=4, column=0, padx=(0, 0), pady=(10, 10), ipadx=1, ipady=4)

delete_button = tb.Button(input_frame, text='DELETE CUSTOMER', width=20,bootstyle="outline", takefocus=False, command=delete)
delete_button.grid(row=5, column=0, padx=(0, 0), pady=(10, 10), ipadx=1, ipady=4)

cancel_edit_button = tb.Button(input_frame, text='CANCEL EDIT', width=20,bootstyle="info,outline", takefocus=False, command=cancel_edit)

custview()      # Called to initially display the customer details when the window is opened.
window.mainloop()
