import sources
import stages
import targets

if __name__ == '__main__':
    
    print("*"*8, "Source ingestion", "*"*8)
    sources.ingest_lookup()
    source_time_series_mgrs = sources.ingest_time_series()
    source_daily_reports_mgrs = sources.ingest_daily_reports()
    print("*"*8, "----------------", "*"*8, "\n")
    
    print("*"*8, "Stage load", "*"*8)
    lookup_manager = stages.ingest_lookup(source_time_series_mgrs, source_daily_reports_mgrs)
    stages.ingest_time_series(lookup_manager.object_list)
    stages.ingest_daily_reports(lookup_manager.object_list)
    print("*"*8, "----------------", "*"*8, "\n")

    
    print("*"*8, "Target load", "*"*8)
    targets.load_lookup()
    targets.load_time_series()
    targets.load_daily_reports()
    print("*"*8, "----------------", "*"*8, "\n")
    