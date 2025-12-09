from tkinter import *
from tkinter import ttk
import tkintermapview


root = Tk()
root.title('=== SYSTEM LOTNISKOWY ===')
root.geometry('1200x700')
root.configure(bg='black')

top_frame = Frame(root, height=50)
left_frame = Frame(root, width=400)
right_frame = Frame(root)

top_frame.grid(row=0, column=0, columnspan=2, sticky=EW)
left_frame.grid(row=1,column=0, sticky=NS)
right_frame.grid(row=1,column=1, sticky=NSEW)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

#GÓRNA CZĘŚĆ

top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=1)
top_frame.grid_columnconfigure(2, weight=1)


button_airports = Button(top_frame, text = 'LOTNISKA', width=15)
button_airports.grid(row=0, column=0, sticky=EW)

button_employees = Button(top_frame, text = 'PRACOWNICY', width=15)
button_employees.grid(row=0, column=1, sticky=EW)

button_clients = Button(top_frame, text = 'KLIENCI', width=15)
button_clients.grid(row=0, column=2, sticky=EW)

#LEWA CZĘŚĆ

label_head = Label(left_frame, text='FORMULARZ')
label_head.grid(row=0, column=0, columnspan=2)

label_name = Label(left_frame, text = 'Imię: ')
label_name.grid(row=1, column=0, sticky=W)
entry_name = Entry(left_frame, width=25)
entry_name.grid(row=1, column=1, sticky=EW)

label_surname = Label(left_frame, text = 'Nazwisko: ')
label_surname.grid(row=2, column=0, sticky=W)
entry_surname = Entry(left_frame, width=25)
entry_surname.grid(row=2, column=1, sticky=EW)

label_city = Label(left_frame, text = 'Miasto: ')
label_city.grid(row=3, column=0, sticky=W)
entry_city = Entry(left_frame, width=25)
entry_city.grid(row=3, column=1, sticky=EW)

label_code = Label(left_frame, text = 'Kod Lotniska: ')
label_code.grid(row=4, column=0, sticky=W)
entry_code = Entry(left_frame, width=25)
entry_code.grid(row=4, column=1, sticky=EW)

button_add = Button(left_frame, text = 'DODAJ', width=25)
button_add.grid(row=5, column=0, columnspan=2, sticky=EW)

button_update = Button(left_frame, text = 'AKTUALIZUJ', width=25)
button_update.grid(row=6, column=0, columnspan=2, sticky=EW)

button_delete = Button(left_frame, text='USUŃ', width=25)
button_delete.grid(row=7, column=0, columnspan=2, sticky=EW)

Frame(left_frame, height=2).grid(row=8, column=0, columnspan=2, sticky=EW)

filter_frame = Frame(left_frame)
filter_frame.grid(row=9, column=0, columnspan=2, sticky=EW)

label_list = Label(filter_frame, text='LISTA: ')
label_list.grid(row=0, column=0, sticky=W)

label_filtr = Label(filter_frame, text = 'Filtruj: ')
label_filtr.grid(row=0, column=1, sticky=W)

checkbox_filtr = ttk.Combobox(filter_frame, values=["KODY"])
checkbox_filtr.grid(row=0, column=2, sticky=W)
checkbox_filtr.current(0)


list_frame = Frame(left_frame)
list_frame.grid(row=10, column=0, columnspan=2, sticky=NSEW)

left_frame.grid_rowconfigure(10, weight=1)
list_frame.grid_rowconfigure(0, weight=1)
list_frame.grid_columnconfigure(0, weight=1)

listbox_list = Listbox(list_frame)
listbox_list.grid(row=0, column=0, sticky=NSEW)

scrollbar = Scrollbar(list_frame)
scrollbar.grid(row=0, column=1, sticky=NS)

listbox_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox_list.yview)

# PRAWA CZĘŚĆ

right_frame.grid_rowconfigure(0, weight=1)
right_frame.grid_rowconfigure(1, weight=0)
right_frame.grid_columnconfigure(0, weight=1)

map_frame = Frame(right_frame)
map_frame.grid(row=0, column=0, sticky=NSEW)

map_widget = tkintermapview.TkinterMapView(map_frame, width=600, height=400, corner_radius=0)
map_widget.pack(fill=BOTH, expand=True)
map_widget.set_position(52.2,21.0)
map_widget.set_zoom(6)



