import csv
import mysql.connector
import fechas as f

bbdd = mysql.connector.connect(
    host='localhost',
    user='root',
    password='alumno2021',
    database='Tienda'
)

mycursor= bbdd.cursor()
sql = 'insert into Clientes (nombre, apellidos,dni, f_nac, f_alta) values (%s, %s, %s,%s,%s )'

#Clientes naceran antes del 2000 y estaran dados de alta desde el 2018 que se abre la empresa
with open('csv/clientes.csv') as file:
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        row.append(f.getFechaNacimiento())
        row.append(f.getFechaAlta())
        print(row)
        mycursor.execute(sql, row)

bbdd.commit()
print(mycursor.rowcount, 'record inserted')