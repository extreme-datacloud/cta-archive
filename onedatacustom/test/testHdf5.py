import unittest
import os
import shutil
import onedatacustom.metadataextractor
import onedatacustom.metadatagenerator
import onedatacustom.test.util.counter as count
import datetime
import sys
import time

class Hdf5Test(unittest.TestCase):
    currentDir=os.path.dirname(os.path.abspath(__file__))
    def testHDF5Extractor(self):
        start= time.time()
        output_json=onedatacustom.metadataextractor.extract(self.currentDir+"/ressources/gamma_test.hdf5")
        print("output_json extractor"+str(output_json))
        self.assertIn('{"TelescopeID": "AFX123", "trigger": 112456, "CaptureDate": "2012-04-23T16:25:08", "EventID": "UIDASDBN456"',output_json)
        end=time.time()
        print ("time to parse files is {:f} s".format(end-start))

    def testHDF5Generator(self):
        metadatagenerator=onedatacustom.metadatagenerator.generate(self.currentDir+"/ressources/gamma_test_generated.hdf5")
        metadatagenerator.set_trigger_value(112457)
        metadatagenerator.set_capture_date_value(1335198308)
        metadatagenerator.set_event_id_value("UIDASDBN456")
        metadatagenerator.set_telescope_id_value("AFX123")

        output_json=onedatacustom.metadataextractor.extract(self.currentDir+"/ressources/gamma_test_generated.hdf5")
        print("output_json generator"+str(output_json))
        self.assertIn('{"TelescopeID": "AFX123", "trigger": 112457, "CaptureDate": "2012-04-23T16:25:08", "EventID": "UIDASDBN456"',output_json, )

    def testLoopHDF5Generator(self, nbrfileperdirectory=2, scalefactor=2, path_to_volumes=os.path.dirname(os.path.abspath(__file__))+"/ressources/volumes/" ):
        try:
            shutil.rmtree(path_to_volumes)
        except :
            print ("Oops! directory does not yet exist")

        os.mkdir(path_to_volumes)
        onedatacustom.metadatagenerator.MetaDataGeneratorHdf5.generate_several_HDF5_file(nbrfileperdirectory,path_to_volumes,scalefactor)
        counter = count.Counter(path_to_volumes)
        total_file = 0
        for cls in counter.work():
            total_file += cls.files
        print("nbr files generated "+str(total_file))
        self.assertEqual(total_file,nbrfileperdirectory*scalefactor**2)

def main():
    hdf5Test=Hdf5Test()
    print (sys.argv[1])
    print (sys.argv[2])

    if len(sys.argv)>3 :
        path_to_volumes=sys.argv[3]
    else :
        path_to_volumes=os.path.dirname(os.path.abspath(__file__))+"/ressources/volumes/"

    hdf5Test.testLoopHDF5Generator(int(sys.argv[1]),int(sys.argv[2]),path_to_volumes)

if __name__ == '__main__':
    main()
