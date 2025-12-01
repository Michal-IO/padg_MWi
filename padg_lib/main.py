from padg_lib.model import airports, employees
from padg_lib.controller import *

def main():
    while True:
        print('================ SYSTEM LOTNISKOWY ================')
        print('1. Zarządzanie Lotniskami')
        print('2. Zarządzanie Pracownikami')
        print('0. Wyjście')
        print('===================================================')

        tmp_choice = input('Wybierz opcję: ')
        if tmp_choice == '0':
          break

        if tmp_choice == '1':
            while True:
                print('Wybrano funkcje zarządzania lotniskami')
                print('================ SYSTEM ZARZADZANIA LOTNISKAMI ================')
                print('1. Wyświetl wszystkie lotniska')
                print('2. Dodaj nowe lotnisko')
                print('3. Usuń lotnisko')
                print('4. Aktualizuj dane lotniska')
                print('0. Powrót')
                print('===============================================================')

                sub_choice = input('Wybierz opcję: ')

                if sub_choice == '0':
                    break
                if sub_choice == '1':
                    print('Wybrano funkcje wyświetlania lotnisk')
                    airport_info(airports)
                if sub_choice == '2':
                    print('Wybrano funkcję dodania nowego lotniska')
                    add_airport(airports)
                if sub_choice == '3':
                    print('Wybrano funkcje usunięcia lotniska')
                    delete_airport(airports)
                if sub_choice == '4':
                    print('Wybrano funkcje aktualizacji lotniska')
                    update_airport(airports)

        if tmp_choice == '2':
            while True:
                print('Wybrano funkcje zarządzania pracownikami')
                print('================ SYSTEM ZARZADZANIA PRACOWNIKAMI ================')
                print('1. Wyświetl wszystkich pracowników')
                print('2. Dodaj nowego pracownika')
                print('3. Usuń pracownika')
                print('4. Aktualizuj dane pracownika')
                print('0. Powrót')
                print('==================================================================')

                sub_choice2 = input('Wybierz opc1ję:')

                if sub_choice2 == '0':
                    break
                if sub_choice2 == '1':
                    print('Wybrano funkcje wyświetlania pracowników')
                    employee_info(employees)
                if sub_choice2 == '2':
                    print('Wybrano funckcje dodawania pracowników')
                    add_employee(employees)
                if sub_choice2 == '3':
                    print('Wybrano funkcje usuwania pracowników')
                    delete_employee(employees)
                if sub_choice2 == '4':
                    print('Wybrano funkcje aktualizowania pracowników')
                    update_employee(employees)
if __name__ == '__main__':
    main()
