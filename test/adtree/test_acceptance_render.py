
from adtree import *

import inspect

from adtree.models import Attack
from adtree.renderer import Renderer


def attack(param, children = []):
    pass


def and_gate(param):
    pass


def defence(param):
    pass


def test_ok():
    root_node = attack("Obtain secrets", [
        attack("Attack Vault clients"),
        attack("Attack Vault server",[
            attack("Obtain Vault token"),
            attack("Decrypt storage", [
                and_gate([
                    attack("Obtain access to the storage"),
                    attack("Network access to the CloudHSM"),
                    attack("Obtain HSM PIN")
                ]),
            ]),
        ]),
        defence("y"),
        and_gate("AND", [
            attack("x"),
            defence("y"),
        ])
    ])


    # attack("Obtain secrets",["attack clients"],
    # )
    # goal = Attack("Obtain secrets")
    # goal.add_attacks(
    #
    #
    # )
    #
    # goal.add_attack("attack clients")
    # goal.add_attack("attack server")
    #
    # goal.add_defence("x")
    #
    #
    # "obtain secrets", \
    #  "attack clients", \
    #  "attack server"
    #  "obtain Vault token"
    #  "decrypt the storage"

    Renderer().render(root=root_node, fname=inspect.currentframe().f_code.co_name)


