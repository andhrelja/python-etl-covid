import utils
from .transform import (
    transform_source_time_serie,
    transform_source_daily_report,
    transform_source_lookup,
)

from .models import (
    TimeSeriesStage,
    DailyReportsStage,
    LookupStage
)


class BaseManager(object):
    model = None
    transformation = None

    def __init__(self, rows, filename, lookup_objects=None):
        if self.transformation is None and self.model is None:
            raise ValueError("BaseManager should be used with a transformation function and a model attribute")
        
        self.lookup_objects = lookup_objects
        self.filename = filename
        self.dict_list = rows
        self.object_list = []

        self.set_objects()
        
    def set_objects(self):
        for kwargs in self.dict_list:
            obj = self.model(**kwargs)
            self.object_list.append(obj)
    
    def set_fieldnames(self):
        header = self.object_list[0].to_dict()
        self.fieldnames = list(header.keys())

    def get_objects(self):
        assert len(self.object_list) != 0
        return self.object_list

    def get_fieldnames(self):
        return self.fieldnames

    def transform_objects(self):
        stage_object_list = []
        for obj in self.get_objects():
            stage_rows = self.transformation(obj)
            stage_objects = self.create_stage_objects(stage_rows)
            stage_object_list += stage_objects
        self.object_list = stage_object_list
    
    def create_stage_objects(self, stage_rows):
        stage_objects = []
        for kwargs in stage_rows:
            stage_obj = self.model(**kwargs)
            stage_objects.append(stage_obj)
        return stage_objects
    
    def write_objects(self, filepath):
        self.set_fieldnames()

        utils.write_csv(
            filepath,
            utils.generate_rows(self.object_list),
            self.fieldnames
        )


class TimeSeriesManager(BaseManager):
    model = TimeSeriesStage
    transformation = transform_source_time_serie


class DailyReportsManager(BaseManager):
    model = DailyReportsStage
    transformation = transform_source_daily_report


class LookupManager(BaseManager):
    model = LookupStage
    transformation = transform_source_lookup

    def update_non_existent(self, mgr):
        for obj in mgr.get_objects():
            if obj.combined_key not in self.get_combined_keys():
                kwargs = {
                    'uid': self.get_max_uid(),
                    'capture_date': obj.capture_date,
                    'combined_key': obj.combined_key,
                    'country_region': obj.country_region,
                    'province_state': obj.province_state,
                    'lat': 0,
                    'long': 0,
                    'population': 0,
                }
                
                new_lookup_obj = self.model(**kwargs)
                self.object_list.append(new_lookup_obj)

    def get_max_uid(self):
        max_uid = 0
        for obj in self.get_objects():
            if obj.uid > max_uid:
                max_uid = obj.uid
        return max_uid + 1

    def get_combined_keys(self):
        return (obj.combined_key for obj in self.get_objects())
    
    def get_country_info(self, country_region):
        for obj in self.get_objects():
            if obj.country_region == country_region:
                return {
                    'uid': self.get_max_uid(),
                    'capture_date': obj.capture_date,
                    'iso2': obj.iso2,
                    'iso3': obj.iso3,
                    'code3': obj.code3,
                    'province_state': obj.province_state,
                    'country_region': obj.country_region,
                    'population': 0,
                }