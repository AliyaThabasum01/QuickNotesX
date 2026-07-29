import json
import os
from datetime import datetime

FILE = "notes.json"

def load_notes():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_notes(notes):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=4)

def add_note(title, content):
    notes = load_notes()
    notes.append({
        "title": title,
        "content": content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_notes(notes)
    print("✅ Note added!")

def view_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return

    print("\n📝 Notes\n")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note['title']}")
        print(f"   {note['content']}")
        print(f"   Created: {note['created_at']}")
        print()

def delete_note(note_id):
    notes = load_notes()

    if 1 <= note_id <= len(notes):
        removed = notes.pop(note_id - 1)
        save_notes(notes)
        print(f"🗑️ Deleted: {removed['title']}")
    else:
        print("❌ Invalid note number.")
