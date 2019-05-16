#!/usr/bin/python

import json
import sys
from datetime import datetime
from ctapipe.io import event_source
from ctapipe.utils import get_dataset_path
from astropy import units


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


class MetaDataExtractorCtaContainer:
    datePattern='%Y-%m-%d %H:%M:%S'
    is_simulation = 'is_simulation'
    pointing_direction_az = 'pointing_direction_az'
    pointing_direction_alt = 'pointing_direction_alt'
    is_diffuse= 'is_diffuse'
    particle_type= 'particle_type'
    run_id='run_id'
    time='time'
    simtel_version= 'simtel_version'


    def __init__(self, container_file_path):
        self.source=event_source(container_file_path)
        self.event = next(iter(self.source))

    def get_is_simulation(self):
        return self.source.metadata.get("is_simulation")

    def get_is_diffuse(self):
        return self.source.metadata.get("is_simulation")

    def get_particle_type(self):
        return self.event.mc.shower_primary_id

    def get_run_id(self):
        return int(self.event.r0.obs_id)

    def get_time(self):
        return self.event.mcheader.detector_prog_start

    def get_pointing_direction_az(self):
        return (self.event.mcheader.run_array_direction[0].to(units.rad).value)

    def get_pointing_direction_alt(self):
        return(self.event.mcheader.run_array_direction[1].to(units.rad).value)

    def get_simtel_version(self):
        return self.event.mcheader.simtel_version

    def to_json(self):
         return json.dumps(self.to_dic(), cls=DateTimeEncoder)

    def to_dic(self):
        return {self.is_simulation: self.get_is_simulation(), self.pointing_direction_alt: self.get_pointing_direction_alt(), self.pointing_direction_az:self.get_pointing_direction_az(), self.is_diffuse:self.get_is_diffuse(), self.particle_type: self.get_particle_type(), self.run_id: self.get_run_id(),self.time: self.get_time(), self.simtel_version: self.get_simtel_version()}


def extract(file_path):
    return MetaDataExtractorCtaContainer(file_path).to_json()


def main():
    file_path = sys.argv[1]
    print(extract(file_path))
    exit(0)

if __name__ == '__main__':
    print(main())



def main():

    file_path=get_dataset_path("gamma_test_large.simtel.gz")
    print (file_path)
    print(extract(file_path))
    exit(0)

if __name__ == '__main__':
    print(main())
