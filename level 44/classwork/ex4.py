def twice_as_old(dad_years_old, son_years_old):
    years = dad_years_old - 2 * son_years_old
    if years < 0:
        return -years
    return years