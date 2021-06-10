def recipe():
    name = input("Recipe name: ")
    ing = input("Ingredients: ")
    ins = input("Instructions: ")
    rec = name.capitalize() + '\n\n'+ing.title()+'\n'+ins.title()

    with open(name, 'w') as file:
        content = file.write(rec)

recipe()

