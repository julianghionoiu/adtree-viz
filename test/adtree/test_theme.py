from __future__ import annotations

import inspect

from adtree.models import Attack, Defence, AndGate, ADTree
from adtree.themes import RedBlueFillTheme, RedGreenOutlineTheme


def test_render_fill(approvals):
    tree = ADTree("REFS.01", Attack("the goal", [
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
    ]))
    approvals.verify(tree, inspect.currentframe().f_code, RedBlueFillTheme())


def test_render_outline(approvals):
    tree = ADTree("REFS.01", Attack("the goal", [
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
    ]))
    approvals.verify(tree, inspect.currentframe().f_code, RedGreenOutlineTheme())

