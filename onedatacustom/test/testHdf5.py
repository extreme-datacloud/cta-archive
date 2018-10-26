import unittest
import os
import onedatacustom.metadataextractor
import onedatacustom.metadatagenerator
import datetime

class Hdf5Test(unittest.TestCase):
    currentDir=os.path.dirname(os.path.abspath(__file__))
    #def testHDF5Extractor(self):
    #    self.assertEqual(onedatacustom.metadataextractor.extract(self.currentDir+"/ressources/gamma_test.hdf5"), '{"TelescopeID": "AFX123", "trigger": "112456", "CaptureDate": "2012-04-23T16:25:08", "EventID": "UIDASDBN456"}')

    def testHDF5Generator(self):
        metadatagenerator=onedatacustom.metadatagenerator.generate(self.currentDir+"/ressources/gamma_test_generated.hdf5")
        metadatagenerator.set_trigger_value(112457)
        metadatagenerator.set_capture_date_value(1335198308)
        metadatagenerator.set_event_id_value("UIDASDBN456")
        metadatagenerator.set_telescope_id_value("AFX123")

        print (onedatacustom.metadataextractor.extract(self.currentDir+"/ressources/gamma_test_generated.hdf5"))
        self.assertEqual(onedatacustom.metadataextractor.extract(self.currentDir+"/ressources/gamma_test_generated.hdf5"), '{"TelescopeID": "AFX123", "trigger": 112457, "CaptureDate": "2012-04-23T16:25:08", "EventID": "UIDASDBN456"}')

