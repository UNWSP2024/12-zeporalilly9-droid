# Program #1:MPG Calculator
# Author: Zepora Lilly
# Date: 11/21/2025

import tkinter as tk

def calculate_mpg():
    try:
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())
        mpg = miles / gallons
        result_label.config(text=f"MPG: {mpg:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

root = tk.Tk()
root.title("MPG Calculator")

tk.Label(root, text="Gallons of gas:").pack()
gallons_entry = tk.Entry(root)
gallons_entry.pack()

tk.Label(root, text="Miles driven:").pack()
miles_entry = tk.Entry(root)
miles_entry.pack()

tk.Button(root, text="Calculate MPG", command=calculate_mpg).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()