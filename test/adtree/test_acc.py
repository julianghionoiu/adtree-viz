from __future__ import annotations

import inspect

from adtree.models import Attack, Defence, AndGate
from adtree.themes import RedBlueFillTheme, RedGreenOutlineTheme, NoFormatTheme


def test_render_fill_theme(approvals):
    tree = Attack("the goal", [
        Attack("path1", [
            Defence("defend path1", [
                Attack("path1 defence defeated")
            ])
        ]),
        Attack("path2", [
            Attack("path2.1"),
            AndGate([
                Attack("path3.1"),
                Attack("path3.2"),
            ]),
        ]),
    ])
    approvals.verify(tree, inspect.currentframe().f_code, RedBlueFillTheme())


def test_render_outline_theme(approvals):
    tree = Attack("the goal", [
        Attack("path1", [
            Defence("defend path1", [
                Attack("path1 defence defeated")
            ])
        ]),
        Attack("path2", [
            Attack("path2.1"),
            AndGate([
                Attack("path3.1"),
                Attack("path3.2"),
            ]),
        ]),
    ])
    approvals.verify(tree, inspect.currentframe().f_code, RedGreenOutlineTheme())


def test_share_node(approvals):
    shared_node = Attack("shared node", [Defence("node 1 defence")])
    tree = Attack("root", [
        Attack("path1", [
            shared_node
        ]),
        Attack("path2", [
            shared_node
        ]),
    ])

    approvals.verify(tree, inspect.currentframe().f_code, NoFormatTheme())


def test_do_not_share_and_gate(approvals):
    tree = Attack("don't share AND", [
        AndGate([
            Attack("path1"),
            Attack("path2")
        ]),
        AndGate([
            Attack("path3"),
            Attack("path4")
        ])
    ])

    approvals.verify(tree, inspect.currentframe().f_code, NoFormatTheme())
