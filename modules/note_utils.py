
# notes = {}
# def create_note():
#     title = input("Enter Title:").lower()
#     if title in notes:
#         print("Already exists")
#     else:
#         content = input("Content : ")
#         notes[title] = content

# def read_note():
#     title = input("Enter the note name : ").lower()
#     if title in notes:
#         print(notes[title])
#     else:
#         print("No such note exits")

# def update_note():
#     title = input("Which note you want to update:").lower()
    
#     if title in notes:
#         content = input("Enter the updated content:")
#         notes[title] = content
#     else:
#         print("No such note exists")

# def delete_note():
#     title = input("Enter name of the note to be deleted:").lower()
#     if title in notes:
#         print("Deleted",notes[title])
#         del notes[title]
#     else:
#         print("No such note exists")



import json
import os

NOTES_FILE = "notes.json"

# Load notes from the file (at program start)
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    return {}

# Save notes to the file
def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

notes = load_notes()

def create_note():
    title = input("Enter Title: ").strip().lower()
    if title in notes:
        print("Note already exists.")
    else:
        content = input("Enter Content: ").strip()
        notes[title] = content
        save_notes(notes)
        print("Note saved.")

def read_note():
    title = input("Enter the note name: ").strip().lower()
    if title in notes:
        print(f"\n{title.upper()}:\n{notes[title]}")
    else:
        print("No such note exists.")

def update_note():
    title = input("Which note you want to update: ").strip().lower()
    if title in notes:
        content = input("Enter the updated content: ").strip()
        notes[title] = content
        save_notes(notes)
        print("Note updated.")
    else:
        print("No such note exists.")

def delete_note():
    title = input("Enter name of the note to delete: ").strip().lower()
    if title in notes:
        del notes[title]
        save_notes(notes)
        print("Note deleted.")
    else:
        print("No such note exists.")

def list_notes():
    if not notes:
        print("No notes available.")
    else:
        print("\nYour Notes:")
        for i, title in enumerate(notes, 1):
            print(f"{i}. {title}")


