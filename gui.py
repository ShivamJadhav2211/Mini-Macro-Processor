import tkinter as tk
from tkinter import messagebox

from pass1 import pass1
from pass2 import pass2
from tables import MNT, MDT

def run_macro():

    input_text = input_box.get("1.0", tk.END)
    lines = input_text.strip().split("\n")

    # Clear old tables
    MNT.clear()
    MDT.clear()

    # Run Pass 1
    if not pass1(lines):
        messagebox.showerror("Error", "Pass 1 failed")
        return

    # Run Pass 2
    result = pass2(lines)

    if result:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "\n".join(result))


# GUI Window
root = tk.Tk()
root.title("MiniMacro Processor")
root.geometry("900x650")

title = tk.Label(root, text="MiniMacro Processor",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)

# Input Label
tk.Label(root, text="Input Program").pack()

# Input Box
input_box = tk.Text(root, height=15, width=100)
input_box.pack(pady=5)

# Run Button
run_btn = tk.Button(root,
                    text="Run Macroprocessor",
                    font=("Arial", 12, "bold"),
                    command=run_macro)

run_btn.pack(pady=10)

# Output Label
tk.Label(root, text="Output").pack()

# Output Box
output_box = tk.Text(root, height=15, width=100)
output_box.pack(pady=5)

root.mainloop()