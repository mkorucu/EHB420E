from datetime import datetime as dt

current_datetime = dt.now()

formatted_date = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
print(formatted_date)
