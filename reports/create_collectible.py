from brownie import Advancedcollectible
from scripts.helpful_scripts import accounts,fund_with_link
from web3 import Web3

def main():
    account = get_account()
    advanced_collectible = Advancedcollectible[-1]
    fund_with_link(advanced_collectible.address,amount = Web3.toWei(0.1,'ether'))
    creation_transaction  = advanced_collectible.createCollectible({'from':account})
    creation_transaction.wait(1)
    print('collectible creaated')
    return advanced_collectible,creation_transaction