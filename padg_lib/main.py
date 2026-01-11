from padg_lib.model import airports, employees, clients
from padg_lib.controller import *
from padg_lib.view import root


button_airports.config(command=switch_airports)
button_employees.config(command=switch_employees)
button_clients.config(command=switch_clients)
button_add.config(command=add)
button_delete.config(command=delete)
button_update.config(command=update)
button_filtr.config(command=filter)

listbox_list.bind('<<ListboxSelect>>', select)

if __name__ == '__main__':
    root.mainloop()
