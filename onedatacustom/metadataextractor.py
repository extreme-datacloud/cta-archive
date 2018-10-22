#!/usr/bin/python

import h5py
import json
import sys
from datetime import datetime

#from protozfits import File


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


class MetaDataExtractorHdf5:
    telescope_ID = 'TelescopeID'
    trigger = 'trigger'
    capture_date = 'CaptureDate'
    event_id = 'EventID'

    def __init__(self, h5_file_path):
        self.h5_file = h5py.File(h5_file_path, 'r')

    def get_trigger_value(self):
        return int(self.h5_file[self.trigger][0])

    def get_telescope_id_value(self):
        return str((self.h5_file[self.telescope_ID][0]).decode())

    def get_capture_date_value(self):
        # 1335198308->2012-04-23T16:25:43.511Z
        return datetime.utcfromtimestamp(self.h5_file[self.capture_date][0])

    def get_event_id_value(self):
        return (self.h5_file[self.event_id][0]).decode()

    def to_json(self):
        data = {self.telescope_ID: self.get_telescope_id_value(), self.trigger: self.get_trigger_value(),
                self.capture_date: self.get_capture_date_value(), self.event_id: self.get_event_id_value()}
        return json.dumps(data, cls=DateTimeEncoder)

"""
class MetaDataExtractorZfits:
    telescope_ID = 'TelescopeID'
    capture_date = 'CaptureDate'

    def __init__(self, zfits_file_path):
        zfits_file = File(zfits_file_path, 'r')
        self.header = next(zfits_file.RunHeader)

    def get_telescope_id_value(self):
        return str(self.header.telescopeID)

    def get_capture_date_value(self):
        return datetime.fromtimestamp(self.header.dateMJD)

    def to_json(self):
        data = {self.telescope_ID: self.get_telescope_id_value(), self.capture_date: self.get_capture_date_value()}
        return json.dumps(data, cls=DateTimeEncoder)
"""

def extract(file_path):
    if file_path.endswith('.fz'):
        print("not supported")
        # return MetaDataExtractorZfits(file_path).to_json()
    elif file_path.endswith('.hdf5'):
        return MetaDataExtractorHdf5(file_path).to_json()
    else:
        raise Exception("File format not supported")

def main():
    file_path = sys.argv[1]
    print(extract(file_path))
    exit(0)

if __name__ == '__main__':
    print(main())
