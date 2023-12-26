














import json

# Your JSON data
data = '''
{
    "class": "Warrior",
    "name": "Eric Rodriguez",
    "hp": 52,
    "mp": 10,
    "strength": 12,
    "dexterity": 8,
    "intelligence": 4,
    "experience": 0,
    "level": 0,
    "statusEffect": null,
    "equipment": {
        "head": null,
        "chest": null,
        "legs": null,
        "boots": null,
        "hands": null,
        "weapon": null,
        "offhand": null,
        "neck": null,
        "ring": null
    }
}
'''

# Parse JSON data
parsed_data = json.loads(data)

# Get the value of the "class" attribute
character_class = parsed_data['class']

# Print the extracted class
print(character_class)

