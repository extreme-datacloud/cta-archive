import unittest
import os
from onedatacustom import  metadataextractorDebug
import time
from ctapipe.utils import get_dataset_path


class CtaContainerTest(unittest.TestCase):
    currentDir=os.path.dirname(os.path.abspath(__file__))

    def testCtaContainerExtractor(self):

        start= time.time()
        output_json=metadataextractorDebug.extract("fakefile", '"{"is_simulation": true, "pointing_direction_alt": 1.2217304706573486}"')
        print("output_json extractor"+str(output_json))
        self.assertIn('"{"is_simulation": true, "pointing_direction_alt": 1.2217304706573486}"',output_json)
        end=time.time()
        print ("time to parse files is {:f} s".format(end-start))
