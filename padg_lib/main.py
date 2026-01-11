from padg_lib.controller import *
from padg_lib.view import root
import psycopg2

db_engine = psycopg2.connect(
    user="postgres",
    database="postgres",
    password="postgres",
    port="5432",
    host="localhost",
)

button_airports.config(command=switch_airports)
button_employees.config(command=switch_employees)
button_clients.config(command=switch_clients)
button_add.config(command=add)
button_delete.config(command=delete)
button_update.config(command=update)
button_filtr.config(command=filter)

listbox_list.bind('<<ListboxSelect>>', select)

load_db(db_engine)
def close():
    save_db(db_engine)
    db_engine.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close)

if __name__ == '__main__':
    load_db(db_engine)
    root.mainloop()
