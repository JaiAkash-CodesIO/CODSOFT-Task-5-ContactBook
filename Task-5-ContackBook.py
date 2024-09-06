import tkinter as tk
from tkinter import messagebox
import json

contacts = {}

def load_contacts():
    global contacts
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}

def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()
    
    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts()
        update_contact_list()
        messagebox.showinfo("Success", f"Contact for {name} added.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and phone number are required.")

def update_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()
    
    if name in contacts:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts()
        update_contact_list()
        messagebox.showinfo("Success", f"Contact for {name} updated.")
        clear_entries()
    else:
        messagebox.showerror("Error", f"No contact found with the name {name}.")

def delete_contact():
    name = name_entry.get().strip()
    
    if name in contacts:
        del contacts[name]
        save_contacts()
        update_contact_list()
        messagebox.showinfo("Success", f"Contact for {name} deleted.")
        clear_entries()
    else:
        messagebox.showerror("Error", f"No contact found with the name {name}.")

def search_contact():
    name = name_entry.get().strip()
    
    if name in contacts:
        contact = contacts[name]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact['Phone'])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, contact['Email'])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, contact['Address'])
    else:
        messagebox.showerror("Error", f"No contact found with the name {name}.")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name}: {details['Phone']}")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Book")
root.geometry("500x400")

name_label = tk.Label(root, text="Name:", font=('Arial', 12))
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root, font=('Arial', 12))
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(root, text="Phone:", font=('Arial', 12))
phone_label.grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root, font=('Arial', 12))
phone_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email:", font=('Arial', 12))
email_label.grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root, font=('Arial', 12))
email_entry.grid(row=2, column=1, padx=10, pady=5)

address_label = tk.Label(root, text="Address:", font=('Arial', 12))
address_label.grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(root, font=('Arial', 12))
address_entry.grid(row=3, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Contact", font=('Arial', 12), command=add_contact)
add_button.grid(row=4, column=0, padx=10, pady=10)

update_button = tk.Button(root, text="Update Contact", font=('Arial', 12), command=update_contact)
update_button.grid(row=4, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Contact", font=('Arial', 12), command=delete_contact)
delete_button.grid(row=5, column=0, padx=10, pady=10)

search_button = tk.Button(root, text="Search Contact", font=('Arial', 12), command=search_contact)
search_button.grid(row=5, column=1, padx=10, pady=10)

contact_list_label = tk.Label(root, text="Contact List:", font=('Arial', 12))
contact_list_label.grid(row=6, column=0, padx=10, pady=10)

contact_list = tk.Listbox(root, font=('Arial', 12), height=6, width=40)
contact_list.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

load_contacts()
update_contact_list()

root.mainloop()
