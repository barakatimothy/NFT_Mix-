from scripts.helpful_scripts import LOCAL_BLOCKCHAIN,get_accounts
from brownie import network
import pytest
from scripts.simple_collectible.deploy_and_create import deploy_and_create

def can_create_simple_collectible():
  if network.show_active() not in LOCAL_BLOCKCHAIN:
      pytest.skip()
      simple_collectible = deploy_and_create()
      assert simple_collectible.ownerOf(0)==get_account()