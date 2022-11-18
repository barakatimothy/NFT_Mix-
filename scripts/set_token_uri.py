from brownie import network,Advancedcollectible
from scripts.helpful_scripts import get_breed,get_account
dog_metadat_dic={
    "st_benard":"url",
    'shiba_inu':'url',
     'pug' :url
}
def main():
    print(f"working on{network.show_active()} ")
    advanced_collectible = Advancedcollectible[-1]
    number_collectibles = advanced_collectible.tokkenCounter()
    print(f'You have{number_collectibles} tokenId')
    for token_id in range (number_collectibles):
        breed = advanced_collectible.tokenToBreed(token_id)
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI{token_id}")
            set_tokenURI(token_id ,advanced_collectible,dog_metadat_dic[breed])
def set_tokenURI(token_id,nft_contract,token_URI):            
        account = get_account()
        tx = nft_contract.setTokenURI(token_id,token_URI,{"from":account})
        tx.wait(1)
        print(f"Awesome!You can view your NFT at{OPEN_SEA.format(nft_contract.address,token_id)}")
        print("please wait 20 mins and hit refresh metadata button")