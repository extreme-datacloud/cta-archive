import unittest
import os
from onedatacustom import  metadataextractorCtaContainer
import time
from ctapipe.utils import get_dataset_path


class CtaContainerTest(unittest.TestCase):
    currentDir=os.path.dirname(os.path.abspath(__file__))

    def testCtaContainerExtractor(self):
        file_path=get_dataset_path("gamma_test_large.simtel.gz")
        print(file_path)
        start= time.time()
        output_json=metadataextractorCtaContainer.extract(file_path)
        print("output_json extractor"+str(output_json))
        self.assertIn('{"is_simulation": true, "pointing_direction_alt": 1.2217304706573486, "pointing_direction_az": 0.0, "is_diffuse": true, "particle_type": 0, "run_id": 7514, "time": 1467926303, "simtel_version": 1462392225}',output_json)
        end=time.time()
        print ("time to parse files is {:f} s".format(end-start))
