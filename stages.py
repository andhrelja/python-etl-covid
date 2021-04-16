import config
import utils
from stage.manager import (
    TimeSeriesManager,
    DailyReportsManager,
    LookupManager
)

from tqdm import tqdm


def check_time_series_created():
    source_dir = [path for path in config.SOURCE_TIME_SERIES if path.suffix == ".csv" and path.exists()]
    stage_dir = [path for path in config.STAGE_TIME_SERIES if path.suffix == ".csv" and path.exists()]
    return len(source_dir) == len(stage_dir) and len(stage_dir) > 0

def check_daily_reports_created():
    source_dir = [path for path in config.SOURCE_DAILY_REPORTS.iterdir() if path.suffix == ".csv"]
    stage_dir = [path for path in config.STAGE_DAILY_REPORTS.iterdir() if path.suffix == ".csv"]
    return len(source_dir) == len(stage_dir) and len(stage_dir) > 0

def check_lookup_created():
    lookup_path = config.STAGE_LOOKUP_CSV
    return lookup_path.exists()

def ingest_time_series(lookup_objects):
    print("Fetching Time Series ...")

    if check_time_series_created():
        print("DONE")
        return
    
    for i, filepath in enumerate(tqdm(config.SOURCE_TIME_SERIES)):
        rows = utils.read_csv(filepath)
        manager = TimeSeriesManager(rows, filepath.name, lookup_objects)
        manager.transform_objects()
        manager.write_objects(config.STAGE_TIME_SERIES[i])


def ingest_daily_reports(lookup_objects):
    print("Fetching Daily Reports ...")

    if check_daily_reports_created():
        print("DONE")
        return
    
    iterdir = list(path for path in config.SOURCE_DAILY_REPORTS.iterdir() if path.suffix == '.csv')
    for filepath in tqdm(iterdir):
        rows = utils.read_csv(filepath)
        manager = DailyReportsManager(rows, filepath.name, lookup_objects)
        manager.transform_objects()
        manager.write_objects(config.STAGE_DAILY_REPORTS / filepath.name)


def ingest_lookup(source_daily_reports_mgrs, source_time_series_mgrs):
    print("Fetching Lookup ...")

    if check_lookup_created():
        print("DONE")
        rows = utils.read_csv(config.STAGE_LOOKUP_CSV)
        manager = LookupManager(rows, config.STAGE_LOOKUP_CSV.name)
        return manager
    
    rows = utils.read_csv(config.SOURCE_LOOKUP_CSV)
    manager = LookupManager(rows, config.SOURCE_LOOKUP_CSV.name)
    
    print("Update non-existent Daily Reports ...")    
    for mgr in tqdm(source_daily_reports_mgrs):
        manager.update_non_existent(mgr)
    
    print("Update non-existent Time Series ...")        
    for mgr in tqdm(source_time_series_mgrs):
        manager.update_non_existent(mgr)
    
    manager.write_objects(config.STAGE_LOOKUP_CSV)
    return manager
