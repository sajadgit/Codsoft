import tkinter as tk
from tkinter import ttk, messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book App")

        # Configure the background color of the window
        self.root.configure(bg="#81c784")

        self.contacts = []

        # Create a style for buttons and labels
        style = ttk.Style()
        style.configure("TButton", padding=10, font=("Helvetica", 12))
        style.configure("TLabel", font=("Helvetica", 12))

        # Create and style labels and entry fields
        self.name_label = ttk.Label(root, text="Name:",background="#81c784")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w" )
        self.name_entry = ttk.Entry(root, width=40)  # Make input fields wider
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.phone_label = ttk.Label(root, text="Phone:",background="#81c784")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.phone_entry = ttk.Entry(root, width=40)  # Make input fields wider
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.email_label = ttk.Label(root, text="Email:",background="#81c784")
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = ttk.Entry(root, width=40)  # Make input fields wider
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.address_label = ttk.Label(root, text="Address:",background="#81c784")
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.address_entry = ttk.Entry(root, width=40)  # Make input fields wider
        self.address_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Style buttons
        self.add_button = ttk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, columnspan=3, padx=10, pady=10)

        self.search_label = ttk.Label(root, text="Search:",background="#81c784")
        self.search_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.search_entry = ttk.Entry(root, width=40)  # Make the search field slightly smaller
        self.search_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.search_button = ttk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=5, column=2, padx=10, pady=5)

        self.contacts_listbox = tk.Listbox(root, width=60, height=15)  # Make the listbox wider
        self.contacts_listbox.grid(row=6, columnspan=3, padx=10, pady=10)

        self.view_button = ttk.Button(root, text="View All", command=self.view_contacts)
        self.view_button.grid(row=7, column=0, padx=10, pady=10)

        self.update_button = ttk.Button(root, text="Update", command=self.update_contact)
        self.update_button.grid(row=7, column=1, padx=10, pady=10)

        self.delete_button = ttk.Button(root, text="Delete", command=self.delete_contact)
        self.delete_button.grid(row=7, column=2, padx=10, pady=10)

        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            self.clear_entries()
            self.view_contacts()
        else:
            messagebox.showwarning("Warning", "Both Name and Phone are required.")

    def search_contact(self):
        search_term = self.search_entry.get().lower()
        self.contacts_listbox.delete(0, tk.END)

        for contact in self.contacts:
            if search_term in contact["Name"].lower() or search_term in contact["Phone"].lower():
                self.contacts_listbox.insert(tk.END, f"{contact['Name']}, {contact['Phone']}")

    def view_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['Name']}, {contact['Phone']},{contact['Email']},{contact['Address']}")

    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            selected_contact = self.contacts[index]

            # Open a new window for updating the contact
            update_window = tk.Toplevel(self.root)
            update_window.configure(bg="#81c784")
            update_window.geometry("250x250")
            update_window.title("Update Contact")

            name_label = tk.Label(update_window, text="Name:",background="#81c784")
            name_label.grid(row=0, column=0)
            name_entry = tk.Entry(update_window)
            name_entry.grid(row=0, column=1)
            name_entry.insert(0, selected_contact["Name"])

            phone_label = tk.Label(update_window, text="Phone:",background="#81c784")
            phone_label.grid(row=1, column=0)
            phone_entry = tk.Entry(update_window)
            phone_entry.grid(row=1, column=1)
            phone_entry.insert(0, selected_contact["Phone"])

            email_label = tk.Label(update_window, text="Email:",background="#81c784")
            email_label.grid(row=2, column=0)
            email_entry = tk.Entry(update_window)
            email_entry.grid(row=2, column=1)
            email_entry.insert(0, selected_contact["Email"])

            address_label = tk.Label(update_window, text="Address:",background="#81c784")
            address_label.grid(row=3, column=0)
            address_entry = tk.Entry(update_window)
            address_entry.grid(row=3, column=1)
            address_entry.insert(0, selected_contact["Address"])

            update_button = tk.Button(update_window, text="Update Contact", command=lambda: self.perform_update(
                selected_index, name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get()))
            update_button.grid(row=4, columnspan=3)

        else:
            messagebox.showwarning("Warning", "Select a contact to update.")

    def perform_update(self, selected_index, name, phone, email, address):
        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts[selected_index[0]] = contact
            self.view_contacts()
        else:
            messagebox.showwarning("Warning", "Both Name and Phone are required.")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            self.contacts.pop(selected_index[0])
            self.view_contacts()
        else:
            messagebox.showwarning("Warning", "Select a contact to delete.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
