from datetime import datetime as dt

current_datetime = dt.now()
formatted_date = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
print("Output1:\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!\nOutput2:\nCurrent date and time :\n%s", formatted_date)
