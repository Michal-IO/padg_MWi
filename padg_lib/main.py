from padg_lib.model import airports, employees
from padg_lib.controller import *

def main():
    while True:
        print('================ SYSTEM LOTNISKOWY ================')
        print('1. Wyświetl wszystkie lotniska')
        print('2. Dodaj nowe lotnisko')
        print('3. Usuń lotnisko')
        print('4. Aktualizuj dane lotniska')
        print('0. Wyjście')
        print('===================================================')

        tmp_choice = input('Wybierz opc1ję:')

        if tmp_choice == '0':
            break
        if tmp_choice == '1':
            print('Wybrano funkcje wyświetlania lotnisk')
            airport_info(airports)
        if tmp_choice == '2':
            print('Wybrano funckcje dodawania lotnisk')
            add_airport(airports)
        if tmp_choice == '3':
            print('Wybrano funkcje usuwania lotnisk')
            delete_airport(airports)
        if tmp_choice == '4':
            print('Wybrano funkcje aktualizowania lotnisk')
            update_airport(airports)
if __name__ == '__main__':
    main()
