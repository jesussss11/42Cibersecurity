import datetime
kata = (2019, 9, 25, 3, 30)

fecha = datetime.datetime(kata[0], kata[1], kata[2], kata[3], kata[4])
fecha_formateada = fecha.strftime("%m/%d/%Y %H:%M")

print(fecha_formateada)