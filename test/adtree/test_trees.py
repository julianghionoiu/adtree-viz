from __future__ import annotations

import inspect

from adtree.models import Attack, ADTree, ExternalADTree
from adtree.themes import NoFormatTheme


def build_test_tree():
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
    return {
        "tree": tree,
        "internal_ref_to_expand": some_internal_ref1
    }


def test_references_default(approvals):
    test_tree_obj = build_test_tree()
    approvals.verify(tree=test_tree_obj["tree"],
                     theme=NoFormatTheme(),
                     test_code=inspect.currentframe().f_code)


def test_references_some_toggled(approvals):
    test_tree_obj = build_test_tree()
    approvals.verify(tree=test_tree_obj["tree"],
                     subtrees_to_expand=[test_tree_obj["internal_ref_to_expand"]],
                     theme=NoFormatTheme(),
                     test_code=inspect.currentframe().f_code)
