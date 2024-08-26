import datetime as dt
import pandas as pd

def ls_to_ls_of_ls(ls, row_length):

    ls_of_ls = [ls[i:i+row_length] for i in range(0, len(ls), row_length)]

    return ls_of_ls

def points_half_ppr_QB(td, yd, intcpt, fum_lost, two_pt_conv):
   
   points = float(td) * 4.0 + float(yd) / 25.0 - float(intcpt) - float(fum_lost) * 2.0 + float(two_pt_conv) * 2.0

   return points

def points_half_ppr_K(fg_39, fg_49, fg_lng, fg_miss, xtra_made, xtra_miss):

    points = float(fg_39) * 3.0 + float(fg_49) * 4.0 + float(fg_lng) * 5.0 - float(fg_miss) + float(xtra_made) - float(xtra_miss)

    return points

def points_half_ppr_RB_WR_TE(td, yd, rec, fum_lost, two_pt_conv):

    points = float(td) * 6.0 + float(yd) / 10.0 + float(rec) * 0.5 - float(fum_lost) * 2.0 + float(two_pt_conv) * 2.0

    return points

def calculate_age(birthdate, date):

    years = date.year - birthdate.year - ((date.month, date.day) < (birthdate.month, birthdate.day))
    
    if (date.month, date.day) < (birthdate.month, birthdate.day):
        time_to_birthday = dt.datetime(date.year, birthdate.month, birthdate.day) - dt.datetime(date.year, date.month, date.day)
        age = years + (365 - time_to_birthday.days) / 365
    else:
        time_after_birthday = dt.datetime(date.year, date.month, date.day) - dt.datetime(date.year, birthdate.month, birthdate.day)
        age = years + time_after_birthday.days / 365

    return round(age, 2)
