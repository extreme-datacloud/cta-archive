import requests
import json
import csv
import os


class RestQuery:

    def __init__(self, hostname,token):
        self. headers = {'X-Auth-Token': token}
        self.hostname=hostname
        requests.packages.urllib3.disable_warnings()

    def get_spaceId(self):
        url = "https://"+self.hostname+"/api/v3/onezone/user/spaces"
        response = requests.request("GET", url, headers=self.headers, verify=False)
        return (response.text)

    def get_attributefromfile(self,path):
        url = "https://"+self.hostname+"/api/v3/oneprovider/attributes/SPACE-SMALL/"+path
        response = requests.request("GET", url, headers=self.headers, verify=False)
        #print(url)
        #print(response.text)
        return (json.loads(response.text))

    def get_attributeextendedfromfile(self,path):
        url = "https://"+self.hostname+"/api/v3/oneprovider/attributes/SPACE-SMALL/"+path
        querystring= {"extended":"true"}
        response = requests.request("GET", url, headers=self.headers, verify=False, params=querystring)
        #print(url)
        #print(response.text)
        return (json.loads(response.text))


def main(pathdirectory0, scalefactor, nbr_of_file_per_directory):

    restquery=RestQuery("cc-xdc02.in2p3.fr","MDAxNWxvY2F00aW9uIG9uZXpvbmUKMDAzMGlkZW500aWZpZXIgOTIzNDBmZjkyYTI1Y2RjZTlhM2ZmMWIyYTE5MGJjMGEKMDAxYWNpZCB00aW1lIDwgMTU3NTM4MDY00MwowMDJmc2lnbmF00dXJlIGnMtasbKyvaMI84gZo0061QqELeHb1KJBFJulqOmTdBsCg")

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
                    jsonAttribute=restquery.get_attributefromfile(filename)
                    jsonAttributeExtended=restquery.get_attributeextendedfromfile(filename)
                    writer.writerow({'file':jsonAttribute["name"],'ctime':jsonAttribute["ctime"],'ctime':jsonAttribute["ctime"], 'atime':jsonAttribute["atime"],'Extractiontime':int(jsonAttributeExtended["onedata_json"]["Extractiontime"])})


if __name__ == '__main__':
    main("testA",2 ,500)
