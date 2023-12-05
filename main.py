import tkinter as tk
from PIL import Image, ImageTk 
import os
from tkinter import ttk
from tkinter import messagebox
from time import sleep
from db import *
from decimal import Decimal


app = tk.Tk()
app.title("BANK MANAGEMENT")
app.geometry("900x640")




# Create left frame
left_frame = tk.Frame(app, bg="lightblue")
left_frame.grid(row=0, column=0, sticky="nsew")

# Create right frame
right_frame = tk.Frame(app, bg="lightgreen")
right_frame.grid(row=0, column=1, sticky="nsew")

# Configure grid weights to make frames resize properly
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=9)
app.grid_rowconfigure(0, weight=1)



# Logo image
logo_image = Image.open(os.path.join(os.getcwd(),"test_images\CustomTkinter_logo_single.png"))  
logo_image = logo_image.resize((50, 50))  
logo_photo = ImageTk.PhotoImage(logo_image)

# Displaying the image with text in the left frame
logo_label = tk.Label(left_frame, image=logo_photo,padx=5, text="BOI", compound=tk.LEFT, bg="lightblue",fg="#0052CC",font=('sans-serif',32,'bold'))
logo_label.pack(pady=20)


def change_right_frame_content(content,account_number=None):
    # Remove current content in right_frame
    for widget in right_frame.winfo_children():
        widget.destroy()
    
    if content ==  "NEW ACCOUNT":
        create_account()  

    elif content ==  "ALL ACCOUNT HOLDERS":
        create_account_holders()   

    elif content ==  "WITHDRAW AMOUNT":
        withdraw_amount()  

    elif content ==  "DEPOSITE AMOUNT":
        deposite_amount()  

    elif content == "DELETE ACCOUNT":
        delete_account()

    elif content == "BALANCE ENQUIRY":
        get_balance()

    elif content == "MODIFY AN ACCOUNT":
        modify_account()    

    elif content == "TRANSFER MONEY":
        transfer_money()    

    elif content == "PRINT PASSBOOK":
        print_passbook(account_number)

    elif content == "PASSBOOK":
        passbook() 

    elif content == "ACCOUNT DETAILS":
        get_account()

    elif content == "PRINT ACCOUNT":
        print_account(account_number)                      

       

        


def on_click(event):
    event.widget.config(bg="black", fg="white")
    selected_menu_item = event.widget.cget("text")
    change_right_frame_content(selected_menu_item)

    for label in menu_labels:
        if label != event.widget:
            label.config(bg="lightblue", fg="black")
   


    


menu_labels= []

menu_font= ("sans-serif",10,"bold")
menu_text_color= "black"

# menu1 effect label
menu1_image = Image.open(os.path.join(os.getcwd(),r"test_images\add_user_light.png"))  # Replace with the path to your icon
menu1_image = menu1_image.resize((20, 20))  # Resize the image as needed
menu1_photo = ImageTk.PhotoImage(menu1_image)

menu1_label = tk.Label(left_frame,padx=5,pady=10, image=menu1_photo, text="NEW ACCOUNT",font=menu_font,fg="white", compound=tk.LEFT,anchor="w", bg="black")
menu1_label.image = menu1_photo  
menu1_label.pack(fill=tk.X, pady=5)

# Bind events for menu1 effect
menu1_label.bind("<Button-1>",on_click)


menu2_image = Image.open(os.path.join(os.getcwd(),"test_images\mi2.png"))  # Replace with the path to your icon
menu2_image = menu2_image.resize((20, 20))  # Resize the image as needed
menu2_photo = ImageTk.PhotoImage(menu2_image)

menu2_label = tk.Label(left_frame,padx=5,pady=10, image=menu2_photo, text="ALL ACCOUNT HOLDERS",font=menu_font,fg=menu_text_color, compound=tk.LEFT,anchor="w", bg="lightblue")
menu2_label.image = menu2_photo  
menu2_label.pack(fill=tk.X, pady=5)

# Bind events for menu2 effect
menu2_label.bind("<Button-1>",on_click)


menu3_image = Image.open(os.path.join(os.getcwd(),"test_images\mi3.png"))  # Replace with the path to your icon
menu3_image = menu3_image.resize((20, 20))  # Resize the image as needed
menu3_photo = ImageTk.PhotoImage(menu3_image)

