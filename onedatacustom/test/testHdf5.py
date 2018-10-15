import unittest
import os
import onedatacustom.metadataextractor
class Hdf5Test(unittest.TestCase):
    currentDir=os.path.dirname(os.path.abspath(__file__))
    def testHDF5(self):
        self.assertEqual(onedatacustom.metadataextractor.extract(self.currentDir+"/ressources/gamma_test.hdf5"), '{"TelescopeID": "AFX123", "trigger": 112456, "CaptureDate": "2012-04-23T18:25:08", "EventID": "UIDASDBN456"}')

    def testZfits(self):
        self.assertEqual(onedatacustom.metadataextractor.extract(self.currentDir+"/ressources/example_9evts_NectarCAM.fits.fz"), '{"TelescopeID": "0", "CaptureDate": "1975-07-08T09:35:45"}')
