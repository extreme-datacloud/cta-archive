#!/usr/bin/python

import h5py
import json
import os
from datetime import datetime
import time
import sys
import shutil

from . import restquery as rq


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
        self.h5_file = h5py.File(h5_file_path, 'a')
        self.meta_dataset=self.h5_file

    def set_trigger_value(self, trigger_value):
        self.meta_dataset.attrs[self.trigger]=trigger_value

    def get_trigger_value(self):
        return self.meta_dataset.attrs[self.trigger]

    def set_telescope_id_value(self, telescope_ID_value):
        self.meta_dataset.attrs[self.telescope_ID]=telescope_ID_value

    def get_telescope_id_value(self):
        return self.meta_dataset.attrs[self.telescope_ID]

    def set_capture_date_value(self, time_stamp_value):
        self.meta_dataset.attrs[self.capture_date]=time_stamp_value
        # 1335198308->2012-04-23T16:25:43.511Z
        # datetime.strptime("2012-04-23T16:25:43.511Z","%Y-%m-%dT%H:%M:%S.%fZ").time()
        #self.h5_file.create_dataset(self.capture_date, (1,1), 'i8',time_stamp_value)

    def get_telescope_id_value(self):
        return self.meta_dataset.attrs[self.capture_date]

    def set_event_id_value(self, event_ID_value):
        self.meta_dataset.attrs[self.event_id]=event_ID_value
        #ascii_event_value = [event_ID_value.encode("ascii", "ignore") ]
        #self.h5_file.create_dataset(self.event_id, (1,1), 'S20', ascii_event_value)

    def get_event_id_value(self):
        return self.meta_dataset.attrs[self.event_id]

    def generate_several_HDF5_file(nbr_of_file_per_directory, scalefactor, root_path_to_volumes, relative_path_to_volume, sleeptime=1, connectiontuple=None):
        try:
            shutil.rmtree(root_path_to_volumes+relative_path_to_volume)
        except :
            print ("Oops! directory does not yet exist")

        os.mkdir(root_path_to_volumes+""+relative_path_to_volume)
        start= time.time()
        for j in range (1,scalefactor+1):
            pathdirectory1=relative_path_to_volume+"/"+str(j)
            os.mkdir(root_path_to_volumes+pathdirectory1)
            for k in range (1,scalefactor+1):
                pathdirectory2=pathdirectory1+"/"+str(k)
                os.mkdir(root_path_to_volumes+pathdirectory2)
                print (str(j)+":"+str(k))
                for i in range (0,nbr_of_file_per_directory):
                    file_id=int(str(j)+str(k)+str(i).zfill(3))
                    fileName=pathdirectory2+"/gamma_test_generated_"+str(file_id)+".hdf5"
                    metadatagenerator=generate(root_path_to_volumes+fileName)
                    metadatagenerator.set_trigger_value(file_id)
                    metadatagenerator.set_capture_date_value(1335198308+file_id)
                    metadatagenerator.set_event_id_value("UIDASDBN"+str(file_id/10))
                    metadatagenerator.set_telescope_id_value("AFX"+str(file_id%100))
                    if connectiontuple!=None:
                        restquery=rq(connectiontuple[0],connectiontuple[1])
                        restquery.set_attribute(fileName,root_path_to_volumes)


                time.sleep(sleeptime)
        end=time.time()
        print ("time to generate {:d} files is {:f} s".format(nbr_of_file_per_directory*(scalefactor-1)**2, end-start))

def generate(file_path):
    if file_path.endswith('.hdf5'):
        return MetaDataGeneratorHdf5(file_path)
    else:
        raise Exception("File format not supported")


def main():
    print (sys.argv[1])
    print (sys.argv[2])

    if len(sys.argv)>4 :
        root_path_to_volumes=sys.argv[4]
    else :
        root_path_to_volumes=os.path.dirname(os.path.abspath(__file__))+"/ressources/volumes/"

    if len(sys.argv)>5 :
        relative_path_to_volumes=sys.argv[5]
    else :
        relative_path_to_volumes="/space/"

    if len(sys.argv)>6 :
        host=sys.argv[5]
    else :
        host="lapp-xdc01.in2p3.fr"

    if len(sys.argv)>7 :
        token=sys.argv[6]
    else :
        token="MDAxNWxvY2F00aW9uIG9uZXpvbmUKMDAzMGlkZW500aWZpZXIgOTIzNDBmZjkyYTI1Y2RjZTlhM2ZmMWIyYTE5MGJjMGEKMDAxYWNpZCB00aW1lIDwgMTU3NTM4MDY00MwowMDJmc2lnbmF00dXJlIGnMtasbKyvaMI84gZo0061QqELeHb1KJBFJulqOmTdBsCg"

    MetaDataGeneratorHdf5.generate_several_HDF5_file(int(sys.argv[1]),int(sys.argv[2]),root_path_to_volumes,relative_path_to_volumes,int(sys.argv[3]),(host,token))

if __name__ == '__main__':
    main()
