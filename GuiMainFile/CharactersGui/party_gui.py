import json
import tkinter as tk
from Character import character


def load_character_date(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data


