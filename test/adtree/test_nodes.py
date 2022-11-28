from __future__ import annotations

import inspect

from adtree.models import Attack, Defence, AndGate, ADTree
from adtree.themes import NoFormatTheme


def test_share_node(approvals):
    shared_node = Attack("shared node", [Defence("node 1 defence")])
    tree = ADTree("REFS.01", Attack("root", [
        Attack("path1", [
            shared_node
        ]),
        Attack("path2", [
            shared_node
        ]),
    ]))

    approvals.verify(tree, inspect.currentframe().f_code, NoFormatTheme())


def test_do_not_share_and_gate(approvals):
    tree = ADTree("REFS.01", Attack("don't share AND", [
        AndGate([
            Attack("path1"),
            Attack("path2")
        ]),
        AndGate([
            Attack("path3"),
            Attack("path4")
        ])
    ]))

    approvals.verify(tree, inspect.currentframe().f_code, NoFormatTheme())
