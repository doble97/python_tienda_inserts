import csv
import mysql.connector
import fechas as f

# abrir conexion a bd
bd_conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='alumno2021',
    database='Tienda'
)

cursor = bd_conn.cursor()
sentencia = 'insert into Trabajadores(pk_dni, nombre, apellidos, sueldo, uk_nss, fecha_nacimiento, fecha_contratacion) values (%s,%s,%s,%s,%s,%s,%s)'
# abrir y leer fichero
with open('csv/trabajadores.csv') as file:
    reader_csv = csv.reader(file)
    header = []
    header = next(reader_csv)
    print(header)
    for row in reader_csv:
        row.append(f.getFechaNacimiento())
        row.append(f.getFechaAlta())
        cursor.execute(sentencia, row)
bd_conn.commit()
print(cursor.rowcount, 'record inserted')