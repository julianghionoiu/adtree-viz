from __future__ import annotations

import inspect

from adtree.analysers import IsDefendedAnalyser
from adtree.models import Attack, Defence, AndGate, ADTree, Node, NodeType
from adtree.themes import NoFormatTheme


def test_is_defended(approvals):
    tree = ADTree("REFS.01", Attack("the goal", [
        Attack("path1", [
            Defence("defend path1", [
                Attack("path1 defence defeated")
            ])
        ]),
        Attack("path2", [
            Attack("path2.1", [
                Defence("def2.1"),
                Attack("path2.1.1")
            ]),
            AndGate([
                Attack("path3.1"),
                Attack("path3.2", [
                    Defence("defended")
                ]),
            ]),
        ]),
    ]))

    analyser = IsDefendedAnalyser()
    analyser.analyse_tree(tree)



    approvals.verify(tree=tree,
                     theme=CustomIsDefendedTheme(),
                     test_code=inspect.currentframe().f_code)


# ~~~~~~~~~~~~~~~~~~ Test support code ~~~~~~~~~~~~~~~~~~~

class CustomIsDefendedTheme(NoFormatTheme):
    def get_node_attrs_for(self, node: Node):
        metadata_attrs = {
            "style": "filled"
        }
        if node.get_node_type() == NodeType.DEFENCE:
            metadata_attrs |= {
                "shape": "box",
            }
        if node.get_node_type() == NodeType.AND_GATE:
            metadata_attrs |= {
                "shape": "triangle",
            }
        if node.has_metadata(IsDefendedAnalyser.METADATA_KEY):
            fillcolor = "#C8FFCB" if node.get_metadata(IsDefendedAnalyser.METADATA_KEY) else "#FFD3D6"
            metadata_attrs |= {
                "fillcolor": fillcolor,
            }
        return metadata_attrs
