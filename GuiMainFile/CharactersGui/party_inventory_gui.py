import tkinter as tk
import json
import os
import glob
from tkinter import messagebox
import program

variable_for_path = program.current_directory()


def load_item_data(file_path):
    with open(file_path, 'r') as file:
        item_data = json.load(file)
        return item_data


def display_item_info(item_data, frame, column):
    file_name = item_data["Name"]

    header_label = tk.Label(frame, text=file_name, font=("Arial", 12, "bold"))
    header_label.grid(row=0, column=column, columnspan=2, pady=5)

    stat_font = ("Arial", 12)
    info_labels = [
        f"Name: {item_data['Name']}",
        f"Damage: {item_data['Damage'] if item_data['Damage'] else 'None'}",
        f"Armour: {item_data['Armour'] if item_data['Armour'] else 'None'}",
        f"Strength Bonus: {item_data['Strength Bonus'] if item_data['Strength Bonus'] else 'None'}",
        f"Dexterity Bonus: {item_data['Dexterity Bonus'] if item_data['Dexterity Bonus'] else 'None'}",
        f"Intelligence Bonus: {item_data['Intelligence Bonus'] if item_data['Intelligence Bonus'] else 'None'}",
        f"HP Bonus: {item_data['HP Bonus'] if item_data['HP Bonus'] else 'None'}",
        f"MP Bonus: {item_data['MP Bonus'] if item_data['MP Bonus'] else 'None'}"
    ]

    for i, info in enumerate(info_labels):
        label = tk.Label(frame, text=info, font=stat_font)
        label.grid(row=i + 1, column=column, sticky="w")


def display_items_gui_all(json_files):
    if json_files:
        root = tk.Tk()
        root.title("All Items Details")

        num_columns = 3
        current_row = 0
        current_column = 0

        for file_path in json_files:
            item_data = load_item_data(file_path)

            main_frame = tk.Frame(root)
            main_frame.grid(row=current_row, column=current_column, padx=10, pady=10)

            display_item_info(item_data, main_frame, current_column)

            current_column += 1
            if current_column >= num_columns:
                current_row += 1
                current_column = 0

        root.mainloop()
    else:
        messagebox.showinfo("No Items Found", "No JSON files found in the inventory directory.")


def display_items_gui():
    path = variable_for_path
    current_directory = os.path.join(path, 'Character', 'CharacterSave', 'CharacterInventory')
    json_files = glob.glob(os.path.join(current_directory, '*.json'))
    display_items_gui_all(json_files)
