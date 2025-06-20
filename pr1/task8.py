def func(date):

    year, month, day = date.split('-')
    return {
        'year': year,
        'month': month,
        'day': day
    }

date = '2025-12-31'
date_dict = func(date)
print(date_dict)