def note():
    name = input("Title: ")
    note = input("Notes: ")
    
    rec = name.upper() + '\n\n'+note.title()

    with open(name, 'w') as file:
        content = file.write(rec)

note()

