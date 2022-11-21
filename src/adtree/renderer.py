import json
from graphviz import Digraph
from adtree.models import Attack, Defence, Node

from importlib import resources
import logging


class Renderer(object):
    def _buildDot(
        self,
        node: Node,
        dot: Digraph,
        mapped_edges: dict = {},
        dotformat: dict = {},
        defended_path: bool = False,
    ):
        node_attr = None
        if node.__class__.__name__ in dotformat.keys():
            node_attr = dotformat[node.__class__.__name__]

        if node.__class__.__name__ in dotformat.keys():
            node_attr = dotformat[node.__class__.__name__]
            # Overload the default formatting shape if the Node is flagged as unimplemented

            node_label = node.label
            if isinstance(node, Defence):
                defended_path = True
            dot.node(node.uniq, node.label, **node_attr)
        else:
            dot.node(node.uniq, node.label)

        for edge in node.get_edges():
            # Setup default edge rendering style
            # TODO: Decide if we are talking about "path" or "edge"
            if defended_path is True:
                edge_attr = dotformat["defendedEdge"]
            else:
                edge_attr = dotformat["Edge"]

            label = edge.label

            # TODO: Replace edge mapping string (fancy) with dict of Edge object (simple)
            if f"{node.uniq}:{edge.childNode.uniq}" not in mapped_edges:
                # This is where the percentage % gets added
                dot.edge(node.uniq, edge.childNode.uniq, label=label, **edge_attr)
                # Keeps track of edge mapping so we don't get duplicates as we walk the tree, avoids never ending recursion
                mapped_edges[f"{node.uniq}:{edge.childNode.uniq}"] = True
                self._buildDot(
                    node=edge.childNode,
                    dot=dot,
                    mapped_edges=mapped_edges,
                    dotformat=dotformat,
                    defended_path=defended_path
                )  # recurse

    
    def loadStyle(self, path: str):
        # TODO: Do error handling
        with open(path) as json_file:
            style = json.load(json_file)

        return style

    def buildDot(
        self, root: Node = None, style: dict = None
    ):
        if root is None:
            return None

        # In case render is called multiple times, e.g jupyter
        dot = Digraph()
        dot.graph_attr["overlap"] = "false"
        dot.graph_attr["splines"] = "True"
        dot.graph_attr["nodesep"] = "0.2"
        dot.graph_attr["ranksep"] = "0.4"

        if style is None:
            with resources.open_text("adtree", "style.json") as fid:
                style = json.load(fid)

        self._buildDot(root, dot, dotformat=style)  # recursive call
        return dot

    def render(
        self,
        root: Node = None,
        style: dict = None,
        fname: str = "attacktree-graph",
        fout: str = "png",
    ):
        dot = self.buildDot(
            root=root, style=style
        )
        dot.format = fout
        dot.render(fname, view=True)
