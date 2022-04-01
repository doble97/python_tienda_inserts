import csv
from datetime import datetime
import mysql.connector
import fechas as f

# abrir conexion a bd
bd_conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='alumno2021',
    database='Tienda',
    port=7777
)

cursor = bd_conn.cursor()
trabajadores=[]
jorge=['50050050X','Jorge','Gonzalez Davila',9999.99,123456789987,f.get_date(1997,1,18).strftime('%Y-%m-%d %H:%M:%S'),f.get_date(2017,1,1).strftime('%Y-%m-%d %H:%M:%S')]
darwin=['50050051X','Darwin','Funcion',9999.99,123456789986,f.get_date(1996,5,28).strftime('%Y-%m-%d %H:%M:%S'),f.get_date(2017,1,1).strftime('%Y-%m-%d %H:%M:%S')]
dani=['50050052X','Dani','Sanz',9999.99,123456789985,f.get_date(1998,5,8).strftime('%Y-%m-%d %H:%M:%S'),f.get_date(2017,1,1).strftime('%Y-%m-%d %H:%M:%S')]
david = ['50050053X','Darwin','Funcion',9999.99,123456789984,f.get_date(1995,5,2).strftime('%Y-%m-%d %H:%M:%S'),f.get_date(2017,1,1).strftime('%Y-%m-%d %H:%M:%S')]
trabajadores.append(jorge)
trabajadores.append(darwin)
trabajadores.append(dani)
trabajadores.append(david)

sentencia = 'insert into Trabajadores(pk_dni, nombre, apellidos, sueldo, uk_nss, fecha_nacimiento, fecha_contratacion) values (%s,%s,%s,%s,%s,%s,%s)'
# abrir y leer fichero
for x in trabajadores:
    cursor.execute(sentencia, x)
bd_conn.commit()