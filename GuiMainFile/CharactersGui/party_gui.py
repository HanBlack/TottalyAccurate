import tkinter as tk
import json
import os
import glob
from tkinter import messagebox
import program

variable_for_path = program.current_directory()


def display_character_info(character_data, frame, column):
    file_name = os.path.basename(character_data["class"])

    header_label = tk.Label(frame, text=file_name, font=("Arial", 12, "bold"))
    header_label.grid(row=0, column=column, columnspan=2, pady=5)

    stat_font = ("Arial", 12)
    info_labels = [
        f"Name: {character_data['name']}",
        f"HP: {character_data['hp']}",
        f"MP: {character_data['mp']}",
        f"Strength: {character_data['strength']}",
        f"Dexterity: {character_data['dexterity']}",
        f"Intelligence: {character_data['intelligence']}",
        f"Experience: {character_data['experience']}",
        f"Level: {character_data['level']}",
        f"Status Effect: {character_data['statusEffect']}" if character_data['statusEffect'] else "Status Effect: None"
    ]

    # Equipment information
    equipment_info = "Equipment:"
    for slot, item in character_data['equipment'].items():
        equipment_info += f"\n{slot.capitalize()}: {item if item else 'None'}"

    info_labels.append(equipment_info)

    for i, info in enumerate(info_labels):
        label = tk.Label(frame, text=info, font=stat_font)
        label.grid(row=i + 1, column=column, sticky="w")


def load_character_data(file_path):
    with open(file_path, 'r') as file:
        character_data = json.load(file)
        return character_data


def display_character_gui_all(json_files):
    if json_files:
        root = tk.Tk()
        root.title("All Characters Details")

        num_columns = 3
        current_row = 0
        current_column = 0

        for file_path in json_files:
            character_data = load_character_data(file_path)

            main_frame = tk.Frame(root)
            main_frame.grid(row=current_row, column=current_column, padx=10, pady=10)

            display_character_info(character_data, main_frame, current_column)  # Include the column argument

            current_column += 1
            if current_column >= num_columns:
                current_row += 1
                current_column = 0

        root.mainloop()
    else:
        messagebox.showinfo("No Characters Found", "No JSON files found in the directory.")


def display_character_gui():
    path = variable_for_path
    current_directory = os.path.join(path, 'Character', 'CharacterSave')
    json_files = glob.glob(os.path.join(current_directory, '*.json'))
    display_character_gui_all(json_files)

