from datetime import datetime, date

def create_datetime(datetime_str):
    if isinstance(datetime_str, datetime):
        return datetime_str
    
    if "/" in datetime_str:
        try:
            return datetime.strptime(datetime_str, '%m/%d/%Y %H:%M')
        except ValueError:
            return datetime.strptime(datetime_str, '%m/%d/%y %H:%M')
    else:
        try:
            return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            if "T" in datetime_str:
                return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
            else:
                return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')

def create_date(date_str):
    if isinstance(date_str, date):
        return date_str
    
    if '-' in date_str:
        year, month, day = date_str.split('-')
    elif '.' in date_str:
        day, month, year = date_str.split('.')
    return date(int(year), int(month), int(day))
    