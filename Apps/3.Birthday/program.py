import datetime
from datetime import date


def print_header():
    print('-------------------------------------')
    print('         Compute Birthdays')
    print('-------------------------------------')
    print()


def capture_bday():
    year = int(input('Enter the year you were born [YYYY]: '))
    month = int(input('What month were you born? [MM]: '))
    day = int(input('What day were you born? [DD]: '))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    target_bday = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = target_date - target_bday
    return dt.days


def print_bday_info(birthday, difference):
    if difference < 0:
        print('I have calculated that your birthday {}, occurred {} days ago.'.format(birthday, -difference))
    elif difference > 0:
        print('I have calculated your birthday, {}, will occur in {} days'.format(birthday, difference))
    else:
        print('Happy Birthday!')
    pass


def main():
    print_header()
    bday = capture_bday()
    today: date = datetime.date.today()
    number_of_days = compute_days_between_dates(today, bday)
    print_bday_info(bday, number_of_days)

main()