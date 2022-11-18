from brownie import Advancedcollectible,network
from scripts.helpful_scripts import get_breed
from metadata.sample_meta_data import meta_data_template
from pathlib import Path
import os
import requests
import json 
breed_to_image_uri ={
    "pug":"url",
    "shiba_inu":"url",
    "st_benard": "url" 
}


def main():
    advanced_collectible = Advancedcollectible[-1]
    num_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"you have created {num_of_advanced_collectibles}collectibles")
    for token_id  in range(num_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_filename =( f'./metadata/{network.show_active()}/{token_id}-{breed}.json')
        print (metadata_filename)
        collectible_metadata = meta_data_template
        
        if Path(metadata_filename).exists():
            print(f"{metadata_filename} already exists! delete it to Overwrite")
        else:
            print(f"Creating metadata file:{metadata_filename}")   
            collectible_metadata["name"]=breed
            collectible_metadata["description"]= f'An adorable {breed} pup'
            print(collectible_metadata)
            image_path= "./img/" + breed.replace("_","-")+ '.png'
            image_uri = None
            if os.getenv("UPLOAD_TO_IPFS") == "true":
                image_uri = image_uri if image_uri else breed_to_image_uri(breed)
            image_uri = upload_to_ipfs()
            collectible_metadata['image']= image_uri
            with open(metadata_filename,"w") as file:
                json.dump(collectible_metadata,file)
                if os.getenv("UPLOAD_TO_IPFS") == "true":
                      upload_to_ipfs(metadata_filename)
            
         
def upload_to_ipfs(filepath):
    with Path(filepath).open('rb')as fp:
        image_binary=fp.read()
        ##upload stuff...
        ipfs_url ='http://127.0.0.1:5001'
        endpoint ='api/V0/add'
        response = request.post(ipfs_url+ endpoint,files = {'files':image_binary})
        ipfs_hash = response.json() ["hash"] 
        # './img/0-PUG.png'-> '0-PUG.png'   
        file_name = filepath.split("/")[-1:][0]   
        image_uri = f"https://ipfs.io/ipfs{ipfs_hash}?filname={file_name}"
        print(image_uri)
        return image_uri