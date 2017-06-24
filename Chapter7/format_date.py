import re

def date_formatter(date):
    """
    clean up dates in different formats
    such as 3/14/2015, 03-14-2015, and 2015/3/14 to standard format(yyyy/mm/dd)
    and return the list of date
    Assuming that month is always coming before date.
    """
    dateRegax = re.compile(r"""
        (\d|\d{2}|\d{4})
        (\s|-|/|\.)
        (\d|\d{2})
        (\s|-|/|\.)
        (\d{4}|\d{2})
        """, re.VERBOSE)
    print(dateRegax.findall(date))
    result = []
    for group in dateRegax.findall(date):
        y, m, d = 0, 0, 0
        if len(group[0]) == 4:
            y = group[0]
            m = group[2][1] if group[2][0] == "0" else group[2]
            d = group[4]
        else:
            y = group[4]
            m = group[0][1] if group[0][0] == "0" else group[0]
            d = group[0]
        date = y + "/" + m + "/" + d
        result.append(date)
    for date in result:
        print(date)
    return result

test_text = "12/25/0000, 10.21.1955, 10-21-1985 6-5-1995 2004/2/21 5/25/2111 4999.2.21 3/14/2015, 03-14-2015, and 2015/3/14 "
date_formatter(test_text)






