from __future__ import annotations

import inspect

from adtree.models import Attack, ADTree, ExternalADTree
from adtree.themes import NoFormatTheme


def test_references(approvals):
    some_external_ref = ExternalADTree("EXT.01", "External resource covered by other docs")
    some_internal_ref = ADTree("INT.01", root_node=Attack("internal path1", [
        Attack("path 1.1")
    ]))

    tree = ADTree("REFS.01", Attack("node1", [
        some_external_ref,
        some_internal_ref
    ]))

    approvals.verify(tree, inspect.currentframe().f_code, NoFormatTheme())
