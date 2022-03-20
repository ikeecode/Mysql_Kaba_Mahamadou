from sys import exit
from themenu import menu
import mysql.connector as mc



def affiche_menu(list_menu):
    for ind, item in enumerate(list_menu):
        print(f"{ind + 1}   | {item} ")

choice = ''
# menus_popped = []

in_menu = menu.menus.copy()
def launcher(in_menu):
    menus_popped = []
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
                    with mc.connect(option_files="my1.ini") as mydb:
                        mycursor = mydb.cursor()
                        choice = int(choice)
                        popped = copy_menus.pop(int(choice) - 1)
                        menus_popped.append(popped)
                        selected = menu.sql_requests.get(popped)
                        print(selected)
                        mycursor.execute(selected)
                        result = mycursor.fetchall()
                        mx = max([len(str(r)) for r in result])
                        print()
                        affiche_menu(result)
                        # for res in result:
                        #     print(mx * '_')
                        #     print(res)
                        print()
                except:
                    launcher(copy_menus)

            print(170*"#")
        print("you're out ")

    except KeyboardInterrupt:
        print()
        print("you're out ")
        exit()


launcher(in_menu)
