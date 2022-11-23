from __future__ import annotations

from graphviz import Graph

from adtree.models import Node
from adtree.themes import Theme, NoFormatTheme


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

        node_cache = set()
        self._add_node(dot, root_node, node_cache)

        dot.render(filename, view=self.view)

    def _add_node(self, dot: Graph, current_node: Node, node_cache: set[str]):
        node_attrs = self.theme.get_node_attrs_for(current_node)
        dot.node(current_node.get_id(), current_node.get_label(), **node_attrs)
        node_cache.add(current_node.get_id())

        for child_index, child_node in enumerate(current_node.get_child_nodes()):
            if child_node.get_id() not in node_cache:
                self._add_node(dot, child_node, node_cache)
            edge_attrs = self.theme.get_edge_attrs_for(current_node, child_node)
            dot.edge(current_node.get_id(), child_node.get_id(), **edge_attrs)
