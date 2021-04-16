import config
import utils
from source.manager import Manager
from source.models import (
    TimeSeriesSource, 
    DailyReportsSource, 
    LookupSource
)

from tqdm import tqdm


def check_time_series_created():
    root_dir = [path for path in config.ROOT_TIME_SERIES if path.suffix == ".csv" and path.exists()]
    source_dir = [path for path in config.SOURCE_TIME_SERIES if path.suffix == ".csv" and path.exists()]
    return len(root_dir) == len(source_dir) and len(source_dir) > 0

def check_daily_reports_created():
    root_dir = [path for path in config.ROOT_DAILY_REPORTS.iterdir() if path.suffix == ".csv"]
    source_dir = [path for path in config.SOURCE_DAILY_REPORTS.iterdir() if path.suffix == ".csv"]
    return len(root_dir) == len(source_dir) and len(source_dir) > 0

def check_lookup_created():
    lookup_path = config.SOURCE_LOOKUP_CSV
    return lookup_path.exists()

def ingest_time_series():
    print("Fetching Time Series ...")
    managers = []

    if check_time_series_created():
        for i, filepath in enumerate(tqdm(config.SOURCE_TIME_SERIES)):
            rows = utils.read_csv(filepath)
            manager = Manager(TimeSeriesSource, rows)
            managers.append(manager)
        return managers
    
    
    for i, filepath in enumerate(tqdm(config.ROOT_TIME_SERIES)):
        rows = utils.read_csv(filepath)
        manager = Manager(TimeSeriesSource, rows)
        manager.set_combined_keys()
        manager.set_fieldnames()
        manager.write_objects(config.SOURCE_TIME_SERIES[i])
        managers.append(manager)
    return managers


def ingest_daily_reports():
    print("Fetching Daily Reports ...")
    managers = []

    if check_daily_reports_created():
        for filepath in tqdm(list(config.SOURCE_DAILY_REPORTS.iterdir())):
            rows = utils.read_csv(filepath)
            manager = Manager(DailyReportsSource, rows)
            managers.append(manager)
        return managers
    
    
    iterdir = list(path for path in config.ROOT_DAILY_REPORTS.iterdir() if path.suffix == '.csv')
    for filepath in tqdm(iterdir):
        rows = utils.read_csv(filepath)
        manager = Manager(DailyReportsSource, rows)
        manager.set_combined_keys()
        manager.set_fieldnames()
        manager.write_objects(config.SOURCE_DAILY_REPORTS / filepath.name)
        managers.append(manager)
    return managers


def ingest_lookup():
    print("Fetching Lookup ...")

    if check_lookup_created():
        print("DONE")
        return
    
    for _ in tqdm([1]):
        rows = utils.read_csv(config.ROOT_LOOKUP_CSV)
        manager = Manager(LookupSource, rows)
        manager.write_objects(config.SOURCE_LOOKUP_CSV)
