#Guilherme Gonzaga Silva 11621EMT021 
#prog08.py

#1)
# def hello_func():
#     print('Hello Function')

# # print(hello_func) #<function hello_func at 0x00FB7850>
# # print(hello_func()) #None

# hello_func()
# hello_func()
# hello_func()
# hello_func()

#2)
# def hello_func():
#     return 'Hello Function'

# print(hello_func().upper())

#3)
# def hello_func(greeting, name='You'):
#     return '{}, {}'.format(greeting,name)

# # print(hello_func('Hi', name = 'Corey'))

#4)
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# courses = ['Math', 'Art']
# info = {'name': 'John', 'age': 22}

# student_info(courses, info)
# student_info(*courses, **info)

#5) Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))