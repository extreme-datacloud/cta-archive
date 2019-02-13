import requests
import json
import csv
from onedatacustom.metadataextractor import MetaDataExtractorHdf5


class RestQueryClass:
    def __init__(self, hostname,token):
        self. headers = {'X-Auth-Token': token,"Content-type": "application/json"}
        self.hostname=hostname
        requests.packages.urllib3.disable_warnings()

    def get_spaceId(self):
        url = "https://"+self.hostname+"/api/v3/onezone/user/spaces"
        response = requests.request("GET", url, headers=self.headers, verify=False)
        return (response.text)

    def get_attributefromfile(self, fileName, space_name):
        url = "https://" + self.hostname +"/api/v3/oneprovider/attributes/" + space_name +"/" + fileName
        response = requests.request("GET", url, headers=self.headers, verify=False)
        #print(url)
        #print(response.text)
        return (json.loads(response.text))

    def get_attributeextendedfromfile(self, fileName, space_name):
        url = "https://" + self.hostname +"/api/v3/oneprovider/attributes/" + space_name +"/" + fileName+"?extended=true"
        querystring= {"%22extended%22":"%22true%22"}
        response = requests.request("GET", url, headers=self.headers, verify=False, params=querystring)
        #print(url)
        #print(response.text)
        return (json.loads(response.text))

    def set_attribute(self, fileName, root_path_to_volumes):
        meta_data_extractor=MetaDataExtractorHdf5(root_path_to_volumes+fileName)
        print("attaching metadata to" +fileName + str(meta_data_extractor.to_json()))
        url = "https://" + self.hostname +"/api/v3/oneprovider/metadata/" + fileName
        response = requests.request( "PUT", url, json=meta_data_extractor.to_dic(), headers=self.headers, verify=False)

        print(url)
        print(response)
        #self.pretty_print_POST(response)




def retrieveMetadata(pathdirectory0, scalefactor, nbr_of_file_per_directory):

    restquery=RestQueryClass("cc-xdc02.in2p3.fr","MDAxNWxvY2F00aW9uIG9uZXpvbmUKMDAzMGlkZW500aWZpZXIgOTIzNDBmZjkyYTI1Y2RjZTlhM2ZmMWIyYTE5MGJjMGEKMDAxYWNpZCB00aW1lIDwgMTU3NTM4MDY00MwowMDJmc2lnbmF00dXJlIGnMtasbKyvaMI84gZo0061QqELeHb1KJBFJulqOmTdBsCg")

    with open('./resultQuery/resultExtraction.csv', 'w', newline='') as csvfile:
        fieldnames = ["file", "ctime", "mtime", "atime", "Extractiontime"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for j in range (1,scalefactor+1):
            pathdirectory1=pathdirectory0+"/"+str(j)
            for k in range (1,scalefactor+1):
                pathdirectory2=pathdirectory1+"/"+str(k)
                print (str(j)+":"+str(k))
                for i in range (0,nbr_of_file_per_directory):
                    file_id=int(str(j)+str(k)+str(i).zfill(3))
                    filename=pathdirectory2+"/gamma_test_generated_"+str(file_id)+".hdf5"
                    print (filename)
                    jsonAttribute=restquery.get_attributefromfile(filename,"SPACE_SMALL")
                    jsonAttributeExtended=restquery.get_attributeextendedfromfile(filename, "SPACE_SMALL")
                    writer.writerow({'file':jsonAttribute["name"],'ctime':jsonAttribute["ctime"],'ctime':jsonAttribute["ctime"], 'atime':jsonAttribute["atime"],'Extractiontime':int(jsonAttributeExtended["onedata_json"]["Extractiontime"])})


if __name__ == '__main__':
   restquery=RestQueryClass("lapp-xdc01.in2p3.fr","MDAxNWxvY2F00aW9uIG9uZXpvbmUKMDAzMGlkZW500aWZpZXIgOTIzNDBmZjkyYTI1Y2RjZTlhM2ZmMWIyYTE5MGJjMGEKMDAxYWNpZCB00aW1lIDwgMTU3NTM4MDY00MwowMDJmc2lnbmF00dXJlIGnMtasbKyvaMI84gZo0061QqELeHb1KJBFJulqOmTdBsCg")
   restquery.set_attribute("SPACE-SMALL/testA4/1/1/gamma_test_generated_11001.hdf5","/mnt/c/git/cta-archive/test/ressources/tmp/")

