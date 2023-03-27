import tkinter as tk
from tkinter import ttk

# Define a function to handle the button click event
def handle_click():
    # Get the selected values from the dropdown menus
    first_value = first_var.get()
    second_value = second_var.get()

    # Print the selected values to the console
    print("First value:", first_value)
    print("Second value:", second_value)

# Create the main window
root = tk.Tk()

# Create the first dropdown menu
first_var = tk.StringVar()
first_dropdown = ttk.Combobox(root, textvariable=first_var, values=["Maharashtra", "Delhi", "Odisha"])
first_dropdown.pack()

# Create the second dropdown menu
second_var = tk.StringVar()
second_dropdown = ttk.Combobox(root, textvariable=second_var, values=["within 5,000", "5,000 to 10,000", "10,000 to 20,000","more than 20,000"])
second_dropdown.pack()

# Create a button to handle the click event
button = tk.Button(root, text="Submit", command=handle_click)
button.pack()

# Run the main event loop
root.mainloop()