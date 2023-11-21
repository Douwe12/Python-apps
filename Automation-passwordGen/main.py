import random
import tkinter as tk
from store_functions import store_input, clear_db
from retrieve_functions import retrieve_password

# initialize tkinter
root = tk.Tk()
root.title("Password Manager")
root.geometry("400x400")



# initialize tkinter GUI store
frame_store = tk.Frame(root, borderwidth = 1, relief = "solid")
lbl_url = tk.Label(frame_store, text = "Enter url: ")
lbl_desc = tk.Label(frame_store, text = "Enter description: ")
entry_url = tk.Entry(frame_store)
entry_description = tk.Entry(frame_store)
button_url = tk.Button(frame_store, text = "Store", command = lambda : store_input(entry_url, entry_description))


# initialize tkinter GUI retrieve
frame_retrieve = tk.Frame(root, borderwidth = 1, relief = "solid")
lbl_retrieve_url = tk.Label(frame_retrieve, text = "Enter URL: ")
lbl_retrieve_desc = tk.Label(frame_retrieve, text = "Enter description: ")
lbl_retrieve_result = tk.Label(frame_retrieve, text = "")
entry_retrieve_url = tk.Entry(frame_retrieve)
entry_retrieve_desc = tk.Entry(frame_retrieve)
button_retrieve = tk.Button(frame_retrieve, text = "Retrieve password", command = lambda : retrieve_password(entry_retrieve_url, entry_retrieve_desc, lbl_retrieve_result))


# initialize tkinter clear button
button_delete = tk.Button(root, text = "Delete all passwords", command = lambda : clear_db())
button_delete.place(relx = 0.98, rely= 0.98, anchor = "se", width = 130, height = 30)





# pack tkinter GUI
margin = 10

# store
lbl_url.pack()
entry_url.pack(padx = margin, pady = margin)
lbl_desc.pack()
entry_description.pack(pady = 5)
button_url.pack(padx = margin, pady = margin)
frame_store.pack(pady = 10)

# retrieve
lbl_retrieve_url.pack()
entry_retrieve_url.pack(padx = margin, pady = margin)
lbl_retrieve_desc.pack()
entry_retrieve_desc.pack(pady = 5)
button_retrieve.pack()
lbl_retrieve_result.pack(padx = margin, pady = margin)
frame_retrieve.pack(pady = 10)











root.mainloop()