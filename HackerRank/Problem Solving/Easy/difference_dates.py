from datetime import date


def calc_days(start, end):

    start_split = list(map(int, start.split("-")))
    end_split = list(map(int, end.split("-")))

    start_date = date(start_split[2], start_split[0], start_split[1])
    end_date = date(end_split[2], end_split[0], end_split[1])

    difference = end_date - start_date

    return difference.days

    