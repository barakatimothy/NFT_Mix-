
from scripts.helpful_scripts import get_accounts,Simplecollectible
sample_token_uri ="https://ipfs.io/ipfs/QmSsYRDAb1GZ?filename=pug.png"
open_sea = "https://testnets.opensea.io/assets/{}/{}"
def deploy_and_create():
    account = get_account()
    simple_collectible = Simplecollectible.deploy({"from":account})
    tx = simple_collectible(sample_token_uri,{"from":account})
    tx.wait(1)
    print(f"You can now view this NFT on{open_sea.format(simple_collectible.address,simple_collectible.tokenCounter()-1)}")
    return simple_collectible
def main():
    deploy_and_create()