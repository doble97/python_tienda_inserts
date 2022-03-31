import os
nombre_os=os.name
if nombre_os == 'nt':
    os.system('python inserts_clientes.py')
    os.system('python inserts_trabajadores.py')
else:
    os.system('python3 inserts_clientes.py')
    os.system('python3 inserts_trabajadores.py')