import tkinter as tk
from tkinter import ttk
from GuiMainFile.CharactersGui import character_recruitment, party_gui, party_inventory_gui


def game_run():
    root = tk.Tk()
    root.title("Main Page")

    def open_recruit_characters():
        root.withdraw()  # Hide the main window
        character_recruitment.character_recruit_gui_run(root)  # Pass 'root' as an argument

    def open_display_items():
        root.withdraw()
        party_inventory_gui.display_items_gui()

    def open_party_gui_and_hide_main():
        party_gui.party_gui(root)  # Open party GUI
        root.withdraw()  # Hide the main window

    # Create buttons and place them using grid layout
    recruit_characters_button = ttk.Button(root, text="Recruit Characters", command=open_recruit_characters)
    recruit_characters_button.grid(row=0, column=0, padx=20, pady=10)

    display_characters_button = ttk.Button(root, text="Party", command=open_party_gui_and_hide_main)
    display_characters_button.grid(row=1, column=0, padx=20, pady=10)

    items_characters_button = ttk.Button(root, text="Open inventory", command=open_display_items)
    items_characters_button.grid(row=2, column=0, padx=20, pady=10)

    root.mainloop()


game_run()
