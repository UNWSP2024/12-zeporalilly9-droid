# Program #3: Long-Distance Calls
# Author: Zepora Lilly
# Date: 11/21/2025

import tkinter as tk
from tkinter import messagebox
rates = {
    "Daytime": 0.02,
    "Evening": 0.12,
    "Off-Peak": 0.05
}

def calculate_charge():
    try:
        minutes = float(minutes_entry.get())
        rate = rates[rate_var.get()]
        charge = minutes * rate
        messagebox.showinfo("Call Charge", f"Charge: ${charge:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of minutes.")
    
root = tk.Tk()
root.title("Long-Distance Call Calculator")

rate_var = tk.StringVar(value="Daytime")
tk.Label(root, text="Select Rate Category:").pack()
for category in rates:
    tk.Radiobutton(root,text=f"{category} (${rates[category]:.2f}/min)", variable=rate_var, value=category).pack(anchor='w')

tk.Label(root, text="Minutes:").pack()
minutes_entry = tk.Entry(root)
minutes_entry.pack()

tk.Button(root, text="Calculate Charge", command=calculate_charge).pack()

root.mainloop()
    