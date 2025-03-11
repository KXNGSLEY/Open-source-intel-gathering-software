import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
from main import (
    search_username, check_email, check_ip, 
    extract_document_metadata, extract_image_metadata, 
    find_similar_faces, reverse_image_search
)

def update_button_state(entry_widget, button):
    """Enables/disables button based on input field."""
    button.config(state=tk.NORMAL if entry_widget.get().strip() else tk.DISABLED)

def search_username_action():
    username = username_entry.get().strip()
    if not username:
        messagebox.showerror("Error", "Enter a username")
        return
    results = search_username(username) or "No results found."
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, results)
    output_text.config(state=tk.DISABLED)

def check_email_action():
    email = email_entry.get().strip()
    if not email:
        messagebox.showerror("Error", "Enter an email")
        return
    results = check_email(email) or "No results found."
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, results)
    output_text.config(state=tk.DISABLED)

def check_ip_action():
    ip = ip_entry.get().strip()
    if not ip:
        messagebox.showerror("Error", "Enter an IP address")
        return
    results = check_ip(ip) or "No results found."
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, results)
    output_text.config(state=tk.DISABLED)

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)
        extract_metadata_button.config(state=tk.NORMAL)
        find_faces_button.config(state=tk.NORMAL)
        reverse_search_button.config(state=tk.NORMAL)

def extract_metadata_action():
    file_path = file_path_entry.get().strip()
    if not file_path:
        messagebox.showerror("Error", "Select a file")
        return

    ext = os.path.splitext(file_path)[1].lower()
    if ext in (".pdf", ".docx"):
        results = extract_document_metadata(file_path)
    else:
        results = extract_image_metadata(file_path)

    results = results or "No metadata found."
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, results)
    output_text.config(state=tk.DISABLED)

def find_faces_action():
    image_path = file_path_entry.get().strip()
    if not image_path:
        messagebox.showerror("Error", "Select an image")
        return
    results = find_similar_faces(image_path) or "No similar faces found."
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, results)
    output_text.config(state=tk.DISABLED)

def reverse_search_action():
    image_path = file_path_entry.get().strip()
    if not image_path:
        messagebox.showerror("Error", "Select an image")
        return
    results = reverse_image_search(image_path) or ["No matches found."]
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "\n".join(results))
    output_text.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("OSINT Toolkit")
root.geometry("600x600")
root.resizable(True, True)

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()
search_username_button = tk.Button(root, text="Search Username", command=search_username_action, state=tk.DISABLED)
search_username_button.pack()
username_entry.bind("<KeyRelease>", lambda event: update_button_state(username_entry, search_username_button))

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()
check_email_button = tk.Button(root, text="Check Email", command=check_email_action, state=tk.DISABLED)
check_email_button.pack()
email_entry.bind("<KeyRelease>", lambda event: update_button_state(email_entry, check_email_button))

tk.Label(root, text="IP Address:").pack()
ip_entry = tk.Entry(root)
ip_entry.pack()
check_ip_button = tk.Button(root, text="Check IP", command=check_ip_action, state=tk.DISABLED)
check_ip_button.pack()
ip_entry.bind("<KeyRelease>", lambda event: update_button_state(ip_entry, check_ip_button))

tk.Label(root, text="File Path:").pack()
file_path_entry = tk.Entry(root, width=50)
file_path_entry.pack()
tk.Button(root, text="Browse", command=select_file).pack()

extract_metadata_button = tk.Button(root, text="Extract Metadata", command=extract_metadata_action, state=tk.DISABLED)
extract_metadata_button.pack()

find_faces_button = tk.Button(root, text="Find Similar Faces", command=find_faces_action, state=tk.DISABLED)
find_faces_button.pack()

reverse_search_button = tk.Button(root, text="Reverse Image Search", command=reverse_search_action, state=tk.DISABLED)
reverse_search_button.pack()

output_text = scrolledtext.ScrolledText(root, height=10, width=70, state=tk.DISABLED)
output_text.pack()

root.mainloop()
