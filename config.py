from pathlib import Path

BASE_PATH = Path("C:\\Users\\AndreaHrelja\\AndroidStudioProjects\\CovidAplikacija\\app\\src\\main\\scripts")

ROOT_DATA_FOLDER = BASE_PATH / 'data'
SOURCE_DATA_FOLDER = BASE_PATH / 'source' / 'data'
STAGE_DATA_FOLDER = BASE_PATH / 'stage' / 'data'
TARGET_DATA_FOLDER = BASE_PATH / 'target' / 'data'

# Source Data
ROOT_LOOKUP_CSV = ROOT_DATA_FOLDER / 'UID_ISO_FIPS_LookUp_Table.csv'
SOURCE_LOOKUP_CSV = SOURCE_DATA_FOLDER / 'lookup.csv'
STAGE_LOOKUP_CSV = STAGE_DATA_FOLDER / 'lookup.csv'
TARGET_LOOKUP_CSV = TARGET_DATA_FOLDER / 'lookup.csv'

# Daily Reports
ROOT_DAILY_REPORTS = ROOT_DATA_FOLDER / 'csse_covid_19_daily_reports'
SOURCE_DAILY_REPORTS = SOURCE_DATA_FOLDER / 'daily_reports'
STAGE_DAILY_REPORTS = STAGE_DATA_FOLDER / 'daily_reports'
TARGET_DAILY_REPORTS = TARGET_DATA_FOLDER / 'daily_reports'

# Time Series
ROOT_TIME_SERIES = [
    ROOT_DATA_FOLDER / 'csse_covid_19_time_series' / 'time_series_covid19_confirmed_global.csv',
    ROOT_DATA_FOLDER / 'csse_covid_19_time_series' / 'time_series_covid19_deaths_global.csv',
    ROOT_DATA_FOLDER / 'csse_covid_19_time_series' / 'time_series_covid19_recovered_global.csv'
]

SOURCE_TIME_SERIES = [
    SOURCE_DATA_FOLDER / 'time_series' / 'confirmed_global.csv',
    SOURCE_DATA_FOLDER / 'time_series' / 'recovered_global.csv',
    SOURCE_DATA_FOLDER / 'time_series' / 'deaths_global.csv'
]

STAGE_TIME_SERIES = [
    STAGE_DATA_FOLDER / 'time_series' / 'confirmed_global.csv',
    STAGE_DATA_FOLDER / 'time_series' / 'recovered_global.csv',
    STAGE_DATA_FOLDER / 'time_series' / 'deaths_global.csv'
]

TARGET_TIME_SERIES = TARGET_DATA_FOLDER / 'time_series' / 'time_series_global.csv'
