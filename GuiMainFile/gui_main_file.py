import tkinter as tk
from tkinter import ttk
from GuiMainFile.CharactersGui import character_recruitment, party_gui, party_inventory_gui

def game_run():
    root = tk.Tk()
    root.title("Main Page")

    style = ttk.Style()
    party_window = None  # Initialize the party window variable

    def open_recruit_characters():
        root.withdraw()  # Hide the main window
        character_recruitment.character_recruit_gui_run(root)  # Pass 'root' as an argument

    def open_display_items():
        root.withdraw()
        party_inventory_gui.display_items_gui()

    def open_party_gui_and_hide_main():
        party_gui.party_gui(root)  # Open party GUI
        root.withdraw()  # Hide the main window

    recruit_characters_button = ttk.Button(root, text="Recruit Characters", command=open_recruit_characters)
    recruit_characters_button.pack(padx=20, pady=10)

    display_characters_button = ttk.Button(root, text="Party", command=lambda: open_party_gui_and_hide_main())
    display_characters_button.pack(padx=20, pady=10)

    items_characters_button = ttk.Button(root, text="Open inventory", command=open_display_items)
    items_characters_button.pack(padx=20, pady=10)

    root.mainloop()

game_run()
