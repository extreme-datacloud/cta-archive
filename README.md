Installation:

    0-prerequisit:
        anaconda 5.2
        python 3.6
    
    1-clone the project
        git clone https://gitlab.in2p3.fr/Frederic.Gillardo1/ctaarchive.git
    
    2-from the root of the project execute the following cmd:
    
        conda env create -f environment.yml
        conda activate ctaarchiveenv
        python setup.py install
        
    3-execute the following cmd to extract metadata from a file:
    
        onedataextractor pathToTheHdf5File



Tool specification:
 
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
    Date will be encoded using ISO 8601



