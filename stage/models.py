from .definitions import (
    TIME_SERIES_DEFINITION,
    TIME_SERIES_TRANSFORM,
    DAILY_REPORTS_DEFINITION,
    DAILY_REPORTS_TRANSFORM,
    LOOKUP_DEFINITION,
    LOOKUP_TRANSFORM
)

# Base model to represent a CSV file model based on the definitions script
class BaseStage(object):
    definition = None
    transformation = None

    def __init__(self, **kwargs):
        if not self.definition and not self.transformation:
            raise TypeError("BaseStage should not be used without definition and transformation attributes")
        
        for key, value in kwargs.items():
            try:
                value = self.transformation[key](value)
            except KeyError:
                if key.endswith("_20") or key.endswith("_21"):
                    value = float(value)
                    setattr(self, key, value)
                else:
                    keys = ('province_state', 'country_region', 'combined_key', 'lat', 'long')
                    if key in keys:
                        pass
                    else:
                        raise KeyError
            else:
                setattr(self, key, value)
        
        self.validate()

    def validate(self):
        for key, value in self.to_dict().items():
            try:
                _type = self.definition[key]
            except KeyError:
                if key.endswith("_20") or key.endswith("_21"):
                    pass
                else:
                    keys = ('province_state', 'country_region', 'combined_key', 'lat', 'long')
                    if key in keys:
                        pass
                    else:
                        raise KeyError("Expected one of {}, got '{}'".format(self.definition.keys(), key))
            else:
                if not isinstance(value, _type):
                    raise TypeError("Expected {}, got {} for '{}'".format(_type, type(value), value))

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return "<stage.models.{} country={}>".format(self.__class__.__name__, self.country_region)
    
    def __repr__(self):
        return "<stage.models.{} country={}>".format(self.__class__.__name__, self.country_region)


class TimeSeriesStage(BaseStage):
    definition = TIME_SERIES_DEFINITION
    transformation = TIME_SERIES_TRANSFORM


class DailyReportsStage(BaseStage):
    definition = DAILY_REPORTS_DEFINITION
    transformation = DAILY_REPORTS_TRANSFORM


class LookupStage(BaseStage):
    definition = LOOKUP_DEFINITION
    transformation = LOOKUP_TRANSFORM
