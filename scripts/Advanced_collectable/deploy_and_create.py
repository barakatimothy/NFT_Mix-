
from scripts.helpful_scripts import get_accounts,open_sea,get_contratcts
from brownie import Advancesdcollectible


def deploy_and_create():
    account = get_account()
    advanced_collectible = Advancesdcollectible.deploy(
        get_contratcts("vrf_coordinator"),
        get_contratcts("link_token"),
        config['networks'][network.show_active()]["link_token"],
        config['networks'][network.show_active()]["key_hash"],
        config['networks'][network.show_active()]["fee"],
        {'from':account})
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({'from':account})
    creating_tx.wait(1)
    print("new token Minted")
    
def main():
    deploy_and_create()