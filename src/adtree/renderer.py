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
