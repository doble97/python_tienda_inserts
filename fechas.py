import datetime
from random import randint, random
timestampt_to_date = lambda x: datetime.datetime.fromtimestamp(x)
date_to_timestampt= lambda x: datetime.datetime.timestamp(x)
def limit_timestamp_fnac(): return int(date_to_timestampt(datetime.datetime(2000,1,1)))
def init_timestamp_falta():return int(date_to_timestampt(datetime.datetime(2018,1,1)))
def getFechaNacimiento():
    n = randint(0,limit_timestamp_fnac())    
    fecha = timestampt_to_date(n).strftime('%Y-%m-%d %H:%M:%S')
    return fecha
def getFechaAlta():
    n = randint(init_timestamp_falta(), int(date_to_timestampt(datetime.datetime.now())))
    fecha = timestampt_to_date(n).strftime('%Y-%m-%d %H:%M:%S')
    return fecha