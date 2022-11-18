from brownie import networks,config ,Advancedcollectible
from scripts.helpful_scripts import get_accounts,fund_with_link
from web3 import Web3
def main():
   account = get_accounts()
   advanced_collectible = Advancedcollectible [-1]
   fund_with_link(advanced_collectible.address,amount =Web3.toWei(0.1 ,'ether'))
   creation_transaction =advanced_collectible.CreateCollectible({"from":account})
   creation_transaction.wait()
   print("Collectible created!")