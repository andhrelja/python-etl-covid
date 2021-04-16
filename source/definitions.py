from .clean import clean_value, create_combined_key

# Data tranformation
DAILY_REPORTS_TRANSFORM = {
    'combined_key':         lambda x, y: create_combined_key(x, y),
    'capture_date':         lambda x: x,
    'province_state':       lambda x: clean_value(x),
    'country_region':       lambda x: clean_value(x),
    'fips':                 lambda x: clean_value(x),
    'admin2':               lambda x: clean_value(x),
    'lat':                  lambda x: x if x else 0.0,
    'long':                 lambda x: x if x else 0.0,
    'last_update':          lambda x: x if x else 0,
    'confirmed':            lambda x: x if x else 0,
    'deaths':               lambda x: x if x else 0,
    'recovered':            lambda x: x if x else 0,
    'active':               lambda x: x if x else 0,
    'incident_rate':        lambda x: x if x else 0.0,
    'case_fatality_ratio':  lambda x: x if x and not x.startswith("#") else 0.0
}


TIME_SERIES_TRANSFORM = {
    'combined_key':     lambda x, y: create_combined_key(x, y),
    'capture_date':     lambda x: x,
    'province_state':   lambda x: x,
    'country_region':   lambda x: x,
    'lat':              lambda x: x if x else 0.0,
    'long':             lambda x: x if x else 0.0,
}

LOOKUP_TRANSFORM = {
    'uid':              lambda x: x,
    'capture_date':     lambda x: x,
    'combined_key':     lambda x, y: create_combined_key(x, y),
    'province_state':   lambda x: clean_value(x),
    'country_region':   lambda x: clean_value(x),
    'iso2':             lambda x: clean_value(x),
    'iso3':             lambda x: clean_value(x),
    'code3':            lambda x: x if x else 0,
    'fips':             lambda x: clean_value(x),
    'admin2':           lambda x: clean_value(x),
    'lat':              lambda x: x if x else 0.0,
    'long':             lambda x: x if x else 0.0,
    'population':       lambda x: x if x else 0
}
