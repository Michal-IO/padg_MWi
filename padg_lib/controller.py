

class Airport:
    def __init__(self, name:str, location: str, code: str):
        self.name = name
        self.location = location
        self.code = code
        self.coords = self.get_coordinates()

    def get_coordinates(self):
            import requests
            from bs4 import BeautifulSoup
            url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/123.0.0.0 Safari/537.36"
            }
            response = requests.get(url, headers=headers)
            # print(response.text)
            response_html = BeautifulSoup(response.text, "html.parser")
            # print(response_html.prettify())
            latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
            # print(latitude)
            longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
            # print(longitude)
            return [latitude, longitude]

class Employee:
    def __init__(self, name:str, surname: str, location: str, airport: str):
        self.name = name
        self.surname = surname
        self.location = location
        self.airport = airport
        self.coords = self.get_coordinates()

    def get_coordinates(self):
            import requests
            from bs4 import BeautifulSoup
            url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/123.0.0.0 Safari/537.36"
            }
            response = requests.get(url, headers=headers)
            # print(response.text)
            response_html = BeautifulSoup(response.text, "html.parser")
            # print(response_html.prettify())
            latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
            # print(latitude)
            longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
            # print(longitude)
            return [latitude, longitude]


def add_airport(airports_list: list):
    print('Dodawanie lotnisk...')
    name = input('Wprowadź nazwe lotniska: ')
    location = input('Wprowadź miasto: ')
    code = input('Wprowadź kod lotniska: ')
    print("Lotnisko dodane")
    airports_list.append(Airport(name, location, code))

def airport_info(airports_list: list):
    for airport in airports_list:
        print(f'Lotnisko {airport.name} w miejscowości {airport.location}')

def delete_airport(airports_list: list):
    tmp_name = input('Wprowadz nazwe lotniska do usunięcia: ')
    for airport in airports_list:
        if airport.name == tmp_name:
            airports_list.remove(airport)

def update_airport(airports_list: list):
    tmp_name = input('Wprowadź nazwe: ')
    for airport in airports_list:
        if airport.name == tmp_name:
            airport.name = input('Wprowadź nazwe: ')
            airport.location = input('Wprowadź miasto: ')
            airport.code = input('Wprowadź kod lotniska: ')
            airport.coords = airport.get_coordinates()

def add_employee(employees_list: list):
    print('Dodawanie pracowników...')
    name = input('Wprowadź imię: ')
    surname = input('Wprowadź nazwisko: ')
    location = input('Wprowadź miasto: ')
    airport = input('Wprowadź nazwę lotniska: ')
    employees_list.append(Employee(name, surname, location, airport))

def employee_info(employees_list: list):
    for employee in employees_list:
        print(f'Pracownik {employee.name} {employee.surname}, z miejscowości {employee.location}, na lotnisku {employee.airport}')

def delete_employee(employees_list: list):
    tmp_name = input('Wprowadź imię: ')
    for employee in employees_list:
        if employee.name == tmp_name:
            employees_list.remove(employee)

def update_employee(employees_list: list):
    tmp_name = input('Wprowadź imię: ')
    for employee in employees_list:
        if employee.name == tmp_name:
            employee.name = input('Wprowadź imię: ')
            employee.surname = input('Wprowadź nazwisko: ')
            employee.location = input('Wprowadź miasto: ')
            employee.airport = input('Wprowadź lotnisko: ')
            employee.coords = employee.get_coordinates()

