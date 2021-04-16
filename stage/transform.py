# Transfomration utility. Transforms source CSV values to reflect the desired values
from datetime import date


def transform_source_time_serie(mgr, obj):
    supported_keys = obj.definition.keys()
    stage_rows = []

    stage_row = {'uid': get_uid(mgr.lookup_objects, obj)}

    for key, value in obj.to_dict().items():
        if key not in supported_keys:
            month, day, year = key.split("_")
            year = "20" + year
            capture_date = date(int(year), int(month), int(day))

            _stage_row = {'capture_date': capture_date}
            if 'confirmed' in mgr.filename:
                _stage_row.update({'confirmed': value})
            elif 'deaths' in mgr.filename:
                _stage_row.update({'deaths': value})
            elif 'recovered' in mgr.filename:
                _stage_row.update({'recovered': value})
            stage_rows.append({**stage_row, **_stage_row})

    return stage_rows

def transform_source_daily_report(mgr, obj):
    stage_row = {'uid': get_uid(mgr.lookup_objects, obj)}
    return [{**obj.to_dict(), **stage_row}]

def transform_source_lookup(mgr, obj):
    return [obj.to_dict()]


def get_uid(lookup_objects, obj):
    for lookup_obj in lookup_objects:
        if lookup_obj.combined_key == obj.combined_key:
            return lookup_obj.uid
    return 0

