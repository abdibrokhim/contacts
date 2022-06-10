import user


class Menu:
    def main_menu(self):
        while True:
            print('\nCHOOSE AN OPTION\n')
            print('[1] -> CONTINUE')
            print('[0] -> EXIT\n')

            choice = input("[?] -> ")
            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                self.secondary_menu()
            elif choice == 0:
                exit()
            else:
                print("\nINVALID")

    def secondary_menu(self):
        while True:
            print('\nCHOOSE AN OPTION\n')
            print('[1] -> ADD NEW CONTACT')
            print('[2] -> UPDATE CONTACT')
            print('[3] -> DELETE CONTACT')
            print('[4] -> SEE ALL CONTACTS')
            print('\n[0] -> BACK\n')

            choice = input("[?] -> ")
            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                user.User().add_contact()
            elif choice == 2:
                user.User().update_contact()
            elif choice == 3:
                user.User().delete_contact()
            elif choice == 4:
                user.User().get_contact()
            elif choice == 0:
                return False
            else:
                print("\nINVALID")