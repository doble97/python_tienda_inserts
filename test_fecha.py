from datetime import datetime
import random
import fechas as fechas
last = int(fechas.date_to_timestampt(datetime.now()))
l_times = []
for x in range(0,20):
    n = random.randint(0, last)
    l_times.append(n)
l_dates = []
for x in l_times:
    l_dates.append(fechas.timestampt_to_date(x))

for x in range(len(l_times)):
    print(l_times[x], '--->', l_dates[x])