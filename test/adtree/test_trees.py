from __future__ import annotations

import inspect

from adtree.models import Attack, ADTree, ExternalADTree
from adtree.themes import NoFormatTheme


def build_tree():
    some_external_ref = ExternalADTree("EXT.01", "External resource covered by other docs")
    some_internal_ref1 = ADTree("INT.01", root_node=Attack("internal path1", [
        Attack("path 1.1", [
            ADTree("INT.01.A", Attack("nested path 1.1A"))
        ])
    ]))
    some_internal_ref2 = ADTree("INT.02", root_node=Attack("internal path2", [
        Attack("path 2.1")
    ]))
    tree = ADTree("REFS.01", Attack("node1", [
        some_external_ref,
        some_internal_ref1,
        some_internal_ref2
    ]))
    return tree


def test_references_default(approvals):
    approvals.verify(build_tree(), inspect.currentframe().f_code, NoFormatTheme())


def test_references_all_toggled(approvals):
    approvals.verify(build_tree(), inspect.currentframe().f_code, NoFormatTheme())
