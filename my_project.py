"""From Prompt to Program: a small event budget app."""
import math
import tkinter as tk
from tkinter import ttk

def calculate():
    """Read the fields and update the result when the button is clicked."""
    try:
        attendees = int(attendees_entry.get())
        food = float(food_entry.get())
        supplies = float(supplies_entry.get())
        budget = float(budget_entry.get())
        if attendees <= 0:
            raise ValueError
        if not all(math.isfinite(value) and value >= 0 for value in [food, supplies, budget]):
            raise ValueError
    except (ValueError, OverflowError):
        result_label.config(text="Please check your numbers.", fg="#9C2727")
        detail_label.config(text="Use a whole number of attendees above zero.\nCosts and budget must be zero or more.")
        return

    total = round(attendees * food + supplies, 2)
    if not math.isfinite(total):
        result_label.config(text="Those numbers are too large.", fg="#9C2727")
        detail_label.config(text="Try smaller costs and calculate again.")
        return
    remaining = round(budget - total, 2)
    result_label.config(text="Total cost: $" + format(total, ",.2f"), fg="#17324D")
    if remaining >= 0:
        detail_label.config(text="Within budget. Remaining: $" + format(remaining, ",.2f"), fg="#176441")
    else:
        detail_label.config(text="Over budget by $" + format(abs(remaining), ",.2f"), fg="#9C2727")

window = tk.Tk()
window.title("From Prompt to Program | Event Budget Planner")
window.geometry("560x620")
window.minsize(500, 580)
window.configure(bg="#F3F6FA")

frame = tk.Frame(window, bg="#F3F6FA", padx=32, pady=24)
frame.pack(fill="both", expand=True)
tk.Label(frame, text="Your event. Your budget.", font=("Arial", 23, "bold"),
         bg="#F3F6FA", fg="#17324D").pack(anchor="w")
tk.Label(frame, text="Plan a club event, workshop, or celebration.",
         font=("Arial", 11), bg="#F3F6FA", fg="#44556A").pack(anchor="w", pady=(6, 18))

tk.Label(frame, text="Number of attendees", bg="#F3F6FA", font=("Arial", 11)).pack(anchor="w")
attendees_entry = ttk.Entry(frame, font=("Arial", 13))
attendees_entry.pack(fill="x", pady=(4, 10))
attendees_entry.insert(0, "20")

tk.Label(frame, text="Food cost per person ($)", bg="#F3F6FA", font=("Arial", 11)).pack(anchor="w")
food_entry = ttk.Entry(frame, font=("Arial", 13))
food_entry.pack(fill="x", pady=(4, 10))
food_entry.insert(0, "10")

tk.Label(frame, text="Supplies and other costs ($)", bg="#F3F6FA", font=("Arial", 11)).pack(anchor="w")
supplies_entry = ttk.Entry(frame, font=("Arial", 13))
supplies_entry.pack(fill="x", pady=(4, 10))
supplies_entry.insert(0, "50")

tk.Label(frame, text="Available budget ($)", bg="#F3F6FA", font=("Arial", 11)).pack(anchor="w")
budget_entry = ttk.Entry(frame, font=("Arial", 13))
budget_entry.pack(fill="x", pady=(4, 16))
budget_entry.insert(0, "300")

tk.Button(frame, text="Calculate my event", command=calculate, font=("Arial", 13, "bold"),
          bg="#1768A6", fg="white", padx=12, pady=9).pack(fill="x")
result_label = tk.Label(frame, text="Your estimate will appear here.", font=("Arial", 18, "bold"),
                        bg="#F3F6FA", fg="#17324D", wraplength=440)
result_label.pack(pady=(20, 6))
detail_label = tk.Label(frame, text="Try planning for 20 people with $300.",
                        font=("Arial", 12), bg="#F3F6FA", fg="#44556A", wraplength=440)
detail_label.pack()

attendees_entry.focus_set()
window.bind("<Return>", lambda event: calculate())
window.mainloop()
