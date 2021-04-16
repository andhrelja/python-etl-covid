from datetime import date
from .clean import clean_key
from .definitions import (
    TIME_SERIES_TRANSFORM,
    DAILY_REPORTS_TRANSFORM,
    LOOKUP_TRANSFORM
)

# Base model to represent a CSV file model based on the definitions script
class BaseSource(object):
    transformation = None

    def __init__(self, **kwargs):
        if not self.transformation:
            raise TypeError("BaseSource should not be used without the transformation attribute")
        
        self.capture_date = date.today()
        
        for key, value in kwargs.items():
            key = clean_key(key)

            if key != "combined_key":
                try:
                    value = self.transformation[key](value)
                except ValueError:
                    value = self.transformation[key](float(value))
                except KeyError:
                    if key.endswith("_20") or key.endswith("_21"):
                        pass
                    else:
                        raise KeyError    
                setattr(self, key, value)
        self.set_combined_key()

    def set_combined_key(self):
        self.combined_key = self.transformation['combined_key'](self.province_state, self.country_region)

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return "<source.models.{} country={}>".format(self.__class__.__name__, self.country_region)
    
    def __repr__(self):
        return "<source.models.{} country={}>".format(self.__class__.__name__, self.country_region)


class TimeSeriesSource(BaseSource):
    transformation = TIME_SERIES_TRANSFORM


class DailyReportsSource(BaseSource):
    transformation = DAILY_REPORTS_TRANSFORM


class LookupSource(BaseSource):
    transformation = LOOKUP_TRANSFORM
