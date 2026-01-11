from operator import index
import psycopg2
from padg_lib.view import *
from padg_lib.model import airports, employees, clients

class Airport:
    def __init__(self, name:str, location: str, code: str, coords=None):
        self.name = name
        self.location = location
        self.code = code
        self.coords = coords if coords else self.get_coordinates()

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
    def __init__(self, name:str, surname: str, age: int, location: str, airport_code: str, coords=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.location = location
        self.airport = airport_code
        self.coords = coords if coords else self.get_coordinates()

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

class Client:
    def __init__(self, name:str, surname: str, age: int, location: str, arrival_code: str, departure_code: str, coords=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.location = location
        self.arrival_code = arrival_code
        self.departure_code = departure_code
        self.coords = coords if coords else self.get_coordinates()

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

mode = "null"

def switch_airports():
    global mode
    mode = "airports"

    label_1.grid()
    entry_1.grid()
    label_2.grid()
    entry_2.grid()
    label_3.grid()
    entry_3.grid()
    label_4.grid()
    entry_4.grid()
    label_5.grid()
    entry_5.grid()
    label_6.grid()
    entry_6.grid()

    label_1.config(text="Lotnisko: ")
    label_2.config(text="Miasto: ")
    label_3.config(text="KOD: ")

    label_4.grid_remove()
    entry_4.grid_remove()
    label_5.grid_remove()
    entry_5.grid_remove()
    label_6.grid_remove()
    entry_6.grid_remove()

    listbox_list.delete(0, END)

    for airport in airports:
        listbox_list.insert(END, f"{airport.name}")

    refresh_map()

    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_5.delete(0, END)
    entry_6.delete(0, END)

def switch_employees():
    global mode
    mode = "employees"

    label_1.grid()
    entry_1.grid()
    label_2.grid()
    entry_2.grid()
    label_3.grid()
    entry_3.grid()
    label_4.grid()
    entry_4.grid()
    label_5.grid()
    entry_5.grid()
    label_6.grid()
    entry_6.grid()

    label_1.config(text="Imię: ")
    label_2.config(text="Nazwisko: ")
    label_3.config(text="Wiek: ")
    label_4.config(text="Miasto: ")
    label_5.config(text="KOD: ")

    label_6.grid_remove()
    entry_6.grid_remove()

    listbox_list.delete(0, END)

    for employee in employees:
        listbox_list.insert(END, f"{employee.name} {employee.surname}")

    refresh_map()

    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_5.delete(0, END)
    entry_6.delete(0, END)

def switch_clients():
    global mode
    mode = "clients"

    label_1.grid()
    entry_1.grid()
    label_2.grid()
    entry_2.grid()
    label_3.grid()
    entry_3.grid()
    label_4.grid()
    entry_4.grid()
    label_5.grid()
    entry_5.grid()
    label_6.grid()
    entry_6.grid()

    label_1.config(text="Imię: ")
    label_2.config(text="Nazwisko: ")
    label_3.config(text="Wiek: ")
    label_4.config(text="Miasto: ")
    label_5.config(text="Przylot: ")
    label_6.config(text="Odlot: ")

    listbox_list.delete(0, END)

    for client in clients:
        listbox_list.insert(END, f"{client.name} {client.surname}")

    refresh_map()

    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_5.delete(0, END)
    entry_6.delete(0, END)

def add():
    l1 = entry_1.get()
    l2 = entry_2.get()
    l3 = entry_3.get()
    l4 = entry_4.get()
    l5 = entry_5.get()
    l6 = entry_6.get()

    if mode == "airports":
        airport = Airport(l1, l2, l3)
        airports.append(airport)
        listbox_list.insert(END, airport.name)
        map_widget.set_marker(airport.coords[0], airport.coords[1], text=airport.name)

        code_list = []
        for airport in airports:
            if airport.code not in code_list:
                code_list.append(airport.code)
        checkbox_filtr["values"] = code_list

    if mode == "employees":
        employee = Employee(l1, l2, l3, l4, l5)
        employees.append(employee)
        listbox_list.insert(END, f"{employee.name} {employee.surname}")
        map_widget.set_marker(employee.coords[0], employee.coords[1], text=f"{employee.name} {employee.surname}")

    if mode == "clients":
        client = Client(l1, l2, l3, l4, l5, l6)
        clients.append(client)
        listbox_list.insert(END, f"{client.name} {client.surname}")
        map_widget.set_marker(client.coords[0], client.coords[1], text=f"{client.name} {client.surname}")

    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_5.delete(0, END)
    entry_6.delete(0, END)

def update():
    index = listbox_list.curselection()[0]

    l1 = entry_1.get()
    l2 = entry_2.get()
    l3 = entry_3.get()
    l4 = entry_4.get()
    l5 = entry_5.get()
    l6 = entry_6.get()

    if mode == "airports":
        airport = Airport(l1, l2, l3)
        airports[index] = airport
        listbox_list.delete(index)
        listbox_list.insert(index, l1)
    if mode == "employees":
        employee = Employee(l1, l2, l3, l4, l5)
        employees[index] = employee
        listbox_list.delete(index)
        listbox_list.insert(index, f"{l1} {l2}")
    if mode == "clients":
        client = Client(l1, l2, l3, l4, l5, l6)
        clients[index] = client
        listbox_list.delete(index)
        listbox_list.insert(index, f"{l1} {l2}")

    refresh_map()

def refresh_map():
    map_widget.delete_all_marker()

    if mode == "airports":
        for airport in airports:
            map_widget.set_marker(airport.coords[0], airport.coords[1], text=airport.name)

    if mode == "clients":
        for client in clients:
            map_widget.set_marker(client.coords[0], client.coords[1], text=f"{client.name} {client.surname}")

    if mode == "employees":
        for employee in employees:
            map_widget.set_marker(employee.coords[0], employee.coords[1], text=f"{employee.name} {employee.surname}")


def delete():
    index = listbox_list.curselection()[0]

    if mode == "airports":
        airports.pop(index)
    if mode == "employees":
        employees.pop(index)
    if mode == "clients":
        clients.pop(index)

    listbox_list.delete(index)
    refresh_map()

def details():
    index = listbox_list.curselection()[0]

    if mode == "airports":
        airport = airports[index]
        map_widget.set_position(airport.coords[0], airport.coords[1])

    if mode == "employees":
        employee = employees[index]
        map_widget.set_position(employee.coords[0], employee.coords[1])

    if mode == "clients":
        client = clients[index]
        map_widget.set_position(client.coords[0], client.coords[1])

    map_widget.set_zoom(14)

def select(event):
    selection = listbox_list.curselection()

    index = selection[0]

    if mode == "airports":
        airport = airports[index]

        entry_1.delete(0, END)
        entry_1.insert(0, airport.name)

        entry_2.delete(0, END)
        entry_2.insert(0, airport.location)

        entry_3.delete(0, END)
        entry_3.insert(0, airport.code)

        entry_4.delete(0, END)
        entry_5.delete(0, END)
        entry_6.delete(0, END)

        map_widget.set_position(airport.coords[0], airport.coords[1])

    if mode == "employees":
        employee = employees[index]

        entry_1.delete(0, END)
        entry_1.insert(0, employee.name)

        entry_2.delete(0, END)
        entry_2.insert(0, employee.surname)

        entry_3.delete(0, END)
        entry_3.insert(0, employee.age)

        entry_4.delete(0, END)
        entry_4.insert(0, employee.location)

        entry_5.delete(0, END)
        entry_5.insert(0, employee.airport)

        entry_6.delete(0, END)

        map_widget.set_position(employee.coords[0], employee.coords[1])

    if mode == "clients":
        client = clients[index]

        entry_1.delete(0, END)
        entry_1.insert(0, client.name)

        entry_2.delete(0, END)
        entry_2.insert(0, client.surname)

        entry_3.delete(0, END)
        entry_3.insert(0, client.age)

        entry_4.delete(0, END)
        entry_4.insert(0, client.location)

        entry_5.delete(0, END)
        entry_5.insert(0, client.arrival_code)

        entry_6.delete(0, END)
        entry_6.insert(0, client.departure_code)

        map_widget.set_position(client.coords[0], client.coords[1])

    map_widget.set_zoom(15)

def filter():
    code = checkbox_filtr.get()

    listbox_list.delete(0, END)
    map_widget.delete_all_marker()

    if mode == "airports":
        for airport in airports:
            if airport.code == code:
                listbox_list.insert(END, airport.name)
                map_widget.set_marker(airport.coords[0], airport.coords[1], text=airport.name)
                map_widget.set_position(airport.coords[0], airport.coords[1])

    if mode == "employees":
        for employee in employees:
            if employee.airport == code:
                listbox_list.insert(END, f"{employee.name} {employee.surname}")
                map_widget.set_marker(employee.coords[0], employee.coords[1], text=f"{employee.name} {employee.surname}")
                map_widget.set_position(employee.coords[0], employee.coords[1])

    if mode == "clients":
        for client in clients:
            if client.arrival_code == code or client.departure_code == code:
                listbox_list.insert(END, f"{client.name} {client.surname}")
                map_widget.set_marker(client.coords[0], client.coords[1], text= f"{client.name} {client.surname}")
                map_widget.set_position(client.coords[0], client.coords[1])

    map_widget.set_zoom(15)

def load_db(db_engine):
    airports.clear()
    employees.clear()
    clients.clear()

    cursor = db_engine.cursor()

    cursor.execute("SELECT nazwa, miasto, kod, szerokosc, dlugosc FROM airports;")
    for row in cursor.fetchall():
        airports.append(Airport(row[0], row[1], row[2], coords=[row[3], row[4]]))

    cursor.execute("SELECT imie, nazwisko, wiek, miasto, kod_lotniska, szerokosc, dlugosc FROM employees;")
    for row in cursor.fetchall():
        employees.append(Employee(row[0], row[1], row[2], row[3], row[4], coords=[row[5], row[6]]))

    cursor.execute("SELECT imie, nazwisko, wiek, miasto, kod_przylotu, kod_odlotu, szerokosc, dlugosc FROM clients;")
    for row in cursor.fetchall():
        clients.append(Client(row[0], row[1], row[2], row[3], row[4], row[5], coords=[row[6], row[7]]))

    cursor.close()

def save_db(db_engine):
    cursor = db_engine.cursor()
    cursor.execute("TRUNCATE TABLE airports, employees, clients;")

    for airport in airports:
        cursor.execute("INSERT INTO airports (nazwa, miasto,kod, szerokosc, dlugosc) VALUES (%s, %s, %s, %s, %s)",
                       (airport.name, airport.location, airport.code, airport.coords[0], airport.coords[1]))

    for employee in employees:
        cursor.execute("INSERT INTO employees (imie, nazwisko, wiek, miasto, kod_lotniska, szerokosc, dlugosc) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (employee.name, employee.surname, employee.age, employee.location, employee.airport, employee.coords[0], employee.coords[1]))

    for client in clients:
        cursor.execute("INSERT INTO clients (imie, nazwisko, wiek, miasto, kod_przylotu, kod_odlotu, szerokosc, dlugosc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (client.name, client.surname, client.age, client.location, client.arrival_code, client.departure_code, client.coords[0], client.coords[1]))

    db_engine.commit()
    cursor.close()



