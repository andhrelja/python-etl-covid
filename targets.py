import config
import utils
from target.manager import Manager, TimeSeriesManager
from target.models import (
    TimeSeries, 
    DailyReports, 
    Lookup
)

from tqdm import tqdm


def check_time_series_created():
    return config.TARGET_TIME_SERIES.exists()

def check_daily_reports_created():
    source_dir = [path for path in config.STAGE_DAILY_REPORTS.iterdir() if path.suffix == ".csv" and path.exists()]
    target_dir = [path for path in config.TARGET_DAILY_REPORTS.iterdir() if path.suffix == ".csv" and path.exists()]
    return len(source_dir) == len(target_dir) and len(target_dir) > 0

def check_lookup_created():
    lookup_path = config.TARGET_LOOKUP_CSV
    return lookup_path.exists()

def load_time_series():
    print("Fetching Time Series ...")

    if check_time_series_created():
        print("DONE")
        return
    
    rows = []
    for filepath in tqdm(config.STAGE_TIME_SERIES):
        rows += utils.read_csv(filepath)
    manager = TimeSeriesManager(TimeSeries, rows)
    manager.combine_sources()
    manager.set_fieldnames()
    manager.write_objects(config.TARGET_TIME_SERIES)

def load_daily_reports():
    print("Fetching Daily Reports ...")

    if check_daily_reports_created():
        print("DONE")
        return
    
    iterdir = list(config.STAGE_DAILY_REPORTS.iterdir())
    for filepath in tqdm(iterdir):
        rows = utils.read_csv(filepath)
        manager = Manager(DailyReports, rows)
        manager.write_objects(config.TARGET_DAILY_REPORTS / filepath.name)
        

def load_lookup():
    print("Fetching Lookup ...")

    if check_lookup_created():
        print("DONE")
        return
    
    filepath = config.STAGE_LOOKUP_CSV
    for _ in tqdm([1]):
        rows = utils.read_csv(filepath)
        manager = Manager(Lookup, rows)
        manager.write_objects(config.TARGET_LOOKUP_CSV)
        