menu3_label = tk.Label(left_frame,padx=5,pady=10, image=menu3_photo, text="WITHDRAW AMOUNT",font=menu_font,fg=menu_text_color, compound=tk.LEFT,anchor="w", bg="lightblue")
menu3_label.image = menu3_photo  
menu3_label.pack(fill=tk.X, pady=5)

# Bind events for  effect
menu3_label.bind("<Button-1>",on_click)


menu4_image = Image.open(os.path.join(os.getcwd(),"test_images\mi4.png"))  # Replace with the path to your icon
menu4_image = menu4_image.resize((20, 20))  # Resize the image as needed
menu4_photo = ImageTk.PhotoImage(menu4_image)

menu4_label = tk.Label(left_frame,padx=5,pady=10, image=menu4_photo, text="DEPOSITE AMOUNT",font=menu_font,fg=menu_text_color, compound=tk.LEFT,anchor="w", bg="lightblue")
menu4_label.image = menu4_photo  
menu4_label.pack(fill=tk.X, pady=5)
menu4_label.bind("<Button-1>",on_click)

# Bind events for  effect


menu5_image = Image.open(os.path.join(os.getcwd(),"test_images\mi5.png"))  # Replace with the path to your icon
menu5_image = menu5_image.resize((20, 20))  # Resize the image as needed
menu5_photo = ImageTk.PhotoImage(menu5_image)

menu5_label = tk.Label(left_frame,padx=5,pady=10, image=menu5_photo, text="DELETE ACCOUNT",font=menu_font,fg=menu_text_color, compound=tk.LEFT,anchor="w", bg="lightblue")
menu5_label.image = menu5_photo  
menu5_label.pack(fill=tk.X, pady=5)

# Bind events for  effect
menu5_label.bind("<Button-1>",on_click)



menu6_image = Image.open(os.path.join(os.getcwd(),"test_images\mi6.png"))  # Replace with the path to your icon
menu6_image = menu6_image.resize((20, 20))  # Resize the image as needed
menu6_photo = ImageTk.PhotoImage(menu6_image)

menu6_label = tk.Label(left_frame,padx=5,pady=10, image=menu6_photo, text="BALANCE ENQUIRY",font=menu_font,fg=menu_text_color, compound=tk.LEFT,anchor="w", bg="lightblue")
menu6_label.image = menu6_photo  
menu6_label.pack(fill=tk.X, pady=5)

# Bind events for  effect
menu6_label.bind("<Button-1>",on_click)

menu7_image = Image.open(os.path.join(os.getcwd(),"test_images\mi7.png"))  # Replace with the path to your icon
menu7_image = menu7_image.resize((20, 20))  # Resize the image as needed
menu7_photo = ImageTk.PhotoImage(menu7_image)

menu7_label = tk.Label(left_frame,padx=5,pady=10, image=menu7_photo, text="MODIFY AN ACCOUNT",font=menu_font,fg=menu_text_color, compound=tk.LEFT,anchor="w", bg="lightblue")
menu7_label.image = menu7_photo  
menu7_label.pack(fill=tk.X, pady=5)

# Bind events for  effect
menu7_label.bind("<Button-1>",on_click)


menu8_image = Image.open(os.path.join(os.getcwd(),"test_images\mi8.png"))  # Replace with the path to your icon
menu8_image = menu8_image.resize((20, 20))  # Resize the image as needed
menu8_photo = ImageTk.PhotoImage(menu8_image)

menu8_label = tk.Label(left_frame,padx=5,pady=10, image=menu8_photo, text="TRANSFER MONEY",font=menu_font,fg=menu_text_color, compound=tk.LEFT,anchor="w", bg="lightblue")
menu8_label.image = menu8_photo  
menu8_label.pack(fill=tk.X, pady=5)

# Bind events for  effect
menu8_label.bind("<Button-1>",on_click)


menu9_image = Image.open(os.path.join(os.getcwd(),"test_images\mi9.png"))  # Replace with the path to your icon
menu9_image = menu9_image.resize((20, 20))  # Resize the image as needed
menu9_photo = ImageTk.PhotoImage(menu9_image)

menu9_label = tk.Label(left_frame,padx=5,pady=10, image=menu9_photo, text="PASSBOOK",font=menu_font,fg=menu_text_color, compound=tk.LEFT,anchor="w", bg="lightblue")
menu9_label.image = menu9_photo  
menu9_label.pack(fill=tk.X, pady=5)

