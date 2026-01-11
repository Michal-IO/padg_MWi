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

label_1 = Label(left_frame, text = '...')
label_1.grid(row=1, column=0, sticky=W)
entry_1 = Entry(left_frame, width=25)
entry_1.grid(row=1, column=1, sticky=EW)

label_2 = Label(left_frame, text = '...')
label_2.grid(row=2, column=0, sticky=W)
entry_2 = Entry(left_frame, width=25)
entry_2.grid(row=2, column=1, sticky=EW)

label_3 = Label(left_frame, text = '...')
label_3.grid(row=3, column=0, sticky=W)
entry_3 = Entry(left_frame, width=25)
entry_3.grid(row=3, column=1, sticky=EW)

label_4 = Label(left_frame, text = '...')
label_4.grid(row=4, column=0, sticky=W)
entry_4 = Entry(left_frame, width=25)
entry_4.grid(row=4, column=1, sticky=EW)

label_5 = Label(left_frame, text = '...')
label_5.grid(row=5, column=0, sticky=W)
entry_5 = Entry(left_frame, width=25)
entry_5.grid(row=5, column=1, sticky=EW)

label_6 = Label(left_frame, text = '...')
label_6.grid(row=6, column=0, sticky=W)
entry_6 = Entry(left_frame, width=25)
entry_6.grid(row=6, column=1, sticky=EW)

button_add = Button(left_frame, text = 'DODAJ', width=25)
button_add.grid(row=7, column=0, columnspan=2, sticky=EW)

button_update = Button(left_frame, text = 'AKTUALIZUJ', width=25)
button_update.grid(row=8, column=0, columnspan=2, sticky=EW)

button_delete = Button(left_frame, text='USUŃ', width=25)
button_delete.grid(row=9, column=0, columnspan=2, sticky=EW)

Frame(left_frame, height=2).grid(row=10, column=0, columnspan=2, sticky=EW)

filter_frame = Frame(left_frame)
filter_frame.grid(row=10, column=0, columnspan=2, sticky=EW)

label_list = Label(filter_frame, text='LISTA: ')
label_list.grid(row=0, column=0, sticky=W)

label_filtr = Label(filter_frame, text = 'Filtruj: ')
label_filtr.grid(row=0, column=1, sticky=W)

checkbox_filtr = ttk.Combobox(filter_frame, values=["KODY"])
checkbox_filtr.grid(row=0, column=2, sticky=W)
checkbox_filtr.current(0)

button_filtr = Button(filter_frame, text='FILTR', width=5)
button_filtr.grid(row=0, column=3)


list_frame = Frame(left_frame)
list_frame.grid(row=11, column=0, columnspan=2, sticky=NSEW)

left_frame.grid_rowconfigure(11, weight=1)
list_frame.grid_rowconfigure(0, weight=1)
list_frame.grid_columnconfigure(0, weight=1)

listbox_list = Listbox(list_frame, exportselection=False)
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



