import utils
from tqdm import tqdm

class Manager(object):
    def __init__(self, Model, rows):
        self.model = Model
        self.dict_list = rows
        self.object_list = []

        self.set_objects()
        self.set_fieldnames()
        
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
    
    def write_objects(self, filepath):
        utils.write_csv(
            filepath,
            utils.generate_rows(self.object_list),
            self.fieldnames
        )


class TimeSeriesManager(Manager):
    def combine_sources(self):
        print("Combining Time Series ... ")
        new_object_list, new_objects_created = [], []
        for obj in tqdm(self.get_objects()):
            if (obj.uid, obj.capture_date) not in new_objects_created:
                new_objects_created.append((obj.uid, obj.capture_date))
                new_kwargs = {
                    'uid': obj.uid,
                    'capture_date': obj.capture_date
                }

                for _obj in self.get_existing_time_series(obj.uid, obj.capture_date):
                    if hasattr(_obj, 'confirmed'):
                        new_kwargs['confirmed'] = _obj.confirmed
                    elif hasattr(_obj, 'recovered'):
                        new_kwargs['recovered'] = _obj.recovered
                    elif hasattr(_obj, 'deaths'):
                        new_kwargs['deaths'] = _obj.deaths

                new_obj = self.model(**new_kwargs)
                new_object_list.append(new_obj)
        self.object_list = new_object_list
    
    def get_existing_time_series(self, uid, capture_date):
        for obj in self.get_objects():
            if obj.uid == uid and obj.capture_date == capture_date:
                yield obj