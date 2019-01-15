#!/usr/bin/python

import h5py
import json
import os
from datetime import datetime
import time



class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


class MetaDataGeneratorHdf5:
    telescope_ID_list=[]
    telescope_ID = 'TelescopeID'
    trigger = 'trigger'
    capture_date = 'CaptureDate'
    event_id = 'EventID'
    current_time= 'currenttime'

    def __init__(self, h5_file_path):
        self.h5_file = h5py.File(h5_file_path, 'w')
        self.meta_dataset=self.h5_file

    def set_trigger_value(self, trigger_value):
        self.meta_dataset.attrs[self.trigger]=trigger_value

    def set_telescope_id_value(self, telescope_ID_value):
        self.meta_dataset.attrs[self.telescope_ID]=telescope_ID_value

    def set_capture_date_value(self, time_stamp_value):
        self.meta_dataset.attrs[self.capture_date]=time_stamp_value
        # 1335198308->2012-04-23T16:25:43.511Z
        # datetime.strptime("2012-04-23T16:25:43.511Z","%Y-%m-%dT%H:%M:%S.%fZ").time()
        #self.h5_file.create_dataset(self.capture_date, (1,1), 'i8',time_stamp_value)

    def set_event_id_value(self, event_ID_value):
        self.meta_dataset.attrs[self.event_id]=event_ID_value
        #ascii_event_value = [event_ID_value.encode("ascii", "ignore") ]
        #self.h5_file.create_dataset(self.event_id, (1,1), 'S20', ascii_event_value)

    def generate_several_HDF5_file(nbr_of_file_per_directory, pathdirectory0,scalefactor):
        #directory
        start= time.time()
        for j in range (0,scalefactor):
            pathdirectory1=pathdirectory0+"/"+str(j)
            os.mkdir(pathdirectory1,777)
            time.sleep(5)
            print (j)
            for k in range (0,scalefactor):
                pathdirectory2=pathdirectory1+"/"+str(k)
                os.mkdir(pathdirectory2,777)
                for i in range (0,nbr_of_file_per_directory):
                    file_id=i+k*scalefactor**2+j*scalefactor
                    metadatagenerator=generate(pathdirectory2+"/gamma_test_generated_"+str(file_id)+".hdf5")
                    metadatagenerator.set_trigger_value(file_id)
                    metadatagenerator.set_capture_date_value(1335198308+file_id)
                    metadatagenerator.set_event_id_value("UIDASDBN"+str(file_id/10))
                    metadatagenerator.set_telescope_id_value("AFX"+str(file_id%100))
        end=time.time()
        print ("time to generate {:d} files is {:f} s".format(nbr_of_file_per_directory*scalefactor**2, end-start))

def generate(file_path):
    if file_path.endswith('.fz'):
        print("not supported")
        # return MetaDataExtractorZfits(file_path).to_json()
    elif file_path.endswith('.hdf5'):
        return MetaDataGeneratorHdf5(file_path)
    else:
        raise Exception("File format not supported")
