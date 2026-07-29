from notes import add_note, view_notes, delete_note

while True:
    print("\n====== QuickNotesX ======")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Title: ")
        content = input("Content: ")
        add_note(title, content)

    elif choice == "2":
        view_notes()

    elif choice == "3":
        note_id = int(input("Note number to delete: "))
        delete_note(note_id)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
