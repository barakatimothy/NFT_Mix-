from scripts.helpful_scripts import LOCAL_BLOCKCHAIN,get_accounts,get_contratcts
from brownie import network
import pytest
from scripts.simple_collectible.deploy_and_create import deploy_and_create

def test_can_create_advanced_collectible():
  if network.show_active() not in LOCAL_BLOCKCHAIN:
      pytest.skip()
      advanced_collectible, creating_transaction= deploy_and_create()
      requestId =creating_transaction.events["requestedCollectible"]["requestId"]
      randomNumber = 777
      get_contratcts("vrf coordinator").callbackWithRandomness(requestId,randomNumber,advanced_collectible.address,{"from":get_accounts()})
      assert advanced_collectible.tokenCounter() == 1
      assert advanced_collectibel.tokenIdToBreed(0) == randomNumber%3