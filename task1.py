import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# --- Conversion Functions ---
def celsius_to_fahrenheit(c): return (c * 9/5) + 32
def celsius_to_kelvin(c): return c + 273.15
def fahrenheit_to_celsius(f): return (f - 32) * 5/9
def fahrenheit_to_kelvin(f): return (f - 32) * 5/9 + 273.15
def kelvin_to_celsius(k): return k - 273.15
def kelvin_to_fahrenheit(k): return (k - 273.15) * 9/5 + 32

# --- Conversion Logic ---
def convert_temperature(event=None):
    try:
        value_str = entry_temp.get().strip()
        if not value_str:
            messagebox.showwarning("Input Missing", "Please enter a temperature.")
            return
        value = float(value_str)
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit == to_unit:
            result_var.set(f"{value:.2f} {to_unit}")
            return

        if from_unit == "Celsius":
            result = celsius_to_fahrenheit(value) if to_unit == "Fahrenheit" else celsius_to_kelvin(value)
        elif from_unit == "Fahrenheit":
            result = fahrenheit_to_celsius(value) if to_unit == "Celsius" else fahrenheit_to_kelvin(value)
        else:
            result = kelvin_to_celsius(value) if to_unit == "Celsius" else kelvin_to_fahrenheit(value)

        result_var.set(f"{result:.2f} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def clear_fields():
    entry_temp.delete(0, 'end')
    combo_from.set("Celsius")
    combo_to.set("Fahrenheit")
    result_var.set("")

# --- GUI Setup ---
app = ttk.Window(themename="darkly")  # Options: flatly, darkly, morph, solar, etc.
app.title("🌡️ Modern Temperature Converter")
app.geometry("420x400")
app.resizable(False, False)

app.update_idletasks()
width, height = app.winfo_width(), app.winfo_height()
x = (app.winfo_screenwidth() // 2) - (width // 2)
y = (app.winfo_screenheight() // 2) - (height // 2)
app.geometry(f"+{x}+{y}")

# Title
ttk.Label(app, text="🌡️ Temperature Converter", font=("Segoe UI", 18, "bold")).pack(pady=20)

# Frame
frame = ttk.Frame(app, padding=20)
frame.pack(fill='both', expand=True)

# Entry
ttk.Label(frame, text="Enter Temperature:", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=5)
entry_temp = ttk.Entry(frame, font=("Segoe UI", 10), width=20)
entry_temp.grid(row=0, column=1, pady=5)
entry_temp.bind("<Return>", convert_temperature)

# Comboboxes
units = ["Celsius", "Fahrenheit", "Kelvin"]

ttk.Label(frame, text="From Unit:", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", pady=5)
combo_from = ttk.Combobox(frame, values=units, bootstyle="dark", state="readonly", width=22)
combo_from.set("Celsius")
combo_from.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="To Unit:", font=("Segoe UI", 10)).grid(row=2, column=0, sticky="w", pady=5)
combo_to = ttk.Combobox(frame, values=units, bootstyle="dark", state="readonly", width=22)
combo_to.set("Fahrenheit")
combo_to.grid(row=2, column=1, pady=5)

# Buttons
ttk.Button(frame, text="Convert", bootstyle="success-outline", width=20, command=convert_temperature).grid(row=3, column=0, columnspan=2, pady=15)
ttk.Button(frame, text="Clear", bootstyle="secondary", width=20, command=clear_fields).grid(row=4, column=0, columnspan=2)

# Result
result_var = ttk.StringVar()
ttk.Label(frame, textvariable=result_var, font=("Segoe UI", 12, "bold"), foreground="#44bd32").grid(row=5, column=0, columnspan=2, pady=15)

frame.grid_columnconfigure(1, weight=1)

app.mainloop()
