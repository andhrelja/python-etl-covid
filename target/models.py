from .definitions import (
    TIME_SERIES_DEFINITION,
    TIME_SERIES_TRANSFORM,
    DAILY_REPORTS_DEFINITION,
    DAILY_REPORTS_TRANSFORM,
    LOOKUP_DEFINITION,
    LOOKUP_TRANSFORM
)

# Base model to represent a CSV file model based on the definitions script
class BaseModel(object):
    definition = None
    transformation = None

    def __init__(self, **kwargs):
        if not self.definition or not self.transformation:
            raise TypeError("BaseModel should not be used without definition and transformation")

        for key, value in kwargs.items():
            if key in self.definition.keys():
                value = self.transformation[key](value)
                setattr(self, key, value)
        self.validate()
    
    def validate(self):
        for key, value in self.to_dict().items():
            _type = self.definition[key]
            
            if not isinstance(value, _type):
                raise TypeError("Expected {}, got {} for '{}'".format(_type, type(value), value))


    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return "<target.models.{} country={}>".format(self.__class__.__name__, self.country_region)
    
    def __repr__(self):
        return "<target.models.{} country={}>".format(self.__class__.__name__, self.country_region)


class TimeSeries(BaseModel):
    definition = TIME_SERIES_DEFINITION
    transformation = TIME_SERIES_TRANSFORM


class DailyReports(BaseModel):
    definition = DAILY_REPORTS_DEFINITION
    transformation = DAILY_REPORTS_TRANSFORM


class Lookup(BaseModel):
    definition = LOOKUP_DEFINITION
    transformation = LOOKUP_TRANSFORM
