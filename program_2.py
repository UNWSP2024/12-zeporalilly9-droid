# Program #2: Joe's Automotive
# Author: Zepora Lilly
# Date: 11/21/2025

import tkinter as tk

services = {
    "Oil Change": 30.0,
    "Lube Job": 20.0,
    "Radiator Flush": 40.0,
    "Transmission Fluid": 100.0,
    "Inspection": 35.0,
    "Muffler Replacement": 200.0,
    "Tire Rotation": 20.0
}

def calculate_total():
    total = sum(price for service, price in service.items() if vars[service].get())
    result_label.config(text=f"Total Charges: ${total:.2f}")

root = tk.Tk()
root.title("Joe's Automotive")

vars = {}
for service in services:
    vars[service] = tk.BooleanVar()
    tk.Checkbutton(root, text=f"{service} - ${services[service]:.2f}", variable=vars[service]).pack(anchor='w')

tk.Button(root, text="Calculate Total", command=calculate_total). pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
