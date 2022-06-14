from datetime import datetime
from khayyam import JalaliDatetime

def compare_date(date1, date2) -> bool:
    time1 = datetime.strptime(date1, "%Y/%m/%d %H:%M:%S")
    time2 = datetime.strptime(date2, "%Y/%m/%d %H:%M:%S")
    return True if time1 > time2 else False

def to_gregorian_strftime(moment):
    dt = JalaliDatetime.strptime(moment, "%Y/%m/%d %H:%M:%S")
    return dt.todatetime().strftime("%Y/%m/%d %H:%M:%S")

def to_gregorian_date(moment):
    dt = JalaliDatetime.strptime(moment, "%Y/%m/%d")
    return dt.todate().strftime("%Y/%m/%d")