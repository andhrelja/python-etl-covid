import utils

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

    def set_combined_keys(self):
        for obj in self.object_list:
            obj.set_combined_key()

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
