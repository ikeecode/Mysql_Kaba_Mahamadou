from sys import exit
from themenu import menu

def affiche_menu(list_menu):
    for ind, item in enumerate(list_menu):
        print(f"{ind + 1}   | {item} ")

choice = ''
menus_popped = []

in_menu = menu.menus.copy()
def launcher(in_menu):
    global copy_menus
    try:
        copy_menus = in_menu.copy()
        while len(copy_menus) > 0:
            affiche_menu(copy_menus)
            choice = input("Choisir une operation: ")

            if choice.lower() == 'e':
                print("Ces taches ont deja été effectuées une fois au moins")
                # affiche_menu(menus_popped)
                launcher(menus_popped)
            elif choice.lower() == 'q':
                exit()
            elif choice.lower() == 'r':
                copy_menus = menu.menus.copy()
                launcher(copy_menus)
            elif choice.lower() != 'q':
                try:
                    choice = int(choice)
                    popped = copy_menus.pop(int(choice) - 1)
                    menus_popped.append(popped)
                    print(menu.sql_requests.get(popped))
                except:
                    launcher(copy_menus)

            print(170*"#")
        print("you're out ")

    except KeyboardInterrupt:
        print()
        print("you're out ")
        exit()


launcher(in_menu)
