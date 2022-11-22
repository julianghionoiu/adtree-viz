from __future__ import annotations

import inspect
from abc import ABC, abstractmethod
from typing import List

from graphviz import Graph


class Theme(ABC):
    @abstractmethod
    def get_graph_attrs(self):
        pass

    @abstractmethod
    def get_node_attrs_for(self, node: Node):
        pass


class NoFormat(Theme):

    def get_graph_attrs(self):
        return {}

    def get_node_attrs_for(self, node: Node):
        return {}


class RedBlueFill(Theme):

    def get_graph_attrs(self):
        return {
            "overlap": "False",
            "splines": "True",
            "nodesep": "0.2",
            "ranksep": "0.4"
        }

    def get_node_attrs_for(self, node: Node):
        if node.__class__ == Attack:
            return {
                "color": "#ff5c5c",
                "shape": "plaintext",
                "style": "filled, rounded",
                "fontname": "Arial",
                "margin": "0.2"
            }
        elif node.__class__ == Defence:
            return {
                "color": "#5cc1ff",
                "shape": "plaintext",
                "style": "filled, rounded",
                "fontname": "Arial",
                "margin": "0.2"
            }
        else:
            return {}


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
    def __init__(self, theme: Theme = NoFormat()):
        self.theme = theme

    def render(self, root_node: Node, fname: str = "attacktree-graph", fout: str = "png"):
        dot = Graph(graph_attr=self.theme.get_graph_attrs())

        self._add_node(dot, "R", root_node)

        dot.format = fout
        dot.render(fname, view=True)

    def _add_node(self, dot: Graph, current_id: str, current_node: Node):
        dot.node(current_id, current_node.label, **self.theme.get_node_attrs_for(current_node))

        for child_index, child_node in enumerate(current_node.get_child_nodes()):
            child_id = current_id + "." + str(child_index)

            self._add_node(dot, child_id, child_node)
            dot.edge(current_id, child_id)


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

    Renderer(theme=RedBlueFill()).render(root_node=root_node, fname=inspect.currentframe().f_code.co_name)
