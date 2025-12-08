from padg_lib.model import airports, employees, clients
from padg_lib.controller import *

def main():
    while True:
        print('================ SYSTEM LOTNISKOWY ================')
        print('1. Zarządzanie Lotniskami')
        print('2. Zarządzanie Pracownikami')
        print('3. Zarzadzanie klientami')
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
                print('5. Zarządzanie kadrą wybranego lotniska')
                print('6. Zarządzanie klientami wybranego lotniska')
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
                if sub_choice == '5':
                    airport_code = input("Podaj kod lotniska: ")

                    airport_exist = False
                    for airport in airports:
                        if airport.code == airport_code:
                            airport_exist = True
                            break
                    if not airport_exist:
                        print(f'Błąd: Lotnisko o kodzie [{airport_code}] nie istnieje')
                        print('Najpierw dodaj lotnisko do listy')
                    else:
                        while True:
                            print(f'=== SYSTEM ZARZADZANIA PRACOWNIKAMI LOTNISKA [{airport_code}] ===')
                            print('1. Wyświetl pracowników lotniska')
                            print('2. Dodaj pracownika do tego lotniska')
                            print('3. Usuń pracownika z tego lotniska')
                            print('4. Edytuj pracownika tego lotniska')
                            print('0. Wróc do menu lotnisk')

                            employee_choice = input('Wybierz opcje: ')

                            if employee_choice == '0':
                                break
                            if employee_choice == '1':
                                employee_in_airport_info(employees, airport_code)
                            if employee_choice == '2':
                                add_employee_to_airport(employees, airport_code)
                            if employee_choice == '3':
                                delete_employee_from_airport(employees, airport_code)
                            if employee_choice == '4':
                                update_employee_in_airport(employees, airport_code)
                if sub_choice == '6':
                    airport_code = input('Podaj kod kod lotniska: ')
                    airport_exist = False
                    for airport in airports:
                        if airport.code == airport_code:
                            airport_exist = True
                            break
                    if not airport_exist:
                        print(f'Błąd: Lotnisko o kodzie [{airport_code}] nie istnieje')
                        print('Najpierw dodaj lotnisko do listy')
                    else:
                        while True:
                            print(f'=== KLIENCIE LOTNISKA [{airport_code}] ===')
                            print('1. Wyświetl klientów tego lotniska')
                            print('2. Dodaj klienta do tego lotniska')
                            print('3. Usuń klienta z tego lotniska')
                            print('4. Edytuj klienta tego lotniska')
                            print('0. Wróć do menu lotnisk')

                            client_choice = input('Wybierz opcje: ')
                            if client_choice == '0':
                                break
                            if client_choice == '1':
                                client_in_airport_info(clients, airport_code)
                            if client_choice == '2':
                                add_client_to_airport(clients, airport_code)
                            if client_choice == '3':
                                delete_client_from_airport(clients, airport_code)
                            if client_choice == '4':
                                update_client_in_airport(clients, airport_code)



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

                sub_choice = input('Wybierz opc1ję:')

                if sub_choice == '0':
                    break
                if sub_choice == '1':
                    print('Wybrano funkcje wyświetlania pracowników')
                    employee_info(employees)
                if sub_choice == '2':
                    print('Wybrano funckcje dodawania pracowników')
                    add_employee(employees, airports)
                if sub_choice == '3':
                    print('Wybrano funkcje usuwania pracowników')
                    delete_employee(employees)
                if sub_choice == '4':
                    print('Wybrano funkcje aktualizowania pracowników')
                    update_employee(employees)

        if tmp_choice == '3':
            while True:
                print('===== MENU KLIENTOW =====')
                print('1. Wyświetl klientów')
                print('2. Dodaj klienta')
                print('3. Usuń klienta')
                print('4. Aktualizuj klienta')
                print('0. Powrót')

                sub_choice = input('Wybierz opcje: ')
                if sub_choice == '0':
                    break
                if sub_choice == '1':
                    client_info(clients)
                if sub_choice == '2':
                    add_client(clients, airports)
                if sub_choice == '3':
                    delete_client(clients)
                if sub_choice == '4':
                    update_client(clients)

if __name__ == '__main__':
    main()
