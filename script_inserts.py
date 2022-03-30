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

with open('csv/users.csv') as file:
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