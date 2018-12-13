**Installation:**

    0-prerequisit:
        anaconda 5.2
        python 3.6
    
    1-clone the project
        git clone https://gitlab.in2p3.fr/CTA-LAPP/cta-archive.git
    
    2-from the root of the project execute the following cmd:
    
        conda env create -f environment.yml
        conda activate ctaarchiveenv
        conda install numpy protobuf astropy
        pip install https://github.com/cta-sst-1m/protozfitsreader/archive/v1.0.2.tar.gz
        python setup.py install
        
    3-execute the following cmd to extract metadata from a file:
    
        onedataextractor path_To_Hdf5_Or_ZFits_File

**Running with Docker
        make docker-build
        make docker-test
    
    or test manually with test file in the container:
        docker run Frederic.Gillardo1/ctaarchive onedatacustom/test/ressources/example_9evts_NectarCAM.fits.fz
    or files outside of the container:
        docker run -v $PWD/onedatacustom/test/ressources:/data Frederic.Gillardo1/ctaarchive /data/example_9evts_NectarCAM.fits.fz
        
    
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
    
    Zfits
          If the input is Zfits file with the following MetaData :
             
                    TelescopeID : String = AFX123
                    CaptureDate : date = 1335198308 (it is the timeStamp in Z for 2012-04-23T18:25:43 Z)
                         
          The tool will return as output the following text (json object serialized):
                
          {
                    "TelescopeID": "AFX123",
                    "CaptureDate": 2012-04-23T18:25:43Z,
          }
                                 
    Note:
    Date will be encoded using ISO 8601



