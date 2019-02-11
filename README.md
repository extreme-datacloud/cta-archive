**Installation:**

    0-prerequisit:
        anaconda 5.2
        python 3.6
    
    1-clone the project
        git clone https://gitlab.in2p3.fr/CTA-LAPP/cta-archive.git
    
    2-from the root of the project execute the following cmd:
        conda env create -f environment.yml
        conda activate ctaarchiveenv
        python setup.py install

**Command:**

    The following cmd can be executed :
    a-Extract Metadata into JSON format
        onedataextractor path_To_Hdf5
        
    b-Generate HDF5 file with random headers
        onedatagenerator 500 2 0 pathToTheDirectoryTOGenerateFiles
        500: nbr files per directories
        2²: nbr of directories
        0 latency between files generation between differents directories
    
    c-Collect result in csv file
        edit and run the RestQuery class
        
    d-display result
        edit and run in jupyter notebook the class ExtractionVisualisation.ipynb

        
**Running with Docker**

        make docker-build
        make docker-test
    
    
**Tool specification:**
 
    Hdf5
        If the input is HDF5 file with the following MetaData :
     
                   TelescopeID : String = AFX123
                   trigger : number = 112456
                   CaptureDate : date = 1335198308 (it is the timeStamp in Z for 2012-04-23T18:25:43 Z)
                   EventID: String = UIDASDBN456
     
        The tool will return as output the following text (json object serialized):
     
        {
                   "TelescopeID": "AFX123",
                   "trigger": 112456,   (no quote)
                   "CaptureDate": 2012-04-23T18:25:43Z,
                   "EventID":"UIDASDBN456"
        }
    
    Note:
    Date is encoded using ISO 8601
    
    frederic.gillardo@lapp.in2p3.fr




