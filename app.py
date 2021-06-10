def note():
    name = input("Title: ")
    note = input("Notes: ")
    
    rec = name.capitalize() + '\n\n'+note.title()

    with open(name, 'w') as file:
        content = file.write(rec)

note()

