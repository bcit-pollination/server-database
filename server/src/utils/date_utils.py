from datetime import datetime


class TimeRelations:
    LFT_EARLIER = -1
    SIMULTANEOUS = 0
    LFT_LATER = 1


def compare_date_strings(ds1, ds2, datetime_format):
    """
    Compare 2 date strings.

    The strings are parsed using the specified datetime_format

    :returns: -1 if ds1 < ds2. 0 if ds1 == ds2. 1 if ds1 > ds2. Where greater means latest
    """
    date1 = datetime.strptime(ds1, datetime_format)
    date2 = datetime.strptime(ds2, datetime_format)
    if date1 == date2:
        return TimeRelations.SIMULTANEOUS
    if date1 < date2:
        return TimeRelations.LFT_EARLIER
    return TimeRelations.LFT_LATER
