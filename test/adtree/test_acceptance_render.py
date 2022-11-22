from __future__ import annotations

import inspect
import os
from abc import ABC, abstractmethod
from typing import List

from graphviz import Graph
import filecmp


class Theme(ABC):
    @abstractmethod
    def get_graph_attrs(self):
        pass

    @abstractmethod
    def get_node_attrs_for(self, node: Node):
        pass

    @abstractmethod
    def get_edge_attrs_for(self, node_parent: Node, node_child: Node):
        pass


class NoFormatTheme(Theme):

    def get_graph_attrs(self):
        return {}

    def get_node_attrs_for(self, node: Node):
        return {}

    def get_edge_attrs_for(self, node_parent: Node, node_child: Node):
        return {}


class BaseTheme(Theme):

    def get_graph_attrs(self):
        return {
            "overlap": "False",
            "splines": "True",
            "nodesep": "0.2",
            "ranksep": "0.4"
        }

    def get_node_attrs_for(self, node: Node):
        return {
            "color": "#000000",
            "fillcolor": "#ffffff",
            "shape": "box",
            "style": "rounded",
            "fontname": "Arial",
            "margin": "0.2"
        }

    def get_edge_attrs_for(self, node_parent: Node, node_child: Node):
        return {
            "fontname": "Arial",
            "color": "#1f1f1f",
            "style": "solid"
        }


class RedBlueFillTheme(BaseTheme):

    def get_node_attrs_for(self, node: Node):
        base_attrs = super().get_node_attrs_for(node) | {
            "shape": "plaintext",
            "style": "filled, rounded"
        }

        if node.__class__ == Attack:
            return base_attrs | {
                "fillcolor": "#ff5c5c",
            }
        elif node.__class__ == Defence:
            return base_attrs | {
                "fillcolor": "#5cc1ff",
            }
        elif node.__class__ == AndGate:
            return base_attrs | {
                "shape": "triangle",
                "color": "#ff5c5c",
                "fillcolor": "#ff5c5c",
                "margin": "0.05"
            }
        else:
            return base_attrs

    def get_edge_attrs_for(self, node_parent: Node, node_child: Node):
        base_attrs = super().get_edge_attrs_for(node_parent, node_child)

        if (node_parent.__class__ == Attack and node_child.__class__ == Defence) or (
                node_parent.__class__ == Defence and node_child.__class__ == Attack):
            return base_attrs | {
                "style": "dashed"
            }
        else:
            return base_attrs


class Node(object):
    def __init__(self, label: str = "", child_nodes: List[Node] = None):
        self.label = label
        if child_nodes is None:
            self.child_nodes = []
        else:
            self.child_nodes = child_nodes

    def get_label(self) -> str:
        return self.label

    def get_child_nodes(self) -> List[Node]:
        return self.child_nodes

    def __repr__(self):
        return f"{self.__class__.__name__}:{self.label}"


class Attack(Node):
    def __init__(self, label: str = "", child_nodes: List[Node] = None):
        super().__init__(label=label, child_nodes=child_nodes)


class Defence(Node):
    def __init__(self, label: str = "", child_nodes: List[Node] = None):
        super().__init__(label=label, child_nodes=child_nodes)


class AndGate(Node):
    def __init__(self, child_nodes: List[Node] = None):
        super().__init__(label="AND", child_nodes=child_nodes)


class Renderer(object):
    def __init__(self, theme: Theme = None, output_format: str = "png", view=False):
        self.output_format = output_format
        self.view = view
        if theme is None:
            self.theme = NoFormatTheme()
        else:
            self.theme = theme

    def render(self, root_node: Node, filename: str = "attacktree-graph"):
        dot = Graph(graph_attr=self.theme.get_graph_attrs(),
                    format=self.output_format)

        self._add_node(dot, "R", root_node)

        dot.render(filename, view=self.view)

    def _add_node(self, dot: Graph, current_id: str, current_node: Node):
        node_attrs = self.theme.get_node_attrs_for(current_node)
        dot.node(current_id, current_node.label, **node_attrs)

        for child_index, child_node in enumerate(current_node.get_child_nodes()):
            child_id = current_id + "." + str(child_index)

            self._add_node(dot, child_id, child_node)
            edge_attrs = self.theme.get_edge_attrs_for(current_node, child_node)
            dot.edge(current_id, child_id, **edge_attrs)


def test_render_simple_tree():
    root_node = Attack("the goal", [
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

    renderer = Renderer(theme=RedBlueFillTheme(), output_format="png")

    filename_without_extension, ext = os.path.splitext(inspect.currentframe().f_code.co_filename)
    output_file_base = "{0}.{1}".format(filename_without_extension, inspect.currentframe().f_code.co_name)
    actual_output_file = "{0}.actual.dot".format(output_file_base)
    expected_output_file = "{0}.expected.dot".format(output_file_base)

    renderer.render(root_node=root_node, filename=actual_output_file)

    assert filecmp.cmp(expected_output_file, actual_output_file), "dot file differs from expected"
    assert filecmp.cmp(expected_output_file+".png", actual_output_file+".png"), "png file differs from expected"


