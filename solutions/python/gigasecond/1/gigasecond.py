from datetime import datetime, timedelta

def add(moment):
    ONE_GIGA_SECOND = timedelta(seconds=1e9)
    result = moment + ONE_GIGA_SECOND
    return result