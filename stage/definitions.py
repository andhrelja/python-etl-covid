from datetime import datetime, date
from target.clean import create_date, create_datetime

# Data definition
DAILY_REPORTS_DEFINITION = {
    'uid':                  int,
    'combined_key':         str,
    'capture_date':         date,
    'fips':                 str,
    'admin2':               str,
    'last_update':          datetime,
    'confirmed':            int,
    'deaths':               int,
    'recovered':            int,
    'active':               int,
    'incident_rate':        float,
    'case_fatality_ratio':  float,
}

TIME_SERIES_DEFINITION = {
    'uid':          int,
    'combined_key': str,
    'capture_date': date,
    'confirmed':    int,
    'recovered':    int,
    'deaths':       int
}

LOOKUP_DEFINITION = {
    'uid':              int,
    'capture_date':     date,
    'combined_key':     str,
    'province_state':   str,
    'country_region':   str,
    'iso2':             str,
    'iso3':             str,
    'code3':            int,
    'fips':             str,
    'admin2':           str,
    'lat':              float,
    'long':             float,
    'population':       int,
}

# Data tranformation
DAILY_REPORTS_TRANSFORM = {
    'uid':                  lambda x: int(x),
    'combined_key':         lambda x: str(x),
    'capture_date':         lambda x: create_date(x),
    'fips':                 lambda x: str(x),
    'admin2':               lambda x: str(x),
    'last_update':          lambda x: create_datetime(x),
    'confirmed':            lambda x: int(x),
    'deaths':               lambda x: int(x),
    'recovered':            lambda x: int(x) if isinstance(x, int) else int(float(x)),
    'active':               lambda x: int(x),
    'incident_rate':        lambda x: float(x),
    'case_fatality_ratio':  lambda x: float(x)
}


TIME_SERIES_TRANSFORM = {
    'uid':              lambda x: int(x),
    'combined_key':     lambda x: str(x),
    'capture_date':     lambda x: create_date(x),
    'confirmed':        lambda x: int(x),
    'recovered':        lambda x: int(x),
    'deaths':           lambda x: int(x)
}

LOOKUP_TRANSFORM = {
    'uid':              lambda x: int(x),
    'capture_date':     lambda x: create_date(x),
    'combined_key':     lambda x: str(x),
    'province_state':   lambda x: str(x),
    'country_region':   lambda x: str(x),
    'iso2':             lambda x: str(x),
    'iso3':             lambda x: str(x),
    'code3':            lambda x: int(x),
    'fips':             lambda x: str(x),
    'admin2':           lambda x: str(x),
    'lat':              lambda x: float(x),
    'long':             lambda x: float(x),
    'population':       lambda x: int(x)
}
