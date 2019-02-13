import unittest
import os
from onedatacustom import  metadataextractor, metadatagenerator, restquery

import test.util.counter as count
import time
import requests

class Hdf5Test(unittest.TestCase):
    currentDir=os.path.dirname(os.path.abspath(__file__))
    def testHDF5Extractor(self):
        start= time.time()
        output_json=metadataextractor.extract(self.currentDir+"/ressources/gamma_test.hdf5")
        print("output_json extractor"+str(output_json))
        self.assertIn('{"TelescopeID": "AFX123", "trigger": 112456, "CaptureDate": "2012-04-23 16:25:08", "EventID": "UIDASDBN456"',output_json)
        end=time.time()
        print ("time to parse files is {:f} s".format(end-start))

    def testHDF5Generator(self):
        metadatageneratorImpl=metadatagenerator.generate(self.currentDir+"/ressources/gamma_test_generated.hdf5")
        metadatageneratorImpl.set_trigger_value(112457)
        metadatageneratorImpl.set_capture_date_value(1335198308)
        metadatageneratorImpl.set_event_id_value("UIDASDBN456")
        metadatageneratorImpl.set_telescope_id_value("AFX123")
        output_json=metadataextractor.extract(self.currentDir+"/ressources/gamma_test_generated.hdf5")
        print("output_json generator"+str(output_json))
        self.assertIn('{"TelescopeID": "AFX123", "trigger": 112457, "CaptureDate": "2012-04-23 16:25:08", "EventID": "UIDASDBN456"',output_json, )

    def testLoopHDF5Generator(self, nbrfileperdirectory=2, scalefactor=2, root_path_to_volumes=os.path.dirname(os.path.abspath(__file__))+"/ressources/volumes/",relative_path_to_volumes="space",sleeptime=1 ):
        metadatagenerator.MetaDataGeneratorHdf5.generate_several_HDF5_file(nbrfileperdirectory,scalefactor,root_path_to_volumes, relative_path_to_volumes,sleeptime)
        counter = count.Counter(root_path_to_volumes+relative_path_to_volumes)
        total_file = 0
        for cls in counter.work():
            total_file += cls.files
        print("nbr files generated "+str(total_file))
        self.assertEqual(total_file,nbrfileperdirectory*(scalefactor)**2)

    def testRestQuery(self):
        restqueryImpl=restquery.RestQueryClass("noHostanme","noToken")
        with self.assertRaises(requests.exceptions.ConnectionError):
            restqueryImpl.get_attributefromfile("fakeFile","fakeSpace")


