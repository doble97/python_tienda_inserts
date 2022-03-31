import datetime
from random import randint, random
timestampt_to_date = lambda x: datetime.datetime.fromtimestamp(x)
date_to_timestampt= lambda x: datetime.datetime.timestamp(x)
get_date = lambda y,m,d:datetime.datetime(y,m,d)
# def limit_timestamp_fnac(): return int(date_to_timestampt(datetime.datetime(2000,1,1)))
# def init_timestamp_falta():return int(date_to_timestampt(datetime.datetime(2018,1,1)))
def getFechaNacimiento(limit_right=date_to_timestampt(get_date(2000,1,1))):
    n = randint(0,limit_right)    
    fecha = timestampt_to_date(n).strftime('%Y-%m-%d %H:%M:%S')
    return fecha
def getFechaAlta(limit_left=date_to_timestampt(get_date(2018,1,1))):
    n = randint(limit_left, int(date_to_timestampt(datetime.datetime.now())))
    fecha = timestampt_to_date(n).strftime('%Y-%m-%d %H:%M:%S')
    return fecha