# Bind events for  effect
menu9_label.bind("<Button-1>",on_click)


menu10_image = Image.open(os.path.join(os.getcwd(),"test_images\mi10.png"))  # Replace with the path to your icon
menu10_image = menu10_image.resize((20, 20))  # Resize the image as needed
menu10_photo = ImageTk.PhotoImage(menu10_image)

menu10_label = tk.Label(left_frame,padx=5,pady=10, image=menu10_photo, text="ACCOUNT DETAILS",font=menu_font,fg=menu_text_color, compound=tk.LEFT,anchor="w", bg="lightblue")
menu10_label.image = menu10_photo  
menu10_label.pack(fill=tk.X, pady=5)

# Bind events for  effect
menu10_label.bind("<Button-1>",on_click)


menu_labels.extend([menu1_label,menu2_label,menu3_label,menu4_label,menu5_label,menu6_label,menu7_label,menu8_label,menu9_label,menu10_label])

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     
# Function to retrieve form data
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def create_account_form_data(account_entry, account_type_var, balance_entry, pin_entry, progress_bar):
    account_name = account_entry.get()
    account_type = account_type_var.get()
    account_balance = balance_entry.get()
    pin_number = pin_entry.get()

    if not all([account_name, account_type, account_balance, pin_number]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    progress_bar.grid(row=5, column=1, columnspan=2, pady=20)
    progress_bar.start()  # Start the progress bar animation

    # Simulate account creation progress (adjust this logic according to your requirements)
    for i in range(1, 100):
        progress_bar["value"] += 1
        sleep(0.8/i)  # Sleep for a short time to simulate progress
        app.update_idletasks()

    progress_bar.stop()
    progress_bar.grid_remove()  # Hide the progress bar

    createAccountInDB(account_name,account_type,account_balance,pin_number)
    
    messagebox.showinfo("Success", "Account Created")

    # Clear the form fields after submitting
    account_entry.delete(0, tk.END)
    balance_entry.delete(0, tk.END)
    pin_entry.delete(0, tk.END)
    account_type_var.set("")
def create_account():
    form_frame = ttk.Frame(right_frame, padding=100)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")
    
    # Header
    header_label = ttk.Label(form_frame, text="Create Account", foreground="#0052CC", font=('sans-serif', 32, 'bold'))
    header_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Account Number, Account Type, Account Balance, PIN Number
    account_label = ttk.Label(form_frame, text="Account Name")
    account_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    account_entry = ttk.Entry(form_frame)
    account_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

    account_type_label = ttk.Label(form_frame, text="Account Type")
    account_type_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
    account_type_var = tk.StringVar()
    saving_radio = ttk.Radiobutton(form_frame, text="Saving", variable=account_type_var, value="Saving")
    saving_radio.grid(row=2, column=1, padx=10, pady=5, sticky='w')
    current_radio = ttk.Radiobutton(form_frame, text="Current", variable=account_type_var, value="Current")
    current_radio.grid(row=2, column=1, padx=80, pady=5, sticky='ew')

    balance_label = ttk.Label(form_frame, text="Account Balance")
    balance_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
    balance_entry = ttk.Entry(form_frame)
    balance_entry.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

    pin_label = ttk.Label(form_frame, text="PIN Number")
    pin_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
    pin_entry = ttk.Entry(form_frame, show="*")
    pin_entry.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

    progress_bar = ttk.Progressbar(form_frame, orient='horizontal', mode='determinate')
    
    submit_button = ttk.Button(form_frame, text="Submit", command=lambda: create_account_form_data(account_entry, account_type_var, balance_entry, pin_entry, progress_bar))
    submit_button.grid(row=5, column=0, columnspan=2, pady=20)



def create_account_holders():
    # Define the headers
    headers = ['Account', 'IFSC','Name','Type', 'Balance']

    # Place the table within the right_frame
    table_frame = ttk.Frame(right_frame)
    table_frame.grid(row=0, column=0, padx=20, pady=20,sticky='nsew')

    # Create header labels
    for col, header in enumerate(headers):
        label = ttk.Label(table_frame, text=header, font=('Arial', 12, 'bold'))
        label.grid(row=0, column=col, padx=10, pady=5)

    # Simulate some data (You can replace this with your actual data)
    data = getAllAccountsInDB()

    # Populate the table with data
    for row_idx, row_data in enumerate(data, start=1):
        row_data= list(row_data)
        row_data.pop()

        for col_idx, cell_value in enumerate(row_data):
            label = ttk.Label(table_frame, text=cell_value)
            label.grid(row=row_idx, column=col_idx, padx=10, pady=5)
    
    right_frame.grid_columnconfigure(0, weight=1)
    table_frame.grid_columnconfigure(0,weight=1)
    table_frame.grid_columnconfigure(1,weight=1)
    table_frame.grid_columnconfigure(2,weight=1)
    table_frame.grid_columnconfigure(3,weight=1)
    table_frame.grid_columnconfigure(4,weight=1)
        

def withdraw_amount_form_data(account_entry, balance_entry, pin_entry, progress_bar):
    account_number = account_entry.get()
    withdraw_amount = balance_entry.get()
    pin_number = pin_entry.get()

    if not all([account_number, withdraw_amount, pin_number]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    
    progress_bar.grid(row=5, column=1, columnspan=2, pady=20)
    progress_bar.start()  # Start the progress bar animation

    # Simulate account creation progress (adjust this logic according to your requirements)
    for i in range(1, 100):
        progress_bar["value"] += 1
        sleep(0.8/i)  # Sleep for a short time to simulate progress
        app.update_idletasks()

    progress_bar.stop()
    progress_bar.grid_remove()  # Hide the progress bar
    
    data= checkForValidAccount(account_number)

    if data:
        valid_pin,valid_balance= data
        withdraw_amount= Decimal(withdraw_amount)
        encrpt_pin= generateHash(pin_number)

        if encrpt_pin != valid_pin:
            messagebox.showerror("Error", "INVALID PIN")
            return 
        
        if withdraw_amount > valid_balance:
            messagebox.showerror("Error", "INSUFFICIENT BALANCE")
            return
        
        updateBalance(valid_balance-withdraw_amount,account_number)
        updatePassbook(account_number,withdraw_amount,"NULL",valid_balance-withdraw_amount)
        messagebox.showinfo("Success", "Withdraw Success")
    else:
        return    

    # Clear the form fields after submitting
    account_entry.delete(0, tk.END)
    balance_entry.delete(0, tk.END)
    pin_entry.delete(0, tk.END)
def withdraw_amount():
    form_frame = ttk.Frame(right_frame, padding=20)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Header
    header_label = ttk.Label(form_frame, text="WITHDRAW AMOUNT", foreground="#0052CC", font=('sans-serif', 32, 'bold'))
    header_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Account Number
    account_label = ttk.Label(form_frame, text="Account Number")
    account_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    account_entry = ttk.Entry(form_frame)
    account_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

    pin_label = ttk.Label(form_frame, text="PIN Number")
    pin_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
    pin_entry = ttk.Entry(form_frame, show="*")
    pin_entry.grid(row=4, column=1, padx=10, pady=5, sticky='ew')
    

    balance_label = ttk.Label(form_frame, text="Withdraw Amount")
    balance_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
    balance_entry = ttk.Entry(form_frame)
    balance_entry.grid(row=3, column=1, padx=10, pady=5, sticky='ew')
    
    progress_bar = ttk.Progressbar(form_frame, orient='horizontal', mode='determinate')
    submit_button = ttk.Button(form_frame, text="Withdraw", command=lambda: withdraw_amount_form_data(account_entry, balance_entry, pin_entry, progress_bar))
    submit_button.grid(row=5, column=0, columnspan=2, pady=20)



def deposite_amount_form_data(account_entry, balance_entry, progress_bar):
    account_number = account_entry.get()
    deposite_amount = balance_entry.get()

    if not all([account_number, deposite_amount]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    progress_bar.grid(row=5, column=1, columnspan=2, pady=20)
    progress_bar.start()  # Start the progress bar animation

    # Simulate account creation progress (adjust this logic according to your requirements)
    for i in range(1, 100):
        progress_bar["value"] += 1
        sleep(0.8/i)  # Sleep for a short time to simulate progress
        app.update_idletasks()

    progress_bar.stop()
    progress_bar.grid_remove()  # Hide the progress bar

    
    data= checkForValidAccount(account_number)

    if data:
        valid_pin,valid_balance= data
        deposite_amount= Decimal(deposite_amount)
        
        updateBalance(valid_balance+deposite_amount,account_number)
        updatePassbook(account_number,"NULL",deposite_amount,valid_balance+deposite_amount)
        messagebox.showinfo("Success", "Deposite Success")
        
    else:
        return

    # Clear the form fields after submitting
    account_entry.delete(0, tk.END)
    balance_entry.delete(0, tk.END)
def deposite_amount():
    form_frame = ttk.Frame(right_frame, padding=20)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Header
    header_label = ttk.Label(form_frame, text="DEPOSITE AMOUNT", foreground="#0052CC", font=('sans-serif', 32, 'bold'))
    header_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Account Number
    account_label = ttk.Label(form_frame, text="Account Number")
    account_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    account_entry = ttk.Entry(form_frame)
    account_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')
    

    balance_label = ttk.Label(form_frame, text="Account Balance")
    balance_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
    balance_entry = ttk.Entry(form_frame)
    balance_entry.grid(row=3, column=1, padx=10, pady=5, sticky='ew')
    
    progress_bar = ttk.Progressbar(form_frame, orient='horizontal', mode='determinate')
    submit_button = ttk.Button(form_frame, text="Deposite", command=lambda: deposite_amount_form_data(account_entry, balance_entry, progress_bar))
    submit_button.grid(row=5, column=0, columnspan=2, pady=20)


def delete_account_form_data(account_entry,progress_bar):
    account_number = account_entry.get()
    

    if not all([account_number]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    
    progress_bar.grid(row=5, column=1, columnspan=2, pady=20)
    progress_bar.start()  # Start the progress bar animation

    # Simulate account creation progress (adjust this logic according to your requirements)
    for i in range(1, 100):
        progress_bar["value"] += 1
        sleep(0.8/i)  # Sleep for a short time to simulate progress
        app.update_idletasks()

    progress_bar.stop()
    progress_bar.grid_remove()  # Hide the progress bar

    data= checkForValidAccount(account_number)

    if data:    
        deleteAccountInDB(account_number)
        messagebox.showinfo("Success", "Account Deleted")
    else:
        return

    # Clear the form fields after submitting
    account_entry.delete(0, tk.END)
def delete_account():
    form_frame = ttk.Frame(right_frame, padding=20)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Header
    header_label = ttk.Label(form_frame, text="DELETE ACCOUNT", foreground="#0052CC", font=('sans-serif', 32, 'bold'))
    header_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Account Number
    account_label = ttk.Label(form_frame, text="Account Number")
    account_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    account_entry = ttk.Entry(form_frame)
    account_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

    
    
    progress_bar = ttk.Progressbar(form_frame, orient='horizontal', mode='determinate')
    submit_button = tk.Button(form_frame, text="Delete",bg="red",fg="white",command=lambda: delete_account_form_data(account_entry, progress_bar))
    submit_button.grid(row=5, column=0, columnspan=2, pady=20)


def get_balance_form_data(account_entry,balance_label,progress_bar):
    account_number = account_entry.get()
    

    if not all([account_number]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    
    progress_bar.grid(row=5, column=1, columnspan=2, pady=20)
    progress_bar.start()  # Start the progress bar animation

    # Simulate account creation progress (adjust this logic according to your requirements)
    for i in range(1, 100):
        progress_bar["value"] += 1
        sleep(0.8/i)  # Sleep for a short time to simulate progress
        app.update_idletasks()

    progress_bar.stop()
    progress_bar.grid_remove()  # Hide the progress bar
    
    data= checkForValidAccount(account_number)

    if data:    
        valid_pin,valid_balance= data
        balance_label.config(text= f"AVL BAL :- ₹{valid_balance}")
        balance_label.grid(row=3, column=0, columnspan=2, pady=20)

    else:
        return

    # Clear the form fields after submitting
    account_entry.delete(0, tk.END)
def get_balance():
    form_frame = ttk.Frame(right_frame, padding=20)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Header
    header_label = ttk.Label(form_frame, text="BALANCE ENQUIRY", foreground="#0052CC", font=('sans-serif', 32, 'bold'))
    header_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Account Number
    account_label = ttk.Label(form_frame, text="Account Number")
    account_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    account_entry = ttk.Entry(form_frame)
    account_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

    balance_label = ttk.Label(form_frame, text="BAL :-", foreground="green", font=('sans-serif', 22, 'bold'))

    progress_bar = ttk.Progressbar(form_frame, orient='horizontal', mode='determinate')
    submit_button = ttk.Button(form_frame, text="Get Balance", command=lambda: get_balance_form_data(account_entry,balance_label,progress_bar))
    submit_button.grid(row=5, column=0, columnspan=2, pady=20)


def modify_account_form_data(account_entry, account_type_var, name_entry, pin_entry, progress_bar):
    account_number = account_entry.get()
    account_type = account_type_var.get()
    account_name = name_entry.get()
    pin_number = pin_entry.get()

    if not all([account_number, account_type, account_name, pin_number]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    progress_bar.grid(row=5, column=1, columnspan=2, pady=20)
    progress_bar.start()  # Start the progress bar animation

    # Simulate account creation progress (adjust this logic according to your requirements)
    for i in range(1, 100):
        progress_bar["value"] += 1
        sleep(0.8/i)  # Sleep for a short time to simulate progress
        app.update_idletasks()

    progress_bar.stop()
    progress_bar.grid_remove()  # Hide the progress bar

    data= checkForValidAccount(account_number)

    if data:
        valid_pin,valid_balance= data
        encrpt_pin= generateHash(pin_number)

        if encrpt_pin != valid_pin:
            messagebox.showerror("Error", "INVALID PIN")
            return 
        
        modifyAccount(account_number,account_type,account_name)
        messagebox.showinfo("Success", "Account Data Updated")
    else:
        return

    # Clear the form fields after submitting
    account_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    pin_entry.delete(0, tk.END)
    account_type_var.set("")
def modify_account():
    form_frame = ttk.Frame(right_frame, padding=20)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Header
    header_label = ttk.Label(form_frame, text="MODIFY ACCOUNT", foreground="#0052CC", font=('sans-serif', 32, 'bold'))
    header_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Account Number, Account Type, Account Balance, PIN Number
    account_label = ttk.Label(form_frame, text="Account Number")
    account_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    account_entry = ttk.Entry(form_frame)
    account_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

    pin_label = ttk.Label(form_frame, text="PIN Number")
    pin_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
    pin_entry = ttk.Entry(form_frame, show="*")
    pin_entry.grid(row=2, column=1, padx=10, pady=5, sticky='ew')


    name_label = ttk.Label(form_frame, text="Account Holder New Name")
    name_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
    name_entry = ttk.Entry(form_frame)
    name_entry.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

    account_type_label = ttk.Label(form_frame, text="Account New Type")
    account_type_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
    account_type_var = tk.StringVar()
    saving_radio = ttk.Radiobutton(form_frame, text="Saving", variable=account_type_var, value="Saving")
    saving_radio.grid(row=4, column=1, padx=10, pady=5, sticky='w')
    current_radio = ttk.Radiobutton(form_frame, text="Current", variable=account_type_var, value="Current")
    current_radio.grid(row=4, column=1, padx=80, pady=5, sticky='ew')

    

    

    progress_bar = ttk.Progressbar(form_frame, orient='horizontal', mode='determinate')
    
    submit_button = ttk.Button(form_frame, text="Modify", command=lambda: modify_account_form_data(account_entry, account_type_var, name_entry, pin_entry, progress_bar))
    submit_button.grid(row=5, column=0, columnspan=2, pady=20)


def transfer_money_form_data(account_entry, beneficiary_account_entry,transfer_amount_entry,pin_entry, progress_bar):
    account_number = account_entry.get()
    beneficiary_account_number = beneficiary_account_entry.get()
    transfer_amount= transfer_amount_entry.get()
    pin_number = pin_entry.get()

    if not all([account_number, beneficiary_account_number, pin_number]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    progress_bar.grid(row=5, column=1, columnspan=2, pady=20)
    progress_bar.start()  # Start the progress bar animation

    # Simulate account creation progress (adjust this logic according to your requirements)
    for i in range(1, 100):
        progress_bar["value"] += 1
        sleep(0.8/i)  # Sleep for a short time to simulate progress
        app.update_idletasks()

    progress_bar.stop()
    progress_bar.grid_remove()  # Hide the progress bar

    your_data= checkForValidAccount(account_number)
    beneficiary_data= checkForValidAccount(beneficiary_account_number)

    if your_data and beneficiary_data:

        your_valid_pin,your_valid_balance= your_data
        beneficiary_valid_pin,beneficiary_valid_balance= beneficiary_data

        transfer_amount= Decimal(transfer_amount)
        encrpt_pin= generateHash(pin_number)

        if encrpt_pin != your_valid_pin:
            messagebox.showerror("Error", "INVALID PIN")
            return 
        
        if transfer_amount > your_valid_balance:
            messagebox.showerror("Error", "INSUFFICIENT BALANCE")
            return
        
        updateBalance(your_valid_balance-transfer_amount,account_number)
        updateBalance(beneficiary_valid_balance+transfer_amount,beneficiary_account_number)
        
        updatePassbook(account_number,transfer_amount,"NULL",your_valid_balance-transfer_amount)
        updatePassbook(account_number,"NULL",transfer_amount,beneficiary_valid_balance+transfer_amount)
        messagebox.showinfo("Success", "Money Transfer Success")
    else:
        return    

    # Clear the form fields after submitting
    account_entry.delete(0, tk.END)
    beneficiary_account_entry.delete(0, tk.END)
    pin_entry.delete(0, tk.END)
    transfer_amount_entry.delete(0, tk.END)
def transfer_money():
    form_frame = ttk.Frame(right_frame, padding=60)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Header
    header_label = ttk.Label(form_frame, text="Transfer Money", foreground="#0052CC", font=('sans-serif', 32, 'bold'))
    header_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Account Number, Account Type, Account Balance, PIN Number
    account_label = ttk.Label(form_frame, text="Account Number")
    account_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    account_entry = ttk.Entry(form_frame)
    account_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

    beneficiary_account_label = ttk.Label(form_frame, text="Beneficiary Account Number")
    beneficiary_account_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
    beneficiary_account_entry = ttk.Entry(form_frame)
    beneficiary_account_entry.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

    transfer_amount_label = ttk.Label(form_frame, text="Transfer Amount")
    transfer_amount_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
    transfer_amount_entry = ttk.Entry(form_frame)
    transfer_amount_entry.grid(row=3, column=1, padx=10, pady=5, sticky='ew')


    pin_label = ttk.Label(form_frame, text="PIN Number")
    pin_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
    pin_entry = ttk.Entry(form_frame, show="*")
    pin_entry.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

    progress_bar = ttk.Progressbar(form_frame, orient='horizontal', mode='determinate')
    
    submit_button = ttk.Button(form_frame, text="Transfer Money", command=lambda: transfer_money_form_data(account_entry, beneficiary_account_entry,transfer_amount_entry, pin_entry, progress_bar))
    submit_button.grid(row=5, column=0, columnspan=2, pady=20)


def passbook_form_data(account_entry, pin_entry, progress_bar):
    account_number = account_entry.get()
    pin_number = pin_entry.get()

    if not all([account_number, pin_number]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    
    progress_bar.grid(row=5, column=1, columnspan=2, pady=20)
    progress_bar.start()  # Start the progress bar animation

    # Simulate account creation progress (adjust this logic according to your requirements)
    for i in range(1, 100):
        progress_bar["value"] += 1
        sleep(0.8/i)  # Sleep for a short time to simulate progress
        app.update_idletasks()

    progress_bar.stop()
    progress_bar.grid_remove()  # Hide the progress bar
    
 
    data= checkForValidAccount(account_number)

    if data:
        valid_pin,valid_balance= data
        encrpt_pin= generateHash(pin_number)

        if encrpt_pin != valid_pin:
            messagebox.showerror("Error", "INVALID PIN")
            return 
        change_right_frame_content("PRINT PASSBOOK",account_number)

    else:
        return  

    
def passbook():
    form_frame = ttk.Frame(right_frame, padding=20)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Header
    header_label = ttk.Label(form_frame, text="PASSBOOK", foreground="#0052CC", font=('sans-serif', 32, 'bold'))
    header_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Account Number
    account_label = ttk.Label(form_frame, text="Account Number")
    account_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    account_entry = ttk.Entry(form_frame)
    account_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

    pin_label = ttk.Label(form_frame, text="PIN Number")
    pin_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
    pin_entry = ttk.Entry(form_frame, show="*")
    pin_entry.grid(row=4, column=1, padx=10, pady=5, sticky='ew')
    
    
    progress_bar = ttk.Progressbar(form_frame, orient='horizontal', mode='determinate')
    submit_button = ttk.Button(form_frame, text="Get Passbook", command=lambda: passbook_form_data(account_entry, pin_entry, progress_bar))
    submit_button.grid(row=5, column=0, columnspan=2, pady=20)
def print_passbook(account_number):
    # Define the headers
    headers = ["DATE","TIME","WITHDRAW","DEPOSITE","BALANCE"]

    # Place the table within the right_frame
    table_frame = ttk.Frame(right_frame)
    table_frame.grid(row=0, column=0, padx=20, pady=20,sticky='nsew')

    # Create header labels
    for col, header in enumerate(headers):
        label = ttk.Label(table_frame, text=header, font=('Arial', 12, 'bold'))
        label.grid(row=0, column=col, padx=10, pady=5)

    # Simulate some data (You can replace this with your actual data)
    data = getPassbook(account_number)


    # Populate the table with data
    for row_idx, row_data in enumerate(data, start=1):
        
        row_data= list(row_data)
        del row_data[0]
        for col_idx, cell_value in enumerate(row_data):
            label = ttk.Label(table_frame, text=cell_value)
            label.grid(row=row_idx, column=col_idx, padx=10, pady=5)
    
    right_frame.grid_columnconfigure(0, weight=1)
    table_frame.grid_columnconfigure(0,weight=1)
    table_frame.grid_columnconfigure(1,weight=1)
    table_frame.grid_columnconfigure(2,weight=1)
    table_frame.grid_columnconfigure(3,weight=1)
    table_frame.grid_columnconfigure(4,weight=1)
        

def get_account_form_data(account_entry,progress_bar):
    account_number = account_entry.get()
    

    if not all([account_number]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    
    progress_bar.grid(row=5, column=1, columnspan=2, pady=20)
    progress_bar.start()  # Start the progress bar animation

    # Simulate account creation progress (adjust this logic according to your requirements)
    for i in range(1, 100):
        progress_bar["value"] += 1
        sleep(0.8/i)  # Sleep for a short time to simulate progress
        app.update_idletasks()

    progress_bar.stop()
    progress_bar.grid_remove()  # Hide the progress bar
    
    data= checkForValidAccount(account_number)

    if data:    
        change_right_frame_content("PRINT ACCOUNT",account_number)
    else:
        return
def get_account():
    form_frame = ttk.Frame(right_frame, padding=20)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Header
    header_label = ttk.Label(form_frame, text="ACCOUNT INFORMATION", foreground="#0052CC", font=('sans-serif', 32, 'bold'))
    header_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Account Number
    account_label = ttk.Label(form_frame, text="Account Number")
    account_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    account_entry = ttk.Entry(form_frame)
    account_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

    
    
    progress_bar = ttk.Progressbar(form_frame, orient='horizontal', mode='determinate')
    submit_button = ttk.Button(form_frame, text="Get Account Details",command=lambda: get_account_form_data(account_entry, progress_bar))
    submit_button.grid(row=5, column=0, columnspan=2, pady=20)
def print_account(account_number):

    data= getAccount(account_number)

    form_frame = ttk.Frame(right_frame, padding=20)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Header
    header_label = ttk.Label(form_frame, text="Account Info", foreground="#0052CC", font=('sans-serif', 32, 'bold'))
    header_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Account Number, Account Type, Account Balance, PIN Number
    account_label = ttk.Label(form_frame, text="Account Number")
    account_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    account_label_value = ttk.Label(form_frame,text=data[0])
    account_label_value.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

    ifsc_label = ttk.Label(form_frame, text="Account IFSC")
    ifsc_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
    ifsc_label_value = ttk.Label(form_frame,text=data[1])
    ifsc_label_value.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

    account_name_label = ttk.Label(form_frame, text="Account Holder Name")
    account_name_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
    account_name_label_value = ttk.Label(form_frame,text=data[2])
    account_name_label_value.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

    account_type_label = ttk.Label(form_frame, text="Account Type")
    account_type_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
    account_type_label_value = ttk.Label(form_frame, text=data[3])
    account_type_label_value.grid(row=4, column=1, padx=10, pady=5, sticky='w')
    

    balance_label = ttk.Label(form_frame, text="Account Balance")
    balance_label.grid(row=5, column=0, padx=10, pady=5, sticky='w')
    balance_label_value = ttk.Label(form_frame, text=data[4])
    balance_label_value.grid(row=5, column=1, padx=10, pady=5, sticky='w')
    





create_account()

app.mainloop()
