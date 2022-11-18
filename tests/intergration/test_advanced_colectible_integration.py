from scripts.helpful_scripts import LOCAL_BLOCKCHAIN,get_accounts,get_contratcts
from brownie import network
import pytest
import time 
from scripts.simple_collectible.deploy_and_create import deploy_and_create

def test_can_create_advanced_collectible_intergration():
   ##Arrange
  if network.show_active()  in LOCAL_BLOCKCHAIN:
      pytest.skip("only for intergration testing")
      
      ##act
      advanced_collectible, creating_transaction= deploy_and_create()
      time.sleep(60)
      ##assert
      assert advanced_collectible.tokenCounter() == 1
      